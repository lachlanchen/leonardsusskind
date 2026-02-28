[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Kho Lưu Trữ Ghi Chú Bài Giảng Leonard Susskind


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 Tổng quan
Kho lưu trữ này là một kho tư liệu ưu tiên nội dung, lưu trữ các tài liệu ghi chú bài giảng liên quan đến các khóa học của Giáo sư Leonard Susskind.

Các ghi chú bài giảng của Giáo sư Leonard Susskind. Nếu nội dung này vi phạm bất kỳ bản quyền nào, vui lòng liên hệ để tôi xóa kho lưu trữ này. Giáo sư Susskind không chịu trách nhiệm cho lỗi hoặc thông tin sai lệch trong các ghi chú này, và tôi cũng vậy.

### Mục tiêu chính
- Lưu ghi chú khóa học và tiến độ ở cùng một nơi.
- Duy trì khả năng hiển thị tiến độ bản nháp/ghi chú trên cả các lộ trình cốt lõi và bổ trợ.
- Cung cấp tài liệu nguồn (PDF, TeX, BibTeX, template) để tiếp tục biên soạn.

## ✨ Tính năng
- Theo dõi và tham chiếu các khóa học cốt lõi.
- Theo dõi tiến độ các khóa học bổ trợ.
- Có sẵn PDF bài học cho một số lộ trình cốt lõi.
- Có tài liệu nguồn LaTeX ở một số lộ trình đã chọn.
- Template LaTeX có thể tái sử dụng trong `template/tuftle` và `template/kaobook`.
- Hình ảnh của kho lưu trữ trong `figs/`.

## 📌 Ảnh chụp nhanh
| Khu vực | Nội dung có sẵn |
|---|---|
| 📚 Ghi chú | Nhiều bộ ghi chú khóa học, có theo dõi tiến độ |
| 🧪 Mã nguồn | Mã nguồn TeX/BibTeX trong một số dự án con |
| 🧰 Template | `template/tuftle` và `template/kaobook` |
| 🌐 i18n | Thư mục `i18n/` đã tồn tại (hiện đang trống) |

## 🗂️ Cấu trúc dự án
```text
leonardsusskind/
├── README.md
├── LICENSE
├── tuftle_book_guide.pdf
├── figs/
│   ├── banner.(png|svg)
│   ├── logo.(png|svg)
│   └── logo-w-text.(png|svg)
├── i18n/                      # exists; currently empty
├── core_classical/
├── core_quantum/
├── core_special_relativity/
├── core_general_relativity/   # lesson_1.pdf ... lesson_10.pdf
├── core_cosmology/            # lesson_1.pdf ... lesson_9.pdf + cosmology_ch10/
├── core_statistical_mechanics/# lesson_1.pdf ... lesson_11.pdf
├── supplemental_advanced_quantum/
├── supplemental_cosmology_and_black_holes/
├── supplemental_higgs_boson/
├── supplemental_particle_physics_1/
├── supplemental_particle_physics_2/
├── supplemental_particle_physics_3/
├── supplemental_quantum_entanglement/
├── supplemental_relativity/
├── supplemental_string_theory/
└── template/
   ├── tuftle/
   └── kaobook/
```

## 🧩 Điều kiện tiên quyết
Chỉ để đọc:
- Trình đọc PDF.

Để chỉnh sửa/biên dịch tài liệu TeX:
- Một bản phân phối LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` hoặc `biber` tùy theo từng dự án con.
- `makeindex` cho các template có dùng đánh chỉ mục.

Lưu ý giả định:
- Không có hệ thống build duy nhất ở cấp thư mục gốc (`Makefile`, `package.json`, `pyproject.toml`) trong kho lưu trữ này.

## 🚀 Cài đặt
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

Không cần bước cài đặt package cho mục đích sử dụng cơ bản (đọc các ghi chú hiện có).

## 🛠️ Cách sử dụng
### 1) Đọc các ghi chú hiện có
- Mở các file PDF trong những thư mục liên quan, ví dụ:
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) Làm việc với tài liệu LaTeX
- Chỉnh sửa file `.tex` và `.bib` trong thư mục khóa học/template mục tiêu.
- Biên dịch bằng chuỗi công cụ mà thư mục đó yêu cầu.

## ⚙️ Cấu hình
Không có file cấu hình toàn cục.

Cấu hình nằm cục bộ trong từng dự án TeX (document class, backend thư mục tham khảo, file style, đường dẫn hình ảnh), ví dụ:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 Ví dụ
### Ví dụ A: Build `template/kaobook`
`template/kaobook/main.tex` mô tả chuỗi biên dịch này:

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

### Ví dụ C: Xem file PDF chương đã tạo
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 Ghi chú phát triển
- Đây chủ yếu là kho tài liệu/ghi chú, không phải codebase ứng dụng.
- Một số thư mục có chứa các artifact TeX đã tạo (`.aux`, `.log`, `.toc`, `.bbl`, v.v.) được commit trực tiếp trong repo.
- Lệnh build có thể khác nhau theo từng thư mục con; hãy làm theo quy ước `.tex` cục bộ.
- `i18n/` đã tồn tại và được dành cho các biến thể README đa ngôn ngữ.

## 📚 Tiến độ khóa học chuẩn (Được bảo toàn và sắp xếp lại)

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

### Các khóa học bổ trợ
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

## 🧯 Khắc phục sự cố
- `pdflatex: command not found`
  - Cài đặt một bản phân phối LaTeX và đảm bảo các binary nằm trong `PATH`.
- Thư mục tham khảo/chỉ mục không hiển thị
  - Chạy backend bắt buộc (`bibtex` hoặc `biber`) và `makeindex` nếu có dùng, sau đó chạy lại `pdflatex`.
- Lỗi thiếu file style/class
  - Build từ đúng thư mục dự án để các đường dẫn tương đối đến tài nguyên cục bộ được resolve chính xác.
- Kết quả build khác nhau giữa các môi trường
  - Kho lưu trữ này chứa tài liệu được tạo ở các môi trường khác nhau; hãy đồng bộ phiên bản package khi có thể.

## 🗺️ Lộ trình
- Tiếp tục các lộ trình bổ trợ với nội dung chương thực tế và file nguồn.
- Cải thiện tính nhất quán của README theo từng khóa học.
- Thêm các file README đa ngôn ngữ dưới `i18n/` và giữ bộ chọn ngôn ngữ luôn đồng bộ.
- Thêm phần hướng dẫn build ở cấp kho cho từng dự án con có mã nguồn TeX.

## ❤️ Đóng góp hoặc ủng hộ
Bạn có thể đóng góp cho dự án này bằng cách fork dự án và gửi pull request. Nếu dự án này giúp bạn tiết kiệm thời gian phát triển, bạn có thể mời tôi một ly cà phê :)

## 🙏 Lời cảm ơn
- Giáo sư Leonard Susskind vì nội dung bài giảng gốc.
- Các nguồn ghi chú đã tham chiếu:
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 Giấy phép
Kho lưu trữ này được cấp phép theo GNU General Public License v3.0. Xem [LICENSE](LICENSE).
