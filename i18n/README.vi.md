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

## Tổng quan
Kho lưu trữ này ưu tiên nội dung, tập trung lưu trữ tài liệu ghi chú bài giảng liên quan đến các khóa học của Giáo sư Leonard Susskind.

> Ghi chú bài giảng của Giáo sư Leonard Susskind. Nếu nội dung này vi phạm bản quyền, vui lòng liên hệ tôi để xóa kho lưu trữ này. Giáo sư Susskind không chịu trách nhiệm về lỗi hay thông tin sai lệch trong các ghi chú, và tôi cũng vậy.

### Mục tiêu chính
- Lưu trữ ghi chú khóa học và tiến độ trong cùng một nơi.
- Duy trì khả năng theo dõi tiến độ bản nháp/ghi chú trên cả các tuyến học cốt lõi và bổ sung.
- Cung cấp tài liệu nguồn (PDF, TeX, BibTeX, mẫu) để tiếp tục biên soạn.

## Tính năng
- Theo dõi các khóa học cốt lõi và tài liệu tham chiếu.
- Theo dõi tiến độ các khóa học bổ sung.
- Có sẵn PDF bài học cho một số tuyến học cốt lõi.
- Tài liệu nguồn LaTeX trong một số tuyến học.
- Mẫu LaTeX tái sử dụng trong `template/tuftle` và `template/kaobook`.
- Tài nguyên hình ảnh của kho trong `figs/`.
- Bộ README đa ngôn ngữ trong `i18n/`.

## Ảnh chụp nhanh
| Khu vực | Nội dung có sẵn |
|---|---|
| 📝 Ghi chú | Nhiều bộ ghi chú khóa học có theo dõi tiến độ |
| 🧾 Nguồn | Nguồn TeX/BibTeX trong một số dự án con |
| 🧱 Mẫu | `template/tuftle` và `template/kaobook` |
| 🎨 Nhận diện | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | Các biến thể ngôn ngữ `i18n/README.*.md` |

## Mục lục
- [Tổng quan](#tổng-quan)
- [Tính năng](#tính-năng)
- [Ảnh chụp nhanh](#ảnh-chụp-nhanh)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Yêu cầu trước](#yêu-cầu-trước)
- [Cài đặt](#cài-đặt)
- [Sử dụng](#sử-dụng)
- [Cấu hình](#cấu-hình)
- [Ví dụ](#ví-dụ)
- [Ghi chú phát triển](#ghi-chú-phát-triển)
- [Tiến độ khóa học chuẩn (được giữ nguyên và tái tổ chức)](#tiến-độ-khóa-học-chuẩn-được-giữ-nguyên-và-tái-tổ-chức)
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
Dành cho mục đích chỉ đọc:
- Trình đọc PDF.

Dành cho chỉnh sửa/biên dịch tài liệu TeX:
- Một bản phân phối LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` hoặc `biber` tùy theo từng dự án con.
- `makeindex` cho các mẫu có dùng chỉ mục.

Ghi chú giả định:
- Không có hệ thống build chung ở cấp thư mục gốc (`Makefile`, `package.json`, `pyproject.toml`) trong kho này.

## Cài đặt
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

Nếu kho này được fork hoặc mirror, hãy thay `<your-user>` bằng tài khoản phù hợp.

Không cần bước cài đặt gói cho nhu cầu cơ bản (đọc các ghi chú có sẵn).

## Sử dụng
### 1) Đọc các ghi chú hiện có
Mở các tệp PDF trong thư mục liên quan, ví dụ:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Làm việc với tài liệu LaTeX
- Chỉnh sửa các tệp `.tex` và `.bib` trong thư mục khóa học/mẫu mục tiêu.
- Biên dịch bằng chuỗi công cụ phù hợp với thư mục đó.
- Ưu tiên chạy lệnh build từ bên trong thư mục dự án cục bộ để các đường dẫn tương đối được phân giải chính xác.

### 3) Điều hướng theo README của từng tuyến học
Mỗi tuyến học chính có `README.md` riêng để quản lý ghi chú theo phạm vi và ngữ cảnh tiến độ.

## Cấu hình
Không có tệp cấu hình toàn cục.

Cấu hình nằm cục bộ trong từng dự án TeX (lớp tài liệu, backend thư mục tài liệu tham khảo, tệp style, đường dẫn hình ảnh), ví dụ:
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
`cosmology_ch10.tex` dùng `\bibliography{ref}` (quy trình kiểu BibTeX):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Ví dụ C: Build một chương dựa trên Tufte (`supplemental_particle_physics_1/ch1`)
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ví dụ D: Build một chương dựa trên Tufte (`supplemental_advanced_quantum/ch1`)
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ví dụ E: Xem PDF chương đã được tạo
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Ghi chú phát triển
- Đây chủ yếu là kho tài liệu/ghi chú, không phải codebase ứng dụng.
- Một số thư mục bao gồm các tệp phát sinh từ TeX (`.aux`, `.log`, `.toc`, `.bbl`, v.v.) đã được commit trong kho.
- Lệnh build có thể khác nhau theo từng thư mục con; hãy theo quy ước `.tex` tại chỗ.
- Các tệp `README.md` theo từng tuyến học tồn tại trong thư mục core/supplemental và cần giữ đồng bộ với phát biểu tiến độ ở README gốc.
- `i18n/` đã tồn tại và được dùng cho các biến thể README đa ngôn ngữ.
- README gốc được xem là chuẩn; khi cập nhật cần đồng bộ các bản đa ngôn ngữ theo README này.

## Tiến độ khóa học chuẩn (được giữ nguyên và tái tổ chức)

### Các khóa học cốt lõi

#### Cơ học cổ điển
Giáo trình của khóa học này [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) đã được xuất bản. Bạn có thể mua trên Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Cơ học lượng tử
Giáo trình của khóa học này [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) đã được xuất bản. Bạn có thể mua trên Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Thuyết tương đối hẹp và điện động lực học
Giáo trình của khóa học này [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) đã được xuất bản. Bạn có thể mua trên Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Bảng tiến độ cốt lõi
| Course | Draft Progress | Notes Progress | Notes/Reference |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### Các khóa học bổ sung
| Course | Draft Progress | Notes Progress |
|---|---:|---:|
| Advanced Quantum Mechanics | 0/10 | 0/10 |
| Higgs Boson | 0/1 | 0/1 |
| Quantum Entanglement | 0/9 | 0/9 |
| Relativity | 0/9 | 0/9 |
| Particle Physics 1: Basic Concepts | 6/10 | 0/10 |
| Particle Physics 2: Standard Model | 0/10 | 0/10 |
| Particle Physics 3: Supersymmetry and Grand Unification | 0/10 | 0/10 |
| String Theory | 0/11 | 10/10 |
| Cosmology and Black Holes | 0/8 | 0/10 |

### Ghi chú về tính toàn vẹn tiến độ
- Các bảng tiến độ ở trên được giữ nguyên từ nội dung README chuẩn.
- Các tệp trong kho bao gồm cả tuyến học đã hoàn thiện và tuyến học còn ở dạng placeholder; nếu có điểm không nhất quán giữa mục trong bảng và trạng thái thư mục, hãy coi bảng là ý định đã được ghi nhận và cập nhật cả hai cùng nhau trong các lần chỉnh sửa sau.

## Khắc phục sự cố
| Vấn đề | Cách xử lý |
|---|---|
| `pdflatex: command not found` | Cài đặt một bản phân phối LaTeX và đảm bảo binary nằm trong `PATH`. |
| Tài liệu tham khảo/chỉ mục không hiển thị | Chạy backend cần thiết (`bibtex` hoặc `biber`) và `makeindex` nếu có dùng, sau đó chạy lại `pdflatex`. |
| Lỗi thiếu style/class file | Build từ đúng thư mục dự án để các đường dẫn tương đối tới tài nguyên cục bộ được phân giải chính xác. |
| Kết quả build khác nhau giữa các môi trường | Kho này chứa tài liệu được tạo trong các môi trường khác nhau; hãy đồng bộ phiên bản package khi có thể. |
| Liên kết đa ngôn ngữ lỗi thời hoặc thiếu README ngôn ngữ | Đảm bảo dòng chọn ngôn ngữ ở đầu tệp và các tệp dưới `i18n/` luôn đồng bộ. |
| Liên kết markdown GitHub sai sau khi đổi tên thư mục | Kiểm tra lại liên kết ngôn ngữ gốc và mọi tham chiếu `i18n/README.*.md` trong một lượt. |

## Lộ trình
- Tiếp tục các tuyến học bổ sung với nội dung chương thực tế và tệp nguồn.
- Cải thiện tính nhất quán của các tệp README theo từng khóa học.
- Mở rộng và duy trì các README đa ngôn ngữ trong `i18n/`, đồng thời giữ bộ chọn ngôn ngữ luôn đồng bộ.
- Bổ sung mục hướng dẫn build ở cấp kho cho từng dự án con có nguồn TeX.
- Bổ sung đoạn lệnh biên dịch theo từng tuyến học khi có khác biệt toolchain cục bộ.
- Thêm tự động hóa tối thiểu để kiểm tra tính toàn vẹn liên kết README/i18n.

## Đóng góp
Bạn có thể đóng góp cho dự án này bằng cách fork và gửi pull request.

Phạm vi đóng góp gợi ý:
- Thêm mới hoặc cải thiện ghi chú chương và tài liệu tham chiếu.
- Nâng cao chất lượng nguồn TeX và hướng dẫn build có thể tái lập.
- Giữ đồng bộ phát biểu tiến độ giữa README gốc và README theo từng tuyến học.
- Duy trì tính tương đương đa ngôn ngữ trong `i18n/`.

Khuyến nghị cho pull request:
- Nêu rõ chính xác thư mục tuyến học đã thay đổi.
- Kèm các lệnh biên dịch TeX đã dùng (nếu có chỉnh sửa tệp nguồn).
- Cập nhật các bảng tiến độ liên quan khi trạng thái chương thay đổi.
- Cập nhật các README trong `i18n/` sau khi README tiếng Anh chuẩn thay đổi.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Lời cảm ơn
- Giáo sư Leonard Susskind vì nội dung bài giảng gốc.
- Nguồn ghi chú được tham chiếu hiện có: https://www.lapasserelle.com/general_relativity/
- Nguồn ghi chú được tham chiếu hiện có: https://www.lapasserelle.com/cosmology/
- Nguồn ghi chú được tham chiếu hiện có: https://www.lapasserelle.com/statistical_mechanics/

## Giấy phép
Kho lưu trữ này được cấp phép theo GNU General Public License v3.0. Xem [LICENSE](../LICENSE).
