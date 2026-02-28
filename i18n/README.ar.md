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
![Stars](https://img.shields.io/github/stars/lachlanchen/leonardsusskind?style=flat-square&logo=github&label=stars&color=22c55e)
![Forks](https://img.shields.io/github/forks/lachlanchen/leonardsusskind?style=flat-square&logo=github&label=forks&color=3b82f6)
![Last Commit](https://img.shields.io/github/last-commit/lachlanchen/leonardsusskind?style=flat-square&color=8b5cf6)

> 🎓 أرشيف متعدد اللغات لمواد محاضرات ليو نارد سوسكيند، يحتفظ بنسخ PDF النهائية ومصادر LaTeX القابلة للتحرير للدراسة وإعادة الاستخدام والرجوع إليها.

---

## <a id="overview"></a>نظرة عامة
هذا المستودع هو أرشيف قائم على المحتوى لمواد ملاحظات المحاضرات من منظومة تعليم الأستاذ Leonard Susskind.

> ملاحظات محاضرات الأستاذ Leonard Susskind. إذا كان في هذا انتهاك لحقوق النشر، يرجى التواصل معي لحذف هذا المستودع. لا يتحمل الأستاذ Susskind مسؤولية أي أخطاء أو معلومات مضللة في هذه الملاحظات، وكذلك أنا.

يجمع ثلاث طبقات في مكان واحد:

- مسارات ملاحظات مصنّفة مع تتبّع التقدم للمقررات.
- مخرجات منشورة (`.pdf`) للقراءة والمشاركة.
- ملفات المصدر (`.tex`، `.bib`، القوالب) للمحافظة على الأرشيف أو توسيعه.

### <a id="overview-primary-goals"></a>الأهداف الأساسية
- توحيد ملاحظات المقررات والتقدم في مكان واحد.
- حفظ وضوح حالة المسودات في المسارات الأساسية والتكميلية.
- توفير المواد المصدرية (PDF, TeX, BibTeX, القوالب) للاستمرار في التأليف.

## <a id="features"></a>الميزات
- 📚 تتبّع المقررات الأساسية والمرجعيات.
- 📌 تتبّع تقدم المقررات التكميلية.
- 📄 ملفات PDF موجودة للمحاضرات في عدة مسارات أساسية.
- 🧪 مواد LaTeX المصدرية في مسارات مختارة.
- 🧷 قوالب LaTeX قابلة لإعادة الاستخدام في `template/tuftle` و `template/kaobook`.
- 🎨 عناصر بصرية للمستودع في `figs/`.
- 🌐 مجموعة README متعددة اللغات في `i18n/`.

## <a id="quick-snapshot"></a>لقطة سريعة
| المجال | المتاح |
|---|---|
| 📝 الملاحظات | عدة مجموعات من الملاحظات مع تتبّع تقدم | 
| 🧾 المصدر | مصادر TeX/BibTeX في مشاريع فرعية مختارة |
| 🧱 القوالب | `template/tuftle` و`template/kaobook` |
| 🎨 الهوية | `figs/banner.*`، `figs/logo.*`، `figs/logo-w-text.*` |
| 🌍 i18n | نسخ `i18n/README.*.md` |

## <a id="table-of-contents"></a>جدول المحتويات
- [نظرة عامة](#overview)
- [الميزات](#features)
- [لقطة سريعة](#quick-snapshot)
- [هيكل المشروع](#project-structure)
- [المتطلبات المسبقة](#prerequisites)
- [التثبيت](#installation)
- [الاستخدام](#usage)
- [الإعدادات](#configuration)
- [أمثلة](#examples)
- [ملاحظات التطوير](#development-notes)
- [تقدم المقررات الرسمي (المحفوظ والمعاد تنظيمه)](#canonical-course-progress-preserved-and-reorganized)
- [استكشاف الأخطاء](#troubleshooting)
- [خارطة الطريق](#roadmap)
- [المساهمة](#contribution)
- [❤️ Support](#-support)
- [الشكر والتقدير](#acknowledgements)
- [الترخيص](#license)

## <a id="project-structure"></a>هيكل المشروع
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

## <a id="prerequisites"></a>المتطلبات المسبقة
للقراءة:
- 📖 قارئ PDF (نظامي أو عبر تطبيق).

لتحرير/بناء مواد TeX:
- 📦 توزيعة LaTeX (TeX Live / MiKTeX).
- ⚙️ `pdflatex`.
- 🗂️ `bibtex` أو `biber` حسب المشروع الفرعي.
- 🔎 `makeindex` للمشاريع التي تستخدم الفهارس.

---

ملاحظات افتراضية:
- لا يوجد نظام بناء موحد على مستوى الجذر (`Makefile`، `package.json`، `pyproject.toml`) في هذا المستودع.
- من المتوقّع تشغيل سير العمل من داخل كل دليل فرعي.

## <a id="installation"></a>التثبيت
```bash
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

هذا المستودع قائم على المحتوى. إذا تمّ استنساخه أو عمل fork له، عدّل عنوان الـ remote بما يناسب نسختك.

لا يلزم تثبيت حزم عالمية لقراءة الملاحظات الموجودة.

## <a id="usage"></a>الاستخدام
### 1) قراءة الملاحظات الموجودة
افتح ملفات PDF في المجلدات ذات الصلة، مثل:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) تأليف أو توسيع مواد LaTeX
- عدّل ملفات `.tex` و`.bib` داخل مجلد المقرر/القالب المستهدف.
- قم بالترجمة باستخدام سير العمل المحدد في ذلك المجلد.
- ابني الملفات داخل نفس المجلد حتى تُحلّ المسارات النسبية للأصول المحلية بشكل صحيح.

### 3) التصفح حسب نقاط الدخول لكل مسار
لكل مسار رئيسي ملف `README.md` خاص به يضم ملاحظات المجال، والمرجعيات، والتقدم.

## <a id="configuration"></a>الإعدادات
لا يوجد ملف إعدادات عام.

الإعدادات محليًا لكل مشروع TeX. العوامل النموذجية تكون مضمّنة في مصادر المستند نفسها، بما في ذلك:
- إعداد فئة المستند والحزم في `template/kaobook/main.tex`
- البنية/النمط القابلة لإعادة الاستخدام في `template/kaobook/`
- خلفية الببليوغرافيا ونمط الاستشهاد في أزواج `main.tex`/`ref.bib` المحلية
- مسارات إدراج الصور والأصول المخصّصة لكل فصل في كل مشروع

نقاط إعدادات محلية تمثيلية:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## <a id="examples"></a>الأمثلة
### المثال A: بناء `template/kaobook`
يوثّق ملف `template/kaobook/main.tex` سلسلة التجميع التالية:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### المثال B: بناء `core_cosmology/cosmology_ch10`
يعتمد `cosmology_ch10.tex` على سير عمل مشابه لـ BibTeX:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### المثال C: بناء `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### المثال D: بناء `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### المثال E: عرض الناتج محليًا
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## <a id="development-notes"></a>ملاحظات التطوير
- هذا المستودع هو في المقام الأول مستودع توثيق/ملاحظات، وليس قاعدة كود تطبيق.
- بعض المجلدات تشتمل على مخرجات TeX مجمّعة (`.aux`، `.log`، `.toc`، `.bbl`، وغيرها) محفوظة ضمن المستودع.
- أوامر البناء تختلف حسب كل دليل فرعي؛ اتّبع أعراف `.tex` المحلية.
- توجد ملفات `README.md` لكل مسار عبر الأدلة الأساسية والتكميلية ويجب إبقاؤها متوافقة مع تصريحات التقدم في README الرئيسي.
- مجلد `i18n/` موجود ويُستخدم لنسخ README متعددة اللغات.
- يُعامل README الجذر كمرجعية رسمية؛ ينبغي أن تتبع الملفات المترجمة هذه المرجعية عند التحديثات.

## <a id="canonical-course-progress-preserved-and-reorganized"></a>تقدم المقررات الرسمي (المحفوظ والمعاد تنظيمه)

### المساقات الأساسية

#### الميكانيكا الكلاسيكية
تم نشر كتاب هذا المقرر [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681). ويمكن شراؤه من Amazon عبر [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### ميكانيكا الكم
تم نشر كتاب هذا المقرر [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903). ويمكن شراؤه من Amazon عبر [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### النسبية الخاصة والكهرومغناطيسية
تم نشر كتاب هذا المقرر [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065). ويمكن شراؤه من Amazon عبر [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### جدول تقدم المساقات الأساسية
| المساق | تقدم المسودة | تقدم الملاحظات | الملاحظات/المرجع |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | كانت ملاحظات المحاضرة متاحة على https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | كانت ملاحظات المحاضرة من الفصل 1 إلى 9 متاحة على https://www.lapasserelle.com/cosmology/ . الفصل 10 قيد الإنجاز. |
| Statistical Mechanics | 11/11 | 10/10 | كانت ملاحظات المحاضرة متاحة على https://www.lapasserelle.com/statistical_mechanics/. |

### المساقات التكميلية
| المساق | تقدم المسودة | تقدم الملاحظات |
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
- الجداول المذكورة أعلاه محمية كما هي في README الرسمي.
- تتضمن ملفات المستودع مسارات مكتملة ومسارات تجريبية؛ إذا ظهر تعارض بين قيمة الجدول وحالة المجلد، فاعتبر الجدول نية التوثيق المرجعية وقم بتحديث الطرفين معًا في المراجعات المقبلة.

## <a id="troubleshooting"></a>استكشاف الأخطاء
| المشكلة | الحل |
|---|---|
| `pdflatex: command not found` | ثبّت توزيعة LaTeX وتأكد من أن ملفات التنفيذ ضمن `PATH`. |
| لا تظهر الببليوغرافيا/الفهرس | شغّل المحرك المطلوب (`bibtex` أو `biber`) و`makeindex` إن كان مستخدمًا، ثم أعد تشغيل `pdflatex`. |
| أخطاء ملفات النمط/الفئة | نفّذ البناء من دليل المشروع المقصود حتى تُحلّ المسارات النسبية للأصول المحلية بشكل صحيح. |
| اختلاف خرج البناء بين البيئات | يحتوي هذا المستودع موادًا صُنّعت في بيئات متنوعة؛ حاول توحيد إصدارات الحزم متى أمكن. |
| روابط ترجمة قديمة أو فقدان README لغة | تأكد من مزامنة سطر اختيار اللغة في الأعلى مع الملفات داخل `i18n/`. |
| عدم تطابق روابط GitHub بعد إعادة تسمية المجلد | راجع مجددًا روابط اللغة الجذرية وجميع مراجع `i18n/README.*.md` في خطوة واحدة. |

## <a id="roadmap"></a>خارطة الطريق
- متابعة تطوير المسارات التكميلية بمحتوى فصول حقيقي وملفات مصدر.
- تحسين اتساق ملفات README لكل مقرر.
- توسيع وصيانة ملفات README متعددة اللغات ضمن `i18n/` والحفاظ على مزامنتها.
- إضافة قسم إرشادي بنائي على مستوى المستودع لكل مشروع فرعي يضم مصادر TeX.
- إضافة مقتطفات بناء حسب اختلاف أدوات السلسلة المحلية لكل مسار.
- إضافة أتمتة خفيفة للتحقق من سلامة روابط README/i18n.

## <a id="contribution"></a>المساهمة
يمكنك المساهمة في هذا المشروع عن طريق عمل fork ثم إرسال طلب سحب (PR).

نطاق المساهمة المقترح:
- إضافة أو تحسين ملاحظات الفصول والمرجعيات.
- تحسين جودة مصادر TeX وإرشادات البناء القابلة لإعادة الإنتاج.
- الحفاظ على اتساق تصريحات التقدم بين README الجذر وREADME كل مسار.
- الحفاظ على توازن ملفات README متعددة اللغات ضمن `i18n/`.

أفضل ممارسات طلب السحب:
- اذكر مجلدات المسارات الدقيقة التي تم تعديلها.
- أدرج أوامر تجميع TeX المستخدمة (إن تم تعديل ملفات المصدر).
- حدّث جداول التقدم ذات الصلة عندما تتغيّر حالة الفصول.
- حدّث ملفات `i18n/` بعد أي تغييرات على README الإنجليزي الأساسي.

## <a id="acknowledgements"></a>الشكر والتقدير
- الأستاذ Leonard Susskind على المحتوى الأصلي للمحاضرات.
- مصدر الملاحظات المرجعية: https://www.lapasserelle.com/general_relativity/
- مصدر الملاحظات المرجعية: https://www.lapasserelle.com/cosmology/
- مصدر الملاحظات المرجعية: https://www.lapasserelle.com/statistical_mechanics/

## <a id="license"></a>الترخيص
هذا المستودع مرخّص بموجب رخصة GNU General Public License v3.0. انظر [LICENSE](LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
