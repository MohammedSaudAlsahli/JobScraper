# تم كتابة هذه الأداة لغرض التعلم فقط.

### كيف يتم تحميلها؟ 


``` 
pip install requests
``` 
``` 
pip install bs4
``` 
``` 
pip intall git+https://github.com/MohammedSaudAlsahli/JobScraper.git
```
#

### كيف يتم استعمالها؟

يوجد حالياً موقع واحد وخيارين للبحث
## الخيار الأول عن طريق البحث بالموقع:

```py
import jobscraper

path = '/path/to/folder'
keywords = ['hr', 'cyper', 'أسنان']
jobscraper.jobzatySearch(keywords, 1, folderPath=path)

# first part is search query, can be in english or arabic, the second part is how many pages do you want, by default will be one page.
# the output will be json format in desktop by default, or use your own path.
# every keyword has independent json file by its own name.
```

### البيانات المستخرجة بصيغة json:

#### - المثال تم تطبيقه على وظيفة الموارد البشرية من خلال البحث ويمكن تطبيقه على الوظائف الآخرى، كل صفحة يتم استخراج 10 وظائف منها وتكون حسب الترتيب الزمني بحيث يكون رقم 1 هو آخر وظيفة تم اعلانها في صفحة البحث.

#### - بسبب سوء تصميم صفحة الموقع قد يتم استبدال application method بروابط أخرى او نص فارغ او غير مفهوم، لذلك وضعت رابط صفحة الموقع للدخول عليها.

```json
{
    "hr": 1,
    "Job data": {
      "Company name": "الشركة السعودية للصناعات الأساسية سابك",
      "Job title": "سابك توفر 23 وظيفة إدارية وتقنية وهندسية",
      "Job link": "https://www.jobzaty.com/job/sabic-29116",
      "img": "https://www.jobzaty.com/company_logos/thumb/alshrk-alsaaody-llsnaaaat-alasasy-sabk-1575743824-308.jpeg",
      "Announcement date": "تاريخ الإعلان: May 17, 2023",
      "Application method": "https://www.linkedin.com/jobs/search/?currentJobId=3592717603&f_C=165806&geoId=100459316&location=%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9&refresh=true",
      "Job details": {
        "Location": "غير محدد",
        "Work Schedule": "دوام كامل",
        "Availability": "غير محدد",
        "Experience": "غير محدد",
        "Gender": "بدون تفضيل",
        "Education": "البكالوريوس",
        "Deadline": "Jun 10, 2023"
      },
      "Web page data": {
        "Extra details": [
          "الوصف الوظيفي",
          "الشركة السعودية للصناعات الأساسية سابك، تعلن عبر موقعها الرسمي (بوابة التوظيف)، توفر وظائف شاغرة بعدة مجالات إدارية، تقنية، هندسية، وغيرها - وفقاً للتفاصيل التالية:",
          "المسميات الوظيفية:",
          "1- مهندس إدارة القدرات.",
          "(Capability Management Engineer)",
          "2- مهندس البيئة والصحة والسلامة والأمن.",
          "(EHSS Engineer)",
          "3- مهندس إدارة المخاطر.",
          "(Risk Management Engineer)",
          "4- مهندس انشاءات.",
          "(Construction Engineer)",
          "5- مدير ضمان النمو الاستراتيجي-إدارة المخاطر.",
          "(Assurance , Strategic Growth - Risk Management)",
          "6- مدير المخاطر ، النمو الاستراتيجي-إدارة المخاطر.",
          "(Sr. Risk Manager, Strategic Growth - Risk Management)",
          "7- أخصائي التخطيط الضريبي والمشاريع.",
          "(Sr. Specialist, Tax Planning & Projects)",
          "8- مخطط المشروع.",
          "(Project Planner)",
          "9-  أخصائي MTO.",
          "(MTO Specialist)",
          "10- مهندس أول ، الاستدامة.",
          "(Lead Engineer, Sustainability)",
          "11- مهندس أول سلامة العمليات.",
          "(Lead Process Safety Engineer)",
          "12- مدير تطوير المشاريع.",
          "(Sr. Venture Development Manger)",
          "13- أخصائي إدارة المحافظ المتخصصة.",
          "(Sr. Specialist Portfolio Management)",
          "14- مهندس إنشائي مدني.",
          "(Civil Structural Engineer)",
          "15- محلل ، البحوث الاقتصادية.",
          "(Sr. Analyst, Economic Research)",
          "16- مهندس تقدير التكلفة.",
          "(Cost Estimation Engineer)",
          "17- محلل تقنية المعلومات / نظم الإدارة.",
          "(Sr. Analyst, IT/EDMS)",
          "* بالإضافة لوظائف أخرى في عدة تخصصات.",
          "* يتم تحديث الوظائف (حذف / إضافة) حسب الاكتفاء.",
          "عن سابك:",
          "الشركة السعودية للصناعات الأساسية (سابك \"SABIC\") شركة مساهمة عامة سعودية متعددة الصناعات، تنشط في مجال البتروكيماويات والكيماويات والمبلمرات الصناعية والأسمدة والمعادن. تعتبر شركة سابك خامس أكبر شركة بتروكيميات في العالم، وأكبر شركة عامة في الشرق الأوسط والمملكة العربية السعودية كما هو مدرج في تداول. تعود ملكية 70٪ من أسهم سابك لشركة أرامكو السعودية. بالإضافة إلى المساهمين من القطاع الخاص وهم من المملكة العربية السعودية ودول أخرى من دول مجلس التعاون الخليجي الست ( المصدر )",
          "رابط التقديم على وظائف سابك:",
          "- للاطلاع على المهام الوظيفية والشروط والتقديم على وظائف شركة سابك عبر موقعها الرسمي:",
          "بوابة التوظيف: ( اضغط هنا )",
          "◀️ لمتابعة قروب تليجرام للوظائف: ( اضغط هنا )",
          "◀️ لمتابعة حساب تويتر: ( اضغط هنا )",
          "للمشاركة واتساب: ( اضغط هنا )",
          "  أحدث الوظائف في الشركة السعودية للصناعات الأساسية سابك",
          "شارك الوظيفة",
          "روابط ذات صلة",
          "وظائف الهندسةوظائف المحاسبة والخدمات المالية والمصرفيةوظائف تقنية المعلوماتوظائف إدارة أعمالوظائف حكوميةوظائف الشركات الكبرىوظائف للنساءوظائف حديثي التخرج",
          "وظائف غير محدد"
        ]
      }
    }
  },
  {
    "hr": 2,
    "Job data": {
      "Company name": "مجموعة الدكتور سليمان الحبيب الطبية",
      "Job title": "فتح التوظيف للجنسين في عدة مجالات",
      "Job link": "https://www.jobzaty.com/job/alhabib-29115",
      "img": "https://www.jobzaty.com/company_logos/thumb/mjmoaa-aldktor-slyman-alhbyb-altby-1649368675-274.jpg",
      "Announcement date": "تاريخ الإعلان: May 16, 2023",
      "Application method": "/cdn-cgi/l/email-protection#eda5bfc3bda5aead899f9e98818c84808c838c81858c8f848fc38e8280",
      "Job details": {
        "Location": "الرياض",
        "Work Schedule": "دوام كامل",
        "Availability": "غير محدد",
        "Experience": "غير محدد",
        "Gender": "رجال / نساء",
        "Education": "الثانوية العامة فما فوق",
        "Deadline": "Jun 10, 2023"
      },
      "Web page data": {
        "Extra details": [
          "الوصف الوظيفي",
          "مجموعة الدكتور سليمان الحبيب الطبية، تعلن فتح التقديم (للرجال والنساء) لشغل وظائف متعددة في عدة مجالات، بمدينة الرياض، وفقاً للتفاصيل التالية:",
          "المؤهلات المطلوبة:",
          "- الثانوية العامة.",
          "- الدبلوم.",
          "- البكالوريوس فما فوق.",
          "الوظائف الشاغرة:",
          "- مساعد إداري.",
          "(Admin Assistant)",
          "- وظائف أمنية.",
          "(security)",
          "- سكرتير.",
          "(Secretary)",
          "- منسق خدمة المرضى.",
          "(Patient service coordinator)",
          "- منسق التسويق.",
          "(Marketing coordinator)",
          "- أخصائي الأشعة (طبيب).",
          "(Radiology Specialist - Doctor)",
          "- فني الأشعة.",
          "(Radiology Technologist)",
          "- فني الموجات فوق الصوتية.",
          "(Ultrasound technologist)",
          "- أخصائي مختبر (طبيب).",
          "(Labatory specialist - Doctor)",
          "- فني مختبر.",
          "(Labotory technologist)",
          "- فنى سحب دم.",
          "(Phlebotomist)",
          "- مسعف EMT.",
          "(Paramedic EMT)",
          "- أخصائي السمع.",
          "(Audiologist)",
          "- فني ECHO.",
          "(ECHO Tech)",
          "طريقة التقديم:",
          "- ترسل السيرة الذاتية على البريد التالي:",
          "( [email protected] )",
          "مع كتابة (المسمى الوظيفي) باللغة الإنجليزية في عنوان الايميل.",
          "◀️ لمتابعة قروب تليجرام للوظائف: ( اضغط هنا )",
          "◀️ لمتابعة حساب تويتر: ( اضغط هنا )",
          "للمشاركة واتساب: ( اضغط هنا )",
          "  أحدث الوظائف في مجموعة الدكتور سليمان الحبيب الطبية",
          "شارك الوظيفة",
          "روابط ذات صلة",
          "وظائف صحية وطبيةوظائف التسويقوظائف إدارة أعمالوظائف العلاقات العامةوظائف الخدمات الأمنية والحراسةوظائف الترجمة واللغاتوظائف حكوميةوظائف الشركات الكبرىوظائف للنساءوظائف الصيدلةوظائف التمريض",
          "وظائف الرياض"
        ]
      }
    }
  }
```

#

## الخيار الثاني عن طريق البحث داخل التصنيفات الخاصة بموقع جوبذاتي المكون من 32 تصنيف:

```py
import jobscraper

path = '/path/to/folder'
jobscraper.jobzatyCategory(folderPath=path)

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

#### - بسبب سوء تصميم صفحة الموقع قد يتم استبدال application method بروابط أخرى او نص فارغ او غير مفهوم، لذلك وضعت رابط الصفحة للدخول عليها.

```json
{
  "Category": "BIG COMPANIES",
  "Link": "https://www.jobzaty.com/jobs/category/big-companies",
  "Job data": {
    "job 1": {
      "Job title": "الراجحي توفر وظائف إدارية شاغرة",
      "Job link": "https://www.jobzaty.com/job/rajhi-29118",
      "img": "https://www.jobzaty.com/company_logos/thumb/shrk-alrajhy-llbna-oaltaamyr-1666698114-136.jpg",
      "Company name": "شركة الراجحي للبناء والتعمير",
      "Announcement date": "تاريخ الإعلان: May 17, 2023",
      "Application method": "/cdn-cgi/l/email-protection#fe9d9f8c9b9b8c8dbe9f928c9f949697d39d91d08d9f",
      "Job details": {
        "Location": "غير محدد",
        "Work Schedule": "دوام كامل",
        "Availability": "سعودي فقط",
        "Experience": "غير محدد",
        "Gender": "بدون تفضيل",
        "Education": "البكالوريوس",
        "Deadline": "May 31, 2023"
      },
      "Web page data": {
        "Extra details": [
          "الوصف الوظيفي",
          "شركة الراجحي للبناء و التعمير، تُوفر وظائف إدارية شاغرة للعمل بمجال السكرتارية؛ بمقر الشركة في مدينة الرياض، مع ملاحظة أن التقديم متاح للسعوديين فقط - وفقاً للتفاصيل التالية:",
          "المسمى الوظيفي:",
          "- سكرتير تنفيذي.",
          "المهام الوظيفية :",
          "- إعداد جدول الأعمال للرئيس التنفيذي والمساعدة في تخطيط المواعيد واجتماعات مجلس الإدارة والمؤتمرات",
          "- التنسيق وحضور الاجتماعات بالنيابة عن الرئيس التنفيذي.",
          "- استقبال المكالمات الهاتفية وإعادة توجيهها حسب الطلب.",
          "- التعامل المراسلات الصادرة والواردة وترتيبها حسب الأولويات.",
          "- التعامل مع الوثائق السرية والتأكد من بقائها بشكل آمن.",
          "- إعداد الفواتير و البيانات المالية وتقديم المساعدة في مسك الدفاتر.",
          "- الحفاظ على السجلات الإلكترونية والورقية وضمان تنظيم المعلومات بحيث يمكن الوصول إليها بسهولة.",
          "- إجراء البحوث وإعداد العروض التقديمية و التقارير عند الطلب.",
          "المهارات المطلوبة:",
          "- اجادة استخدام برامج مايكروسوفت اوفيس MS Office.",
          "- القدرة على استخدام برامج تخطيط موارد المشاريع ERP.",
          "- المعرفة الجيدة بإدارة المكاتب والإجراءات المحاسبية الأساسية.",
          "- اجادة التعامل مع المفردات الفنية للصناعات المختلفة.",
          "- الإلمام بأساليب البحث الأساسية وتقنيات إعداد التقارير.",
          "- امتلاك مهارات تنظيمية قوية والقدرة على إدارة وقت بشكل ممتاز.",
          "- القدرة على التفاوض والإقناع.",
          "- اجادة مهارات التواصل مع الشخصيات المختلفة.",
          "- النزاهة والسرية في التعامل مع البيانات المختلفة.",
          "- إجادة اللغة الإنجليزية.",
          "متطلبات العمل:",
          "- سعودي الجنسية.",
          "- الحصول على درجة البكالوريوس في إدارة الأعمال أو تخصص ذات صلة.",
          "- الخبرة العملية في وظيفة سكرتير تنفيذي.",
          "مكان العمل:",
          "- الرياض.",
          "طريقة التقديم:",
          "- للتقديم على وظائف شركة الراجحي للبناء و التعمير، تُرسل السيرة الذاتية على البريد التالي:",
          "( [email protected] )",
          "- مع كتابة (المسمى الوظيفي) في حقل العنوان.",
          "◀️ لمتابعة قروب تليجرام للوظائف: ( اضغط هنا )",
          "◀️ لمتابعة حساب تويتر: ( اضغط هنا )",
          "للمشاركة واتساب: ( اضغط هنا )",
          "  أحدث الوظائف في شركة الراجحي للبناء والتعمير",
          "شارك الوظيفة",
          "روابط ذات صلة",
          "وظائف إدارة أعمالوظائف السكرتارية والدعم الإداريوظائف الشركات الكبرىوظائف للنساءوظائف حديثي التخرج",
          "وظائف غير محدد"
        ]
      }
    }
  }
}
```
