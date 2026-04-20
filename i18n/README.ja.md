[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Leonard Susskind 講義ノートリポジトリ

> [LazyingArt LLC](https://lazying.art) 主導。Web サイト: [lazying.art](https://lazying.art) および [learn.lazying.art](https://learn.lazying.art)。

[![Archive](https://img.shields.io/badge/archive-active-16a34a?style=flat-square)](#)
[![Subtitles](https://img.shields.io/badge/subtitles-.srt-2563eb?style=flat-square)](#-repo-layout)
[![Transcripts](https://img.shields.io/badge/transcripts-markdown-0f766e?style=flat-square)](#-repo-layout)
[![Generated Notes](https://img.shields.io/badge/generated_notes-LaTeX-f97316?style=flat-square)](#-repo-layout)
[![PDF Outputs](https://img.shields.io/badge/outputs-PDF-a855f7?style=flat-square)](#-repo-layout)
[![Theoretical Minimum](https://img.shields.io/badge/focus-Theoretical%20Minimum-f59e0b?style=flat-square)](#)

このリポジトリは、Leonard Susskind の講義、より広い *Theoretical Minimum* エコシステム、そして文字起こしから派生した補助ノートを中心とする物理学学習アーカイブです。

講義の文字起こし、字幕ファイル、生成された TeX ノート、コンパイル済み PDF、手作業で保守されているコースフォルダを、安定したディレクトリ構成のもとにまとめています。

> 📘 完全な講義文字起こし、字幕ファイル、生成 TeX ノートのワークフロー、公開済みコース PDF は、ここでひとつのアーカイブとして管理されています。
>
> 🛠️ ここで使われているダウンロード、文字起こし、字幕からノートへの自動化は、補助ツールリポジトリ [Video2Book](https://github.com/lachlanchen/Video2Book) で管理されており、このリポジトリには `Video2Book/` サブモジュールとして含まれています。

## 📚 公開済み書籍

> 📷 プレビュー用カバー画像は各コース PDF の1ページ目から取得しており、ルート README とウェブサイトのカードが実際に公開されている本文とレイアウトに常に一致するようにしています。
>
> 📱 完成した書籍については Pocket-size / penguin 版も公開しています:
> [Pocket-size 1.0x](../all_notes/pocket_books/) と [Pocket-size 1.2x](../all_notes/pocket_books_1_2x/)。
> これらのコンパクト版は、10インチの電子ペーパーデバイスや iPad クラスの画面で快適に読めるよう最適化されています。

<table>
  <tr>
    <td colspan="4"><strong>コア</strong> · 古典 → 量子 → 特殊 → 一般 → 統計 → 宇宙論</td>
  </tr>
  <tr>
    <td align="center">
      <a href="../core_classical_mechanics/2011_fall_theoretical_minimum/classical_mechanics_theoretical_minimum.pdf"><img src="../figs/readme-covers/classical_mechanics_theoretical_minimum.png" width="170" alt="Classical Mechanics Theoretical Minimum cover"></a><br>
      <strong>古典力学</strong><br>
      <sub>2011年秋 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_classical_mechanics/2011_fall_modern_physics_stanford_partial/classical_mechanics_stanford_partial.pdf"><img src="../figs/readme-covers/classical_mechanics_stanford_partial.png" width="170" alt="Classical Mechanics Stanford partial cover"></a><br>
      <strong>古典力学</strong><br>
      <sub>Stanford 部分実施版</sub>
    </td>
    <td align="center">
      <a href="../core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><img src="../figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="170" alt="Quantum Mechanics cover"></a><br>
      <strong>量子力学</strong><br>
      <sub>2012年冬 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_quantum_mechanics/2012_winter_modern_physics_stanford/quantum_mechanics_modern_physics_stanford.pdf"><img src="../figs/readme-covers/quantum_mechanics_modern_physics_stanford_first_page.png" width="170" alt="Quantum Mechanics Modern Physics Stanford cover"></a><br>
      <strong>量子力学</strong><br>
      <sub>2012年冬 Modern Physics Stanford</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../core_special_relativity/2012_spring_theoretical_minimum/special_relativity_theoretical_minimum.pdf"><img src="../figs/readme-covers/special_relativity_theoretical_minimum.png" width="170" alt="Special Relativity cover"></a><br>
      <strong>特殊相対論</strong><br>
      <sub>2012年春 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><img src="../figs/readme-covers/general_relativity_theoretical_minimum.png" width="170" alt="General Relativity cover"></a><br>
      <strong>一般相対論</strong><br>
      <sub>2012年秋 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_general_relativity/2008_fall_einsteins_general_theory_of_relativity/general_relativity_2008_fall_einsteins_general_theory_of_relativity.pdf"><img src="../figs/readme-covers/general_relativity_2008_fall_einsteins_general_theory_of_relativity_first_page.png" width="170" alt="General Relativity 2008 cover"></a><br>
      <strong>一般相対論</strong><br>
      <sub>2008年秋 アインシュタイン一般理論</sub>
    </td>
    <td align="center">
      <a href="../core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><img src="../figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="170" alt="Statistical Mechanics and Thermodynamics cover"></a><br>
      <strong>統計力学</strong><br>
      <sub>2013年春 Theoretical Minimum</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><img src="../figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="170" alt="Cosmology Theoretical Minimum cover"></a><br>
      <strong>宇宙論</strong><br>
      <sub>2013年冬 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_cosmology/2009_winter_legacy_cosmology/cosmology_legacy.pdf"><img src="../figs/readme-covers/cosmology_legacy.png" width="170" alt="Cosmology legacy cover"></a><br>
      <strong>宇宙論</strong><br>
      <sub>2009年冬 レガシー版</sub>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4"><strong>補助</strong> · 量子 → 特殊 → 一般 → 統計 → 宇宙論</td>
  </tr>
  <tr>
    <td align="center">
      <a href="../supplemental_advanced_quantum/advanced_quantum_mechanics.pdf"><img src="../figs/readme-covers/advanced_quantum_mechanics.png" width="170" alt="Advanced Quantum Mechanics cover"></a><br>
      <strong>高等量子力学</strong><br>
      <sub>補助コース書籍</sub>
    </td>
    <td align="center">
      <a href="../supplemental_quantum_entanglement/quantum_entanglement_part_1.pdf"><img src="../figs/readme-covers/quantum_entanglement_part_1.png" width="170" alt="Quantum Entanglement Part 1 cover"></a><br>
      <strong>量子もつれ</strong><br>
      <sub>Part 1</sub>
    </td>
    <td align="center">
      <a href="../supplemental_quantum_entanglement/quantum_entanglement_part_3.pdf"><img src="../figs/readme-covers/quantum_entanglement_part_3.png" width="170" alt="Quantum Entanglement Part 3 cover"></a><br>
      <strong>量子もつれ</strong><br>
      <sub>Part 3</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../supplemental_particle_physics_1/particle_physics_1_basic_concepts.pdf"><img src="../figs/readme-covers/particle_physics_1_basic_concepts.png" width="170" alt="Particle Physics 1 cover"></a><br>
      <strong>粒子物理学 1</strong><br>
      <sub>基本概念</sub>
    </td>
    <td align="center">
      <a href="../supplemental_particle_physics_2/particle_physics_2_standard_model.pdf"><img src="../figs/readme-covers/particle_physics_2_standard_model.png" width="170" alt="Particle Physics 2 cover"></a><br>
      <strong>粒子物理学 2</strong><br>
      <sub>標準模型</sub>
    </td>
    <td align="center">
      <a href="../supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf"><img src="../figs/readme-covers/particle_physics_3_supersymmetry_and_grand_unification.png" width="170" alt="Particle Physics 3 cover"></a><br>
      <strong>粒子物理学 3</strong><br>
      <sub>超対称性と大統一</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf"><img src="../figs/readme-covers/topics_in_string_theory_first_page.png" width="170" alt="Topics in String Theory cover"></a><br>
      <strong>弦理論の諸話題</strong><br>
      <sub>宇宙論とブラックホール集</sub>
    </td>
    <td align="center">
      <a href="../supplemental_string_theory/string_theory_and_m_theory.pdf"><img src="../figs/readme-covers/string_theory_and_m_theory.png" width="170" alt="String Theory and M-Theory cover"></a><br>
      <strong>String Theory and M-Theory</strong><br>
      <sub>補助コース書籍</sub>
    </td>
    <td align="center">
      <a href="../supplemental_higgs_boson/demystifying_the_higgs_boson.pdf"><img src="../figs/readme-covers/demystifying_the_higgs_boson.png" width="170" alt="Demystifying the Higgs Boson cover"></a><br>
      <strong>ヒッグス粒子の謎を解く</strong><br>
      <sub>単独講義書籍</sub>
    </td>
  </tr>
</table>

## ✨ このリポジトリが提供するもの

- `core_*` および `supplemental_*` フォルダにある、既存の手動保守コース PDF と LaTeX 資料。
- 講義アーカイブのための対になった文字起こしレイヤー:
  - `.srt` 用の `subtitles/`
  - タイムスタンプ付き Markdown 文字起こし用の `markdown/`
- `generated_course_notes/` 内の transcript-to-TeX パイプライン。
- プレイリストのダウンロード、文字起こし、字幕からノートへの自動化を行う `Video2Book/` サブモジュール。
- `theoretical_minimum_companion_notes/` にあるインポート済み補助資料。
- `template/kaobook` と `template/tuftle` の再利用可能な LaTeX テンプレート。

英語版が正規の README です。翻訳版は `i18n/` にあり、英語版より更新が遅れる場合があります。

## 🎬 元となるプレイリスト

このリポジトリの主要な文字起こし・字幕アーカイブは、次の YouTube プレイリストから派生しています。

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

## 🗂️ リポジトリ構成

<table>
  <colgroup>
    <col style="width: 33%">
    <col style="width: 33%">
    <col style="width: 34%">
  </colgroup>
  <thead>
    <tr>
      <th>📚 レイヤー</th>
      <th>📍 主なパス</th>
      <th>🧾 内容</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>手動保守のコースフォルダ</td>
      <td><code>core_*</code>, <code>supplemental_*</code></td>
      <td>読者向けコースフォルダ、公開済み PDF、README、および選択された LaTeX ソース。</td>
    </tr>
    <tr>
      <td>字幕</td>
      <td><code>subtitles/</code></td>
      <td><code>.srt</code> 形式の講義字幕ファイル。</td>
    </tr>
    <tr>
      <td>Markdown 文字起こし</td>
      <td><code>markdown/</code></td>
      <td>閲覧、検索、ノート生成に使われるタイムスタンプ付き講義文字起こし。</td>
    </tr>
    <tr>
      <td>生成ノートのソース</td>
      <td><code>generated_course_notes/</code></td>
      <td>文字起こし由来の TeX 章、図、プロンプト、コースビルド資料。</td>
    </tr>
    <tr>
      <td>公開済み生成 PDF</td>
      <td><code>supplemental_*/</code></td>
      <td>完成した生成コースの正規公開成果物であり、コース固有の結合 PDF ファイル名に加えて <code>lecture_XX.pdf</code> ファイルを含みます。</td>
    </tr>
    <tr>
      <td>レガシービルド成果物</td>
      <td><code>core_cosmology/cosmology_ch10/artifacts/</code></td>
      <td>旧 chapter-10 cosmology サブプロジェクトのために保持されているビルド出力。</td>
    </tr>
    <tr>
      <td>補助ノート</td>
      <td><code>theoretical_minimum_companion_notes/</code></td>
      <td><code>weka511/tm</code> プロジェクト由来の、インポート済み TeX 補助ノート。</td>
    </tr>
    <tr>
      <td>テンプレートと共有資料</td>
      <td><code>template/</code>, <code>figs/</code>, <code>the_theoretical_minimum/</code>, <code>Video2Book/</code></td>
      <td>LaTeX テンプレート、共有ブランド資産、関連サブモジュールのチェックアウト、およびダウンロード／文字起こし自動化サブモジュール。</td>
    </tr>
  </tbody>
</table>

`subtitles/`、`markdown/`、`generated_course_notes/` の中では、資料はトラック（`core/` または `supplementary`）、次に主題、次にコース実施単位で整理されています。

生成ノートについては、各コースフォルダは通常次の内容を含みます。

- 講義ごとの TeX と講義ごとの PDF を置く `chapters/`
- 抽出した講義フレームと図版アセットを置く `figures/`
- コース全体をまとめた書籍用の `course.tex` と `course.pdf`

## 🧭 ルートのコースフォルダ

| 🏷️ グループ | 📂 フォルダ |
|---|---|
| コア | `core_classical_mechanics`, `core_quantum_mechanics`, `core_special_relativity`, `core_general_relativity`, `core_cosmology`, `core_statistical_mechanics` |
| 補助 | `supplemental_advanced_quantum`, `supplemental_cosmology_and_black_holes`, `supplemental_higgs_boson`, `supplemental_particle_physics_1`, `supplemental_particle_physics_2`, `supplemental_particle_physics_3`, `supplemental_quantum_entanglement`, `supplemental_relativity`, `supplemental_string_theory` |

## 🚀 リポジトリの使い方

### 📖 公開済みノートを読む

該当するコースフォルダ内の PDF を開いてください。例:

- `../core_classical_mechanics/2011_fall_theoretical_minimum/classical_mechanics_theoretical_minimum.pdf`
- `../core_classical_mechanics/2011_fall_modern_physics_stanford_partial/classical_mechanics_stanford_partial.pdf`
- `../core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf`
- `../core_quantum_mechanics/2012_winter_modern_physics_stanford/quantum_mechanics_modern_physics_stanford.pdf`
- `../core_special_relativity/2012_spring_theoretical_minimum/special_relativity_theoretical_minimum.pdf`
- `../core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf`
- `../core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf`
- `../core_cosmology/2009_winter_legacy_cosmology/cosmology_legacy.pdf`
- `../core_statistical_mechanics/lesson_1.pdf`
- `../supplemental_advanced_quantum/advanced_quantum_mechanics.pdf`
- `../supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf`
- `../supplemental_higgs_boson/demystifying_the_higgs_boson.pdf`
- `../supplemental_particle_physics_1/particle_physics_1_basic_concepts.pdf`
- `../supplemental_particle_physics_2/particle_physics_2_standard_model.pdf`
- `../supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf`
- `../supplemental_quantum_entanglement/quantum_entanglement_part_1.pdf`
- `../supplemental_quantum_entanglement/quantum_entanglement_part_3.pdf`
- `../supplemental_string_theory/string_theory_and_m_theory.pdf`

### 📝 文字起こしを直接読む

次を使います。

- 字幕風の閲覧とタイムスタンプ忠実性のための `../subtitles/`
- テキストレビュー、検索、ノート生成のための `../markdown/`

### ⬇️ 元プレイリストを更新する

`Video2Book` サブモジュールへ委譲する親ラッパーを使用します。

```bash
./scripts/download_susskind_playlist.sh
```

### 🎙️ 文字起こしキューを実行する

`Video2Book` サブモジュールへ委譲する親ラッパーを使用します。

```bash
./scripts/start_transcription_tmux.sh
./scripts/start_transcription_monitor_tmux.sh
```

### 🧪 文字起こし由来ノートに取り組む

生成ノートのワークスペースは次の場所にあります。

- `../generated_course_notes/`

各コース実施単位の中では:

- `chapters/` に講義ごとのフォルダが入ります
- 各講義フォルダには章 TeX とその講義 PDF が入ります
- `course.pdf` はその実施単位のコース全体を結合した PDF です

ノートキュレーターは `Video2Book` サブモジュールへ委譲する親ラッパー経由で実行します。

```bash
./scripts/start_course_notes_tmux.sh
./scripts/start_course_notes_monitor_tmux.sh
```

### 📘 コンパクトなポケット判 PDF を書き出す

完成した生成コース LaTeX から、手持ちしやすい 6x9 インチ版を生成します。

```bash
./scripts/export_course_pocket_pdfs.sh
./scripts/export_course_pocket_pdfs.sh --size a5 --suffix a5
```

出力はデフォルトで `../all_notes/pocket_books/<course>_pocket.pdf` に書き込まれます（正規ファイル名、`--suffix` による任意サフィックス指定も可能）。

### 📚 インポート済み補助ノートに取り組む

```bash
./theoretical_minimum_companion_notes/build_all.sh
```

## 🤝 コラボレーション

Leonard Susskind 関連の学習資料について、数学的品質、明瞭さ、保存性を改善する貢献を歓迎します。

優先分野は次のとおりです。

- 文字起こしのクリーンアップ
  - 話者の割り当て修正
  - タイムスタンプの修復
  - 物理用語、名前、記法の修正
- TeX 改善
  - 文字起こしをより洗練された数学的記述へ変換
  - 構造、組版、相互参照の改善
  - 生成章を長期利用可能なコースノートへ磨き上げる
- 図と方程式の整備
  - 抽出した講義フレームの検証
  - TikZ による図の描き直し
  - 黒板の方程式を信頼できる LaTeX に変換
- より広い物理アーカイブ作業
  - *Theoretical Minimum* 補助資料の改善
  - 関連する Susskind の講義、書籍、ノート群の接続
  - この物理教育資産を責任をもって普及・保存する支援

貢献では、焦点の絞られたコミットを使い、変更したフォルダ、文字起こし、またはコース実施単位を正確に明示してください。

## 🙏 謝辞

- Leonard Susskind に元の講義コンテンツを提供いただいたことへの感謝。
- リポジトリのキュレーションと公開ツール群: [LazyingArt LLC](https://lazying.art)
- `../theoretical_minimum_companion_notes/` にインポートされた補助ノートリポジトリの提供者である Simon Crase への感謝。
- 補助ノートのソースリポジトリ: <https://github.com/weka511/tm>
- 既存の参照ノートソース:
  - <https://www.lapasserelle.com/general_relativity/>
  - <https://www.lapasserelle.com/cosmology/>
  - <https://www.lapasserelle.com/statistical_mechanics/>
- 古い La Passerelle 由来 PDF セットの出典メモ:
  - [`../references/lapasserelle_susskind_pdf_provenance.md`](../references/lapasserelle_susskind_pdf_provenance.md)

## ❤️ 支援

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## ライセンス

このリポジトリは GNU General Public License v3.0 の下でライセンスされています。[LICENSE](../LICENSE) を参照してください。
