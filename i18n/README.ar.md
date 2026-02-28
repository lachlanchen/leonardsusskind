[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# مستودع ملاحظات محاضرات Leonard Susskind

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![Core Tracks](https://img.shields.io/badge/core_tracks-6-1f6feb)
![Supplemental Tracks](https://img.shields.io/badge/supplemental_tracks-9-9a6700)
![i18n](https://img.shields.io/badge/i18n-10%20translations%20%2B%20English-orange)

## نظرة عامة
هذا المستودع أرشيف يركّز على المحتوى لمواد ملاحظات المحاضرات المرتبطة بمقررات البروفيسور Leonard Susskind.

> ملاحظات محاضرات البروفيسور Leonard Susskind. إذا كان هذا ينتهك أي حقوق نشر، يُرجى التواصل معي لحذف هذا المستودع. لا يتحمّل البروفيسور Susskind أي مسؤولية عن الأخطاء أو المعلومات غير الدقيقة في هذه الملاحظات، وكذلك أنا.

### الأهداف الأساسية
- إبقاء ملاحظات المقررات وتقدم العمل في مكان واحد.
- الحفاظ على وضوح تقدم المسودات/الملاحظات عبر المسارات الأساسية والتكميلية.
- توفير المواد المصدرية (PDF وTeX وBibTeX والقوالب) لمواصلة التحرير.

## الميزات
- تتبّع المقررات الأساسية ومراجعها.
- تتبّع تقدم المقررات التكميلية.
- ملفات PDF جاهزة للدروس في عدة مسارات أساسية.
- مواد LaTeX مصدرية في مسارات محددة.
- قوالب LaTeX قابلة لإعادة الاستخدام في `template/tuftle` و`template/kaobook`.
- العناصر البصرية للمستودع في `figs/`.
- مجموعة README متعددة اللغات في `i18n/`.

## لمحة سريعة
| المجال | المتاح |
|---|---|
| 📝 الملاحظات | عدة مجموعات ملاحظات مقررات مع تتبّع التقدم |
| 🧾 المصدر | مصادر TeX/BibTeX في مشاريع فرعية محددة |
| 🧱 القوالب | `template/tuftle` و`template/kaobook` |
| 🎨 الهوية البصرية | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 الترجمة | متغيرات اللغة في `i18n/README.*.md` |

## فهرس المحتويات
- نظرة عامة
- الميزات
- لمحة سريعة
- هيكل المشروع
- المتطلبات المسبقة
- التثبيت
- الاستخدام
- الإعداد
- أمثلة
- ملاحظات التطوير
- التقدم الرسمي للمقررات (محفوظ ومعاد تنظيمه)
- استكشاف الأخطاء وإصلاحها
- خارطة الطريق
- المساهمة
- ❤️ Support
- الشكر والتقدير
- الترخيص

## هيكل المشروع
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

## المتطلبات المسبقة
للقراءة فقط:
- قارئ PDF.

لتحرير/بناء مواد TeX:
- توزيعة LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` أو `biber` بحسب المشروع الفرعي.
- `makeindex` للقوالب التي تستخدم الفهرسة.

ملاحظة افتراضية:
- لا يوجد نظام بناء موحّد على مستوى الجذر (`Makefile` أو `package.json` أو `pyproject.toml`) في هذا المستودع.

## التثبيت
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

إذا كان هذا المستودع متشعبًا (fork) أو نسخة مرآة، استبدل `<your-user>` بالحساب الصحيح.

لا توجد خطوة تثبيت حزم مطلوبة للاستخدام الأساسي (قراءة الملاحظات الموجودة).

## الاستخدام
### 1) قراءة الملاحظات الحالية
افتح ملفات PDF في المجلدات المناسبة، مثلًا:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) العمل على مواد LaTeX
- عدّل ملفات `.tex` و`.bib` في مجلد المقرر/القالب المستهدف.
- قم بالترجمة (compile) باستخدام سلسلة الأدوات المتوقعة لذلك المجلد.
- يفضّل تشغيل أوامر البناء من داخل مجلد المشروع المحلي لكي تُحلّ المسارات النسبية بشكل صحيح.

### 3) التنقل عبر ملفات README الخاصة بالمسارات
كل مسار رئيسي لديه ملف `README.md` محلي خاص به لملاحظات النطاق وتقدم العمل.

## الإعداد
لا يوجد ملف إعداد عام.

الإعداد محلي لكل مشروع TeX (صنف المستند، محرك المراجع، ملفات النمط، ومسارات الرسوميات)، مثلًا:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## أمثلة
### المثال A: بناء `template/kaobook`
`template/kaobook/main.tex` يوثّق سلسلة البناء التالية:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### المثال B: بناء `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` يستخدم `\bibliography{ref}` (تدفق عمل BibTeX):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### المثال C: بناء فصل قائم على Tufte (`supplemental_particle_physics_1/ch1`)
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### المثال D: بناء فصل قائم على Tufte (`supplemental_advanced_quantum/ch1`)
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### المثال E: عرض ملف PDF المُولّد للفصل
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## ملاحظات التطوير
- هذا المستودع هو أساسًا مستودع توثيق/ملاحظات، وليس قاعدة شيفرة تطبيق.
- بعض المجلدات تتضمن مخرجات TeX مولّدة (`.aux`, `.log`, `.toc`, `.bbl`, إلخ) محفوظة داخل المستودع.
- أوامر البناء قد تختلف بحسب المجلد الفرعي؛ اتبع اصطلاحات ملفات `.tex` المحلية.
- توجد ملفات `README.md` لكل مسار عبر مجلدات المسارات الأساسية/التكميلية ويجب إبقاؤها متسقة مع ادعاءات التقدم في README الجذر.
- مجلد `i18n/` موجود ويُستخدم لإصدارات README متعددة اللغات.
- يُعامل README الجذري على أنه المرجع الأساسي؛ ويجب أن تتبعه الملفات متعددة اللغات عند التحديث.

## التقدم الرسمي للمقررات (محفوظ ومعاد تنظيمه)

### المقررات الأساسية

#### الميكانيكا الكلاسيكية
تم نشر كتاب هذا المقرر [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681). يمكنك شراؤه من Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### ميكانيكا الكم
تم نشر كتاب هذا المقرر [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903). يمكنك شراؤه من Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### النسبية الخاصة والكهروديناميكا
تم نشر كتاب هذا المقرر [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065). يمكنك شراؤه من Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### جدول تقدم المقررات الأساسية
| Course | Draft Progress | Notes Progress | Notes/Reference |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### المقررات التكميلية
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

### ملاحظة سلامة التقدم
- الجداول أعلاه محفوظة من النص الرسمي في README.
- ملفات المستودع تتضمن مسارات ناضجة وأخرى مبدئية؛ إذا بدا أن هناك اختلافًا بين الجدول وحالة المجلدات، فاعتبر الجدول هو النية الموثّقة وقم بتحديثهما معًا في المراجعات القادمة.

## استكشاف الأخطاء وإصلاحها
| المشكلة | الحل |
|---|---|
| `pdflatex: command not found` | ثبّت توزيعة LaTeX وتأكد من أن الملفات التنفيذية موجودة في `PATH`. |
| عدم ظهور المراجع/الفهرس | شغّل المحرك المطلوب (`bibtex` أو `biber`) و`makeindex` عند الحاجة، ثم أعد تشغيل `pdflatex`. |
| أخطاء فقدان ملفات style/class | ابنِ المشروع من المجلد المقصود حتى تُحل المسارات النسبية للأصول المحلية بشكل صحيح. |
| اختلاف مخرجات البناء بين البيئات | هذا المستودع يحتوي مواد أُنتجت في بيئات مختلفة؛ وحّد إصدارات الحزم حيثما أمكن. |
| روابط اللغات قديمة أو ملف لغة مفقود | تأكد من تزامن سطر خيارات اللغة أعلى الملف مع الملفات الموجودة ضمن `i18n/`. |
| عدم تطابق روابط Markdown في GitHub بعد إعادة تسمية مجلد | أعد التحقق من روابط لغة الجذر وجميع مراجع `i18n/README.*.md` دفعة واحدة. |

## خارطة الطريق
- مواصلة المسارات التكميلية بمحتوى فصول حقيقي وملفات مصدر.
- تحسين اتساق ملفات README لكل مقرر.
- توسيع وصيانة ملفات README متعددة اللغات تحت `i18n/` مع الحفاظ على تزامن محدد اللغة.
- إضافة قسم إرشادات بناء على مستوى المستودع لكل مشروع فرعي يملك مصادر TeX.
- إضافة مقتطفات بناء لكل مسار عندما توجد فروق في سلسلة الأدوات المحلية.
- إضافة حد أدنى من الأتمتة للتحقق من سلامة روابط README/i18n.

## المساهمة
يمكنك المساهمة في هذا المشروع عبر عمل fork وإرسال pull request.

نطاق مساهمة مقترح:
- إضافة أو تحسين ملاحظات الفصول والمراجع.
- تحسين جودة مصادر TeX وتعليمات البناء القابلة لإعادة الإنتاج.
- إبقاء تصريحات التقدم في README الجذري وملفات README الخاصة بكل مسار متزامنة.
- الحفاظ على تكافؤ ملفات README متعددة اللغات تحت `i18n/`.

ممارسات موصى بها عند إنشاء pull request:
- اذكر مجلد/مجلدات المسار التي تم تعديلها بدقة.
- أدرج أوامر ترجمة TeX المستخدمة (إذا تم تعديل ملفات المصدر).
- حدّث جداول التقدم ذات الصلة عند تغيّر حالة الفصول.
- حدّث ملفات `i18n/` بعد أي تغييرات على README الإنجليزي الأساسي.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## الشكر والتقدير
- البروفيسور Leonard Susskind على المحتوى الأصلي للمحاضرات.
- مصدر الملاحظات المشار إليه: https://www.lapasserelle.com/general_relativity/
- مصدر الملاحظات المشار إليه: https://www.lapasserelle.com/cosmology/
- مصدر الملاحظات المشار إليه: https://www.lapasserelle.com/statistical_mechanics/

## الترخيص
هذا المستودع مرخّص بموجب GNU General Public License v3.0. راجع [LICENSE](LICENSE).
