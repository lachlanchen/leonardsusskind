[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Kho Lưu Trữ Ghi Chú Bài Giảng Leonard Susskind

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![Core Tracks](https://img.shields.io/badge/core_tracks-6-1f6feb)
![Supplemental Tracks](https://img.shields.io/badge/supplemental_tracks-9-9a6700)
![i18n](https://img.shields.io/badge/i18n-10%20translations%20%2B%20English-orange)
![Stars](https://img.shields.io/github/stars/lachlanchen/leonardsusskind?style=flat-square&logo=github&label=stars&color=22c55e)
![Forks](https://img.shields.io/github/forks/lachlanchen/leonardsusskind?style=flat-square&logo=github&label=forks&color=3b82f6)
![Last Commit](https://img.shields.io/github/last-commit/lachlanchen/leonardsusskind?style=flat-square&color=8b5cf6)

> 🎓 Một kho đa ngôn ngữ lưu giữ tài liệu ghi chú bài giảng của Leonard Susskind, giữ nguyên cả PDF đã được chỉnh sửa và nguồn LaTeX có thể chỉnh sửa để học tập, tái sử dụng và tra cứu.

## Tổng quan
Kho này là một kho lưu trữ ưu tiên nội dung gồm tài liệu ghi chú bài giảng của hệ sinh thái giảng dạy của Giáo sư Leonard Susskind.

> Ghi chú bài giảng của Giáo sư Leonard Susskind. Nếu điều này vi phạm bản quyền, vui lòng liên hệ với tôi để xoá kho lưu trữ này. Giáo sư Susskind không chịu trách nhiệm về lỗi hoặc thông tin sai trong các ghi chú, tôi cũng không.

Kho này kết hợp ba lớp tại cùng một nơi:

- Theo dõi các nhánh ghi chú có cấu trúc theo tiến trình môn học.
- Tài liệu đã xuất bản (`.pdf`) để đọc và chia sẻ.
- Tệp nguồn (`.tex`, `.bib`, mẫu) cho người duy trì và mở rộng kho.

### Mục tiêu chính
- Giữ notes theo khoá học và tiến độ ở cùng một chỗ.
- Bảo toàn khả năng nhìn thấy tiến độ bản nháp/ghi chú ở cả các nhánh cốt lõi và bổ sung.
- Cung cấp tài liệu nguồn (PDF, TeX, BibTeX, mẫu) để tiếp tục biên soạn.

## Tính năng
- Theo dõi và tra cứu các khóa học cốt lõi.
- Theo dõi tiến độ khóa học bổ sung.
- Các PDF bài giảng hiện có cho một số nhánh cốt lõi.
- Nguồn LaTeX trong một số nhánh đã chọn.
- Mẫu LaTeX tái sử dụng tại `template/tuftle` và `template/kaobook`.
- Tài nguyên trực quan kho trong `figs/`.
- Tập README đa ngôn ngữ trong `i18n/`.

## Bức tranh nhanh
| Khu vực | Nội dung có sẵn |
|---|---|
| 📝 Ghi chú | Nhiều bộ ghi chú theo khóa học kèm theo theo dõi tiến độ |
| 🧾 Nguồn | Nguồn TeX/BibTeX trong các dự án con đã chọn |
| 🧱 Mẫu | `template/tuftle` và `template/kaobook` |
| 🎨 Nhận diện | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` các biến thể ngôn ngữ |

## Mục lục
- [Tổng quan](#tổng-quan)
- [Tính năng](#tính-năng)
- [Bức tranh nhanh](#bức-tranh-nhanh)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Yêu cầu trước](#yêu-cầu-trước)
- [Cài đặt](#cài-đặt)
- [Sử dụng](#sử-dụng)
- [Cấu hình](#cấu-hình)
- [Ví dụ](#ví-dụ)
- [Ghi chú phát triển](#ghi-chú-phát-triển)
- [Tiến độ khóa học chuẩn (được bảo toàn và tái tổ chức)](#tiến-độ-khóa-học-chuẩn-được-bảo-quản-và-tái-tổ-chức)
- [Khắc phục sự cố](#khắc-phục-sự-cố)
- [Lộ trình](#lộ-trình)
- [Đóng góp](#đóng-góp)
- [❤️ Support](#-support)
- [Lời cảm ơn](#lời-cảm-ơn)
- [Giấy phép](#giấy-phép)

## Cấu trúc dự án
```text
leonardsusskind/
├── README.md
├── LICENSE
├── tuftle_book_guide.pdf
├── figs/
│   ├── banner.(png|svg)
│   ├── logo.(png|svg)
│   └── logo-w-text.(png|svg)
├── i18n/
│   ├── README.ar.md
│   ├── README.de.md
│   ├── README.es.md
│   ├── README.fr.md
│   ├── README.ja.md
│   ├── README.ko.md
│   ├── README.ru.md
│   ├── README.vi.md
│   ├── README.zh-Hans.md
│   └── README.zh-Hant.md
├── core_classical/
│   └── README.md
├── core_quantum/
│   └── README.md
├── core_special_relativity/
│   └── README.md
├── core_general_relativity/
│   ├── README.md
│   └── lesson_1.pdf ... lesson_10.pdf
├── core_cosmology/
│   ├── README.md
│   ├── lesson_1.pdf ... lesson_9.pdf
│   └── cosmology_ch10/
│       ├── cosmology_ch10.tex
│       └── ref.bib
├── core_statistical_mechanics/
│   ├── README.md
│   └── lesson_1.pdf ... lesson_11.pdf
├── supplemental_advanced_quantum/
│   ├── README.md
│   └── ch1/
│       ├── main.tex
│       ├── book_1_template.tex
│       └── bibliography.bib
├── supplemental_cosmology_and_black_holes/
│   └── README.md
├── supplemental_higgs_boson/
│   └── README.md
├── supplemental_particle_physics_1/
│   ├── README.md
│   ├── ch1/
│   │   ├── main.tex
│   │   ├── book_1_template.tex
│   │   └── bibliography.bib
│   └── lecture transcript .txt files
├── supplemental_particle_physics_2/
│   ├── README.md
│   ├── NumberTheory.pdf
│   └── lecture transcript .txt files
├── supplemental_particle_physics_3/
│   └── README.md
├── supplemental_quantum_entanglement/
│   └── README.md
├── supplemental_relativity/
│   └── README.md
├── supplemental_string_theory/
│   └── README.md
└── template/
    ├── kaobook/
    │   ├── main.tex
    │   ├── structure.tex
    │   └── bibliography.bib
    └── tuftle/
        ├── main.tex
        ├── book_1_template.tex
        └── bibliography.bib
```

## Yêu cầu trước
Để đọc:
- Một trình đọc PDF (trên hệ thống hoặc ứng dụng).

Để chỉnh sửa/biên dịch tài liệu TeX:
- Một bản phân phối LaTeX (`TeX Live` / `MiKTeX`).
- `pdflatex`.
- `bibtex` hoặc `biber` tùy theo dự án con.
- `makeindex` cho các dự án có mục lục chỉ mục.

Ghi chú giả định:
- Không có hệ thống build gốc duy nhất (`Makefile`, `package.json`, `pyproject.toml`) hiển thị trong kho này.
- Các quy trình build dự kiến chạy từ từng thư mục dự án con.

## Cài đặt
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

Kho này theo nguyên tắc content-first. Nếu được mirror hoặc fork, hãy thay URL remote bằng bản sao của bạn.

Không cần cài đặt gói toàn cục để đọc các ghi chú hiện có.

## Sử dụng
### 1) Đọc ghi chú hiện có
Mở các tệp PDF trong thư mục tương ứng, ví dụ:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Tạo hoặc mở rộng tài liệu LaTeX
- Chỉnh sửa các tệp `.tex` và `.bib` trong thư mục khóa học/mẫu mục tiêu.
- Biên dịch theo chuỗi công cụ được chỉ định bởi thư mục đó.
- Build tại chỗ để các asset tương đối và tệp style được giải quyết đúng.

### 3) Điều hướng theo điểm vào của từng nhánh học
Mỗi nhánh chính có `README.md` riêng với ghi chú phạm vi hẹp, tài liệu tham khảo và tiến độ.

## Cấu hình
Không có tệp cấu hình toàn cục.

Cấu hình nằm cục bộ trong từng dự án TeX. Các cấu hình điển hình được nhúng trong tài liệu nguồn, gồm:
- Lớp tài liệu và cài đặt package trong `template/kaobook/main.tex`
- Kiến trúc/style có thể tái sử dụng trong `template/kaobook/`
- Backend bibliographic và kiểu trích dẫn trong cặp `main.tex`/`ref.bib` cục bộ
- Đường dẫn include cho hình ảnh và tài nguyên theo chương trong từng dự án

Các điểm cấu hình cục bộ tiêu biểu:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Ví dụ
### Ví dụ A: Build `template/kaobook`
`template/kaobook/main.tex` mô tả chuỗi biên dịch sau:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Ví dụ B: Build `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` sử dụng luồng làm việc kiểu BibTeX:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Ví dụ C: Build `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ví dụ D: Build `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ví dụ E: Xem đầu ra tại máy local
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Ghi chú phát triển
- Đây chủ yếu là kho tài liệu/ghi chú, không phải mã ứng dụng.
- Một số thư mục có chứa các artifact TeX sinh ra (`.aux`, `.log`, `.toc`, `.bbl`, v.v.) đã được commit trong repo.
- Lệnh build có thể khác nhau theo từng thư mục con; hãy tuân theo quy ước `.tex` cục bộ.
- Các tệp `README.md` theo từng khóa học tồn tại trong toàn bộ core và supplemental, và nên được giữ đồng bộ với các tuyên bố tiến độ cấp root.
- `i18n/` đang được sử dụng cho các biến thể README đa ngôn ngữ.
- README gốc được xem là chuẩn; các tệp địa phương hóa nên bám sát khi cập nhật.

## Tiến độ khóa học chuẩn (được bảo toàn và tái tổ chức)

### Các khóa học cốt lõi

#### Cơ học cổ điển
Sách giáo khoa của khóa học này, [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681), đã được xuất bản. Bạn có thể mua tại Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Cơ học lượng tử
Sách giáo khoa của khóa học này, [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903), đã được xuất bản. Bạn có thể mua tại Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Tương đối hẹp và Điện động lực học
Sách giáo khoa của khóa học này, [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065), đã được xuất bản. Bạn có thể mua tại Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Bảng tiến độ cốt lõi
| Khóa học | Tiến độ bản nháp | Tiến độ ghi chú | Ghi chú/Tài liệu tham khảo |
|---|---:|---:|---|
| Vật lý tương đối tổng quát | 10/10 | 10/10 | Ghi chú bài giảng đã được lấy từ https://www.lapasserelle.com/general_relativity/ . |
| Vũ trụ học | 10/10 | 9/10 | Ghi chú bài giảng, từ chương 1 đến 9, đã được lấy từ https://www.lapasserelle.com/cosmology/ . Chương 10 đang được xử lý. |
| Cơ học thống kê | 11/11 | 10/10 | Ghi chú bài giảng đã được lấy từ https://www.lapasserelle.com/statistical_mechanics/. |

### Các khóa học bổ sung
| Khóa học | Tiến độ bản nháp | Tiến độ ghi chú |
|---|---:|---:|
| Cơ học lượng tử nâng cao | 0/10 | 0/10 |
| Higgs Boson | 0/1 | 0/1 |
| Tương tác lượng tử và vướng víu lượng tử | 0/9 | 0/9 |
| Tương đối | 0/9 | 0/9 |
| Vật lý hạt 1: Khái niệm cơ bản | 6/10 | 0/10 |
| Vật lý hạt 2: Mô hình chuẩn | 0/10 | 0/10 |
| Vật lý hạt 3: Siêu đối xứng và Thống nhất Đại hóa | 0/10 | 0/10 |
| Lý thuyết dây | 0/11 | 10/10 |
| Vũ trụ học và lỗ đen | 0/8 | 0/10 |

### Ghi chú về tính toàn vẹn tiến độ
- Các bảng tiến độ ở trên được giữ nguyên từ văn bản README chuẩn.
- Tệp repository chứa cả nhánh đã trưởng thành và các nhánh mẫu; nếu mục trong bảng và trạng thái thư mục thực tế không khớp, hãy coi bảng là ý định đã được ghi lại và cập nhật đồng thời cả hai trong các lần chỉnh sửa kế tiếp.

## Khắc phục sự cố
| Vấn đề | Cách xử lý |
|---|---|
| `pdflatex: command not found` | Cài đặt một distribution LaTeX và chắc chắn các binary có trong `PATH`. |
| Mục lục/bibliography không xuất hiện | Chạy backend bắt buộc (`bibtex` hoặc `biber`) và `makeindex` nếu dùng, sau đó chạy lại `pdflatex`. |
| Thiếu lỗi style/class file | Hãy build từ đúng thư mục dự án để các đường dẫn tương đối tới tài nguyên cục bộ được giải quyết đúng. |
| Kết quả build khác nhau giữa môi trường | Repo này chứa tài liệu được tạo trong các môi trường khác nhau; hiệu chỉnh phiên bản gói khi có thể. |
| Liên kết đa ngôn ngữ lỗi thời hoặc thiếu README ngôn ngữ | Đảm bảo dòng chuyển đổi ngôn ngữ đầu file và các file trong `i18n/` được đồng bộ. |
| Mismatch liên kết Markdown GitHub sau khi đổi tên thư mục | Kiểm tra lại liên kết ngôn ngữ ở root và toàn bộ tham chiếu `i18n/README.*.md` trong một lượt. |

## Lộ trình
- Tiếp tục phát triển các khóa học bổ sung với nội dung chương thực tế và tệp nguồn.
- Nâng cao tính nhất quán của các README theo từng khóa học.
- Mở rộng và duy trì README đa ngôn ngữ trong `i18n/` và giữ bộ chọn ngôn ngữ đồng bộ.
- Thêm một phần hướng dẫn build cấp repository cho từng dự án con có nguồn TeX.
- Thêm các đoạn compile-specific theo sự khác biệt công cụ cục bộ từng nhánh.
- Thêm tự động hóa tối thiểu để xác thực tính toàn vẹn liên kết README/i18n.

## Đóng góp
Bạn có thể đóng góp cho dự án này bằng cách fork và gửi pull request.

Phạm vi đóng góp đề xuất:
- Thêm hoặc cải thiện ghi chú chương và tham chiếu.
- Nâng cao chất lượng source LaTeX và hướng dẫn biên dịch tái lập.
- Giữ cho các tuyên bố tiến độ root README và README theo từng khóa học luôn đồng bộ.
- Duy trì tính tương đương ngôn ngữ của các README trong `i18n/`.

Khuyến nghị quy trình pull request:
- Ghi rõ chính xác thư mục khóa học đã thay đổi.
- Đưa vào các lệnh biên dịch TeX đã dùng (nếu đã chỉnh sửa source file).
- Cập nhật các bảng tiến độ liên quan khi trạng thái chương thay đổi.
- Cập nhật `i18n/` sau khi README tiếng Anh chuẩn thay đổi.

## Lời cảm ơn
- Giáo sư Leonard Susskind cho nội dung bài giảng gốc.
- Nguồn ghi chú tham chiếu hiện có: https://www.lapasserelle.com/general_relativity/
- Nguồn ghi chú tham chiếu hiện có: https://www.lapasserelle.com/cosmology/
- Nguồn ghi chú tham chiếu hiện có: https://www.lapasserelle.com/statistical_mechanics/

## Giấy phép
Kho này được cấp phép theo GNU General Public License v3.0. Xem [LICENSE](../LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
