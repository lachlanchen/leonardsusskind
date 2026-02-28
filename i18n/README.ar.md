[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# مستودع ملاحظات محاضرات ليونارد ساسكيند


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 نظرة عامة
هذا المستودع أرشيف يركز على المحتوى لمواد ملاحظات المحاضرات المرتبطة بمقررات البروفيسور Leonard Susskind.

ملاحظات محاضرات البروفيسور Leonard Susskind. إذا كان هذا ينتهك أي حقوق نشر، يرجى التواصل معي لحذف هذا المستودع. لا يتحمّل البروفيسور Susskind أي مسؤولية عن الأخطاء أو المعلومات غير الدقيقة في الملاحظات، وكذلك أنا.

### الأهداف الأساسية
- إبقاء ملاحظات المقررات وحالة التقدم في مكان واحد.
- الحفاظ على وضوح تقدم المسودات/الملاحظات عبر المسارات الأساسية والتكميلية.
- توفير المواد المصدرية (`PDF` و`TeX` و`BibTeX` والقوالب) لمواصلة التحرير.

## ✨ الميزات
- تتبع المقررات الأساسية ومراجعها.
- تتبع تقدم المقررات التكميلية.
- ملفات PDF دروس موجودة لعدة مسارات أساسية.
- مواد مصدر LaTeX في مسارات محددة.
- قوالب LaTeX قابلة لإعادة الاستخدام في `template/tuftle` و`template/kaobook`.
- عناصر مرئية للمستودع في `figs/`.

## 📌 لقطة سريعة
| المجال | المتاح |
|---|---|
| 📚 الملاحظات | مجموعات متعددة من ملاحظات المقررات مع تتبع للتقدم |
| 🧪 المصدر | مصادر `TeX/BibTeX` في مشاريع فرعية محددة |
| 🧰 القوالب | `template/tuftle` و`template/kaobook` |
| 🌐 التدويل | مجلد `i18n/` موجود (فارغ حاليًا) |

## 🗂️ هيكل المشروع
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

## 🧩 المتطلبات المسبقة
للقراءة فقط:
- قارئ PDF.

لتحرير/بناء مواد TeX:
- توزيعة LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` أو `biber` حسب المشروع الفرعي.
- `makeindex` للقوالب التي تستخدم الفهرسة.

ملاحظة افتراضية:
- لا يوجد نظام بناء موحّد على مستوى الجذر (`Makefile` أو `package.json` أو `pyproject.toml`) في هذا المستودع.

## 🚀 التثبيت
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

لا يلزم أي خطوة تثبيت حزم للاستخدام الأساسي (قراءة الملاحظات الحالية).

## 🛠️ الاستخدام
### 1) قراءة الملاحظات الحالية
- افتح ملفات PDF في المجلدات ذات الصلة، مثل:
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) العمل على مواد LaTeX
- عدّل ملفات `.tex` و`.bib` في مجلد المقرر/القالب المستهدف.
- قم بالترجمة باستخدام سلسلة الأدوات المتوقعة لذلك المجلد.

## ⚙️ الإعداد
لا يوجد ملف إعداد عام.

الإعداد محلي داخل كل مشروع TeX (صنف المستند، محرك الببليوغرافيا، ملفات التنسيق، مسارات الرسومات)، مثل:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 أمثلة
### المثال A: بناء `template/kaobook`
يوثّق `template/kaobook/main.tex` سلسلة البناء التالية:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### المثال B: بناء `core_cosmology/cosmology_ch10`
يستخدم `cosmology_ch10.tex` النمط `\bibliography{ref}` (سير عمل BibTeX):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### المثال C: عرض ملف PDF لفصل مُولَّد
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 ملاحظات التطوير
- هذا المستودع أساسًا مستودع توثيق/ملاحظات، وليس قاعدة كود تطبيق.
- بعض المجلدات تتضمن نواتج TeX مولدة (`.aux` و`.log` و`.toc` و`.bbl` وغيرها) محفوظة داخل المستودع.
- قد تختلف أوامر البناء حسب المجلد الفرعي؛ اتبع اتفاقيات `.tex` المحلية.
- المجلد `i18n/` موجود ومخصّص لنسخ README متعددة اللغات.

## 📚 التقدم المعتمد للمقررات (محفوظ ومعاد تنظيمه)

### المقررات الأساسية

#### الميكانيكا الكلاسيكية
تم نشر الكتاب الخاص بهذا المقرر [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681). يمكنك شراؤه من Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### ميكانيكا الكم
تم نشر الكتاب الخاص بهذا المقرر [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903). يمكنك شراؤه من Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### النسبية الخاصة والكهروديناميكا
تم نشر الكتاب الخاص بهذا المقرر [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065). يمكنك شراؤه من Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### جدول تقدم المقررات الأساسية
| المقرر | تقدم المسودة | تقدم الملاحظات | الملاحظات/المرجع |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### المقررات التكميلية
| المقرر | تقدم المسودة | تقدم الملاحظات |
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

## 🧯 استكشاف الأخطاء وإصلاحها
- `pdflatex: command not found`
  - ثبّت توزيعة LaTeX وتأكد أن الملفات التنفيذية موجودة ضمن `PATH`.
- عدم ظهور المراجع/الفهرس
  - شغّل الخلفية المطلوبة (`bibtex` أو `biber`) و`makeindex` عند الحاجة، ثم أعد تشغيل `pdflatex`.
- أخطاء فقدان ملفات النمط/الصنف
  - قم بالبناء من دليل المشروع المقصود حتى تُحل المسارات النسبية إلى الأصول المحلية بشكل صحيح.
- اختلاف مخرجات البناء بين البيئات
  - يحتوي هذا المستودع على مواد أُنتجت في بيئات مختلفة؛ وحّد إصدارات الحزم قدر الإمكان.

## 🗺️ خارطة الطريق
- متابعة المسارات التكميلية بمحتوى فصول فعلي وملفات مصدر.
- تحسين اتساق ملفات README الخاصة بكل مقرر.
- إضافة ملفات README متعددة اللغات تحت `i18n/` والحفاظ على مزامنة محدد اللغة.
- إضافة قسم إرشادات بناء على مستوى المستودع لكل مشروع فرعي يحتوي على مصادر TeX.

## ❤️ المساهمة أو التبرع
يمكنك المساهمة في هذا المشروع عبر عمل fork للمشروع ثم إرسال pull request. وإذا ساعدك هذا المشروع على تقليل وقت التطوير، يمكنك دعوتي إلى فنجان قهوة :)

## 🙏 الشكر والتقدير
- البروفيسور Leonard Susskind على المحتوى الأصلي للمحاضرات.
- مصادر الملاحظات المرجعية الحالية:
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 الترخيص
هذا المستودع مرخّص بموجب GNU General Public License v3.0. راجع [LICENSE](LICENSE).
