# تم كتابة هذه الأداة لغرض التعلم فقط.

## كيف يتم استعمالها؟

يوجد حالياً موقع واحد وخيارين للبحث

#

## الخيار الأول عن طريق البحث بالموقع:

```py
import searchforjobs

path = '/path/to/folder'
keywords = ['hr', 'cyper', 'أسنان']
searchfrojobs.jobzatySearch(keywords, 1, folderPath=path)

# first part is search query, can be in english or arabic, the second part is how many pages do you want, by default will be one page.
# the output will be json format in desktop by default, or use your own path.
# every keyword has independent json file by its own name.
```

### البيانات المستخرجة بصيغة json:

#### - المثال تم تطبيقه على وظيفة الموارد البشرية من خلال البحث ويمكن تطبيقه على الوظائف الآخرى، كل صفحة يتم استخراج 10 وظائف منها وتكون حسب الترتيب الزمني.

#### - بسبب سوء تصميم صفحة الموقع قد يتم استبدال application method بروابط أخرى او نص فارغ لذلك وضعت رابط الصفحة للدخول عليها.

```json
{
  "hr": 1,
  "Job data": {
    "Job title": "إعلان وظائف إدارية متعددة للجنسين",
    "Job link": "https://www.jobzaty.com/job/mbc-29110",
    "img": "https://www.jobzaty.com/company_logos/thumb/mrkz-tlfzyon-alshrk-alaost-mbc-1567237340-372.png",
    "Company name": "مجموعة إم بي سي (mbc)",
    "Location": "الرياض",
    "Work schedule": "دوام كامل",
    "Availability": "سعودي فقط",
    "Application method": "https://ehff.fa.em2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/requisitions?location=Saudi+Arabia&locationId=300000000275219&locationLevel=country&sortBy=POSTING_DATES_DESC",
    "Web page data": {
      "Job title": "إعلان وظائف إدارية متعددة للجنسين",
      "Announcement date": "تاريخ الإعلان: May 16, 2023",
      "Company name": "مجموعة إم بي سي (mbc)",
      "Job details": {
        "Location": "الرياض",
        "Work Schedule": "دوام كامل",
        "Availability": "سعودي فقط",
        "Experience": "غير محدد",
        "Gender": "بدون تفضيل",
        "Education": "البكالوريوس",
        "Deadline": "May 30, 2023"
      },
      "Extra details": [
        "الوصف الوظيفي",
        "مجموعة إم بي سي (mbc)، توفر وظائف شاغرة (للرجال و النساء) للعملل بمقر المجموعة بمدينة الرياض؛ في عدة مجالات، وفقاً للتفاصيل التالية:",
        "الوظائف الشاغرة:",
        "1- مشرف المحاسبة (التدقيق).",
        "(Accounting Supervisor - Audit)",
        "2- مُنتج المحتوى الرقمي.",
        "(Digital Content Producer)",
        "3- محاسب - حسابات القبض.",
        "(Accountant - Accounts Receivable)",
        "4- مدير الحساب.",
        "(Account Manager)",
        "5- محلل أعمال.",
        "(Business Analyst)",
        "6- مخطط الأعمال.",
        "(Business Planner)",
        "7- مدير التمويل التجاري.",
        "(Commercial Finance Manager)",
        "مكان العمل:",
        "- الرياض.",
        "طريقة التقديم:",
        "- للاطلاع على المهام الوظيفية وبقية الشروط والتقديم على وظائف مجموعة إم بي سي؛ عبر موقعها الرسمي:",
        "رابط التقديم: (اضغط هنا)",
        "◀️ لمتابعة قروب تليجرام للوظائف: ( اضغط هنا )",
        "◀️ لمتابعة حساب تويتر: ( اضغط هنا )",
        "للمشاركة واتساب: ( اضغط هنا )",
        "  أحدث الوظائف في مجموعة إم بي سي (mbc)",
        "شارك الوظيفة",
        "روابط ذات صلة",
        "وظائف المحاسبة والخدمات المالية والمصرفيةوظائف الشركات الكبرىوظائف للنساءوظائف حديثي التخرج",
        "وظائف الرياض"
      ]
    }
  }
}
```

#

## الخيار الثاني عن طريق البحث داخل التصنيفات الخاصة بموقع جوبذاتي المكون من 32 تصنيف:

```py
import searchforjobs

path = '/path/to/folder'
searchfrojobs.jobzatyCategory(folderPath=path)

# action will be in terminal, chose a number or more reference to a category, then select a number for pages.
# the output will be json format in desktop by default, or use your own path.
# every keyword has independent json file by its own name.
```

### مثال 1 لتصنيف واحد فقط:

```
Please choose a category:
1. Big companies
2. Government
3. Information technology
4. Business development
5. Secretarial clerical front office
6. Customer support
7. Health medical
8. Distribution logistics
9. Education
10. Banks
11. Design
12. Business management
13. Fresh graduate
14. Jobs for women
15. HR
16. Taqat
17. Law legal affairs
18. Public relations
19. Project management
20. Media advertising
21. Quality control
22. Data entry
23. Accounts financial services banking
24. Engineering
25. Marketing
26. Sales
27. Manufacturing operations
28. Planning development
29. Procurement warehousing
30. Information security
31. training
32. Cybersecurity jobs
33. New jobs with no specification

Select number or more separated by comma: 1
Please choose number of pages for BIG COMPANIES: 1
```

### مثال 2 لتصنيفين او أكثر:

```
Please choose a category:
1. Big companies
2. Government
3. Information technology
# ... other categories ...

Select number or more separated by comma: 1, 16
Please choose number of pages for BIG COMPANIES: 1
Please choose number of pages for TAQAT: 1
```

### البيانات المستخرجة بصيغة json:

#### - المثال تم تطبيقه على تصنيف الشركات الكبيرة، كل تصنيف يتم كتابة ملف خاص به فلو بحثت عن تصنيف طاقات والشركات الكبيرة سيتم كتابة ملف خاص بطاقات وملف مختلف خاص بالشركات الكبيرة، كل صفحة يكون بها 10 وظائف، اذا اختزت صفحتين ستكون هناك 20 وظيفة، يتم جلب الوظائف الجديدة ثم الوظائف الأقدم حسب التاريخ.

#### - بسبب سوء تصميم صفحة الموقع قد يتم استبدال application method بروابط أخرى او نص فارغ لذلك وضعت رابط الصفحة للدخول عليها.

```json
{
  "Category": "BIG COMPANIES",
  "Link": "https://www.jobzaty.com/jobs/category/big-companies",
  "Job data": {
    "job 1": {
      "Job title": "شركة التعليمية توفر وظائف شاغرة للجنسين",
      "Job link": "https://www.jobzaty.com/job/talemia-29109",
      "img": "https://www.jobzaty.com/company_logos/thumb/shrk-altaalymy-1654007472-18.jpg",
      "Company name": "شركة التعليمية",
      "Location": "الرياض",
      "Work schedule": "دوام كامل",
      "Availability": "سعودي فقط",
      "Application method": "https://fa-erql-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_7/requisitions",
      "Web page data": {
        "Job title": "شركة التعليمية توفر وظائف شاغرة للجنسين",
        "Announcement date": "تاريخ الإعلان: May 16, 2023",
        "Company name": "شركة التعليمية",
        "Job details": {
          "Location": "الرياض",
          "Work Schedule": "دوام كامل",
          "Availability": "سعودي فقط",
          "Experience": "غير محدد",
          "Gender": "بدون تفضيل",
          "Education": "البكالوريوس",
          "Deadline": "May 23, 2023"
        },
        "Extra details": [
          "الوصف الوظيفي",
          "شركة التعليمية (TALEMIA) شركة حكومية مملوكة لـ (صندوق الاستثمارات العامة)، تعلن عبر موقعها الرسمي (بوابة التوظيف)؛ توفر وظائف شاغرة في عدة مجالات، بمقر الشركة بمدينة الرياض، وفقاً للتفاصيل التالية:",
          "الوظائف الشاغرة:",
          "1- أخصائي تطوير التطبيقات.",
          "(Application Development Specialist)",
          "2- مسؤول جودة التطبيقات.",
          "(Application Quality Officer)",
          "3- مدير منتج أول.",
          "(Senior Product Manager)",
          "4- مدير مشروع أول (وظيفتان).",
          "(Senior Project Manager)",
          "5- خبير التعلم الإلكتروني.",
          "(E-Learning Expert)",
          "6- محلل النظم.",
          "(System Analyst)",
          "عن الشركة:",
          "تأسست شركة التعليمية – المملوكة بالكامل لصندوق الاستثمارات العامة – في 18 مايو 2012م، لتطوير النظم التعليمية للحصول على التعليم الأمثل في القرن الحادي والعشرين. وتتطلع \"التعليمية\" في رؤيتها لأن تكون الشريك الأول في الحلول التعليمية المبتكرة والكاملة، إيماناً منها بأن التعليم أحد دعائم الدول المتقدمة التي تسعى للريادة والتميز. في وقت أضحى الاهتمام بالتعليم ضرورة حتمية على المجتمعات التي ترغب في أن يكون التعليم محوراً أساسياً، وركيزة، ويحقق التوافق بين مخرجاته وبين احتياجات سوق العمل.",
          "- للاطلاع على المهام الوظيفية والتقديم على وظائف شركة التعليمية عبر موقعها الرسمي:",
          "بوابة التوظيف: ( اضغط هنا )",
          "◀️ لمتابعة قروب تليجرام للوظائف: ( اضغط هنا )",
          "◀️ لمتابعة حساب تويتر: ( اضغط هنا )",
          "للمشاركة واتساب: ( اضغط هنا )",
          "  أحدث الوظائف في شركة التعليمية",
          "شارك الوظيفة",
          "روابط ذات صلة",
          "وظائف الهندسةوظائف الموارد البشريةوظائف تقنية المعلوماتوظائف إدارة أعمالوظائف قانونيةوظائف الشركات الكبرىوظائف حديثي التخرج",
          "وظائف الرياض"
        ]
      }
    }
  }
}
```
