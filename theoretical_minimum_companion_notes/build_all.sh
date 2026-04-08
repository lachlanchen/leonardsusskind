#!/usr/bin/env bash
set -u

root="$(cd "$(dirname "$0")" && pwd)"
status=0

while IFS= read -r dir; do
  texfile="$(find "$dir" -maxdepth 1 -type f -name '*.tex' -printf '%f\n' | head -n1)"
  if [[ -z "$texfile" ]]; then
    continue
  fi

  base="${texfile%.tex}"
  logfile="$(mktemp)"

  echo "Building $dir/$texfile"

  (
    cd "$dir" || exit 1
    lualatex -interaction=nonstopmode -halt-on-error "$texfile"
    if rg -q '\\makeglossaries' "$texfile"; then
      makeglossaries "$base"
    fi
    bibtex "$base"
    lualatex -interaction=nonstopmode -halt-on-error "$texfile"
    lualatex -interaction=nonstopmode -halt-on-error "$texfile"
  ) >>"$logfile" 2>&1

  if [[ $? -ne 0 ]]; then
    mv "$logfile" "$dir/build.log"
    echo "FAILED  $dir/$texfile"
    status=1
  else
    rm -f "$logfile" "$dir/build.log"
    rm -f \
      "$dir/$base".{aux,bbl,bcf,blg,glg,glo,gls,idx,ilg,ind,ist,loe,lof,log,lol,lot,out,run.xml,toc,xdv,acn,acr,alg} \
      "$dir/$base".{glsdefs,glstex,ist,maf} \
      "$dir/$base".{xdy} \
      "$dir/"*.fdb_latexmk \
      "$dir/"*.fls \
      "$dir/"*.glstex \
      "$dir/"*.synctex.gz 2>/dev/null || true
    echo "OK      $dir/$base.pdf"
  fi
done < <(find "$root" -mindepth 3 -maxdepth 3 -type d | sort)

exit "$status"
