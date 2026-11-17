#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
work="$root/.translation-work"
revision=5684c0f51c0b81133db2efbe60a408b4155a3ff5
patterns="$work/texmf/tex/generic/translation-hyphenation"
mkdir -p "$patterns" "$work/texmf/tex/generic/config"
exec 9>"$work/tex-setup.lock"
flock -n 9 || { printf 'Translation TeX setup is already running.\n' >&2; exit 1; }

cat >"$work/hyphenation.sha256" <<'EOF'
374ad1ce3263f8a2791ec070ef9b516c532dae64456f3fb656e617e8ae53a9d3  hyph-de-1996.tex
6a2e5f39a991a23d1cd8a23dbd0f6fe96a9f07561a6695f4f3320f47030e236c  hyph-es.tex
526cad6fe8f52fcd3caa3fcaf667cb1740cfc14bca198680e00dc343a84594de  hyph-fr.tex
ce988fcc66e5e29d7474df5ab5b489d3f52a50ebccf570997f992d84221b922a  hyph-ru.tex
30fbe4f95f85ba5ae1adf80d3280e9e9bd53d8f2a56e157251c42f2e9632e188  loadhyph-de-1996.tex
6d6bfa74e8896320cea3cfc9360b33c1a02d4266ee111d674a511532e8490556  loadhyph-es.tex
42a59379a68359fb243cfc428bbc4347b1fb9832f82b9a29a62f79927ac2f95e  loadhyph-fr.tex
1842d24208200f3834f9a5da0a6db224d2c8eda046bf7e5220686988a4e9c7fc  loadhyph-ru.tex
708975d63ba0777eed42b57046d4514c88170c1c924ec714837870d753bd794d  hyph-quote-fr.tex
EOF

if [[ -f "$work/texmf-var/web2c/xetex/xelatex.fmt" && -f "$work/tex-ready" ]] &&
   [[ "$(cat "$work/tex-ready")" == "$revision" ]] &&
   (cd "$patterns" && sha256sum --check --status "$work/hyphenation.sha256"); then
  printf 'Translation XeLaTeX format and language patterns are ready.\n'
  exit 0
fi

while read -r expected file; do
  if [[ ! -f "$patterns/$file" ]] || [[ "$(sha256sum "$patterns/$file" | cut -d' ' -f1)" != "$expected" ]]; then
    case "$file" in
      loadhyph-*) subdir=loadhyph ;;
      hyph-quote-*) subdir=patterns/quote ;;
      *) subdir=patterns/tex ;;
    esac
    curl --fail --silent --show-error --location --retry 3 \
      "https://raw.githubusercontent.com/hyphenation/tex-hyphen/$revision/hyph-utf8/tex/generic/hyph-utf8/$subdir/$file" \
      -o "$patterns/$file.download"
    printf '%s  %s\n' "$expected" "$patterns/$file.download" | sha256sum --check
    mv "$patterns/$file.download" "$patterns/$file"
  fi
done <"$work/hyphenation.sha256"

# Isolate the new format from every other project's TeX configuration.
cp "$(kpsewhich language.dat)" "$work/texmf/tex/generic/config/language.dat"
cat >>"$work/texmf/tex/generic/config/language.dat" <<'EOF'
french loadhyph-fr.tex
spanish loadhyph-es.tex
ngerman loadhyph-de-1996.tex
=german
russian loadhyph-ru.tex
EOF
export TEXMFHOME="$work/texmf" TEXMFVAR="$work/texmf-var" TEXMFCONFIG="$work/texmf-config"
fmtutil-user --byfmt xelatex >"$work/tex-setup.log" 2>&1 || {
  tail -n 60 "$work/tex-setup.log" >&2
  exit 1
}
test -f "$work/texmf-var/web2c/xetex/xelatex.fmt"
printf '%s\n' "$revision" >"$work/tex-ready"
printf 'Prepared isolated translation XeLaTeX format with French, Spanish, German and Russian hyphenation.\n'
