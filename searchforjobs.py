import requests, json, re, os, datetime
from bs4 import BeautifulSoup

defaultPath = os.path.join(
    os.path.expanduser("~"), "Desktop/Python/folder-jobs"
)  # default path in desktop
if not os.path.exists(defaultPath):  # create a folder to collect the json or photos
    os.mkdir(defaultPath)
currentTimeString = datetime.datetime.now().strftime("%d-%m %H:%M")

def extract_job_details(jobDetails):
    location = re.search(r"الموقع\n\n(.*?)\n\n", jobDetails)
    work_schedule = re.search(r"الدوام\n(.*?)\n\n", jobDetails)
    availability = re.search(r"متاحة لـ\n(.*?)\n\n", jobDetails)
    experience = re.search(r"الخبرة\n(.*?)\n\n", jobDetails)
    gender = re.search(r"الجنس\n(.*?)\n\n", jobDetails)
    education = re.search(r"الدرجة العلمية\n(.*?)\n\n", jobDetails)
    deadline = re.search(r"أخر موعد\n(.*?)\n", jobDetails)

    job_details = {
        "Location": location.group(1) if location else "",
        "Work Schedule": work_schedule.group(1) if work_schedule else "",
        "Availability": availability.group(1) if availability else "",
        "Experience": experience.group(1) if experience else "",
        "Gender": gender.group(1) if gender else "",
        "Education": education.group(1) if education else "",
        "Deadline": deadline.group(1) if deadline else "",
    }

    return job_details


def jobzatySearch(
    query: list,
    pages: int = 1,
    folderPath: str = defaultPath,
):
    for job in query:
        i = 0
        for page in range(pages):
            jobData = []
            if not os.path.exists(folderPath):
                os.mkdir(folderPath)
            jsonFilePath = os.path.join(folderPath, f"{job.upper()} by search at ({currentTimeString}).json")
            jobzaty = f"https://www.jobzaty.com/search_jobs?search={job}&country_id%5B%5D=191&page={page+1}"
            requestJobzaty = requests.get(jobzaty)
            htmlParser = BeautifulSoup(requestJobzaty.text, "html.parser")

            for div in htmlParser.find_all("div", {"class": "jobint"}):
                i += 1
                title = div.find("a")["title"]
                jobLink = div.find("a")["href"]
                img = div.find("img")
                companyName = div.find("div", {"class": "company"})

                requestWebPageData = requests.get(jobLink)
                htmlWebPageDataParser = BeautifulSoup(
                    requestWebPageData.text, "html.parser"
                )
                header = htmlWebPageDataParser.find_all("div", {"class": "jobinfo"})
                announcementDate = header[0].find("div", {"class": "ptext"})
                jobDetailsHeader = htmlWebPageDataParser.find(
                    "div", {"class": "job-header one"}
                )
                jobDetails = jobDetailsHeader.find("ul", {"class": "jbdetail"})
                getJobDetails = extract_job_details(jobDetails.text)

                pageContent = htmlWebPageDataParser.find("div", {"class": "contentbox"})

                plainPageContent = pageContent.find("p")
                jobs = [job for job in pageContent.text.split("\n") if job != ""]

                applicationMethod = plainPageContent.find("a", {"rel": "nofollow"})[
                    "href"
                ]

                jobData.append(
                    {
                        job: i,
                        "Job data": {
                            "Company name": companyName.text.rstrip(),
                            "Job title": title,
                            "Job link": jobLink,
                            "img": img["src"],
                            "Announcement date": announcementDate.text,
                            "Application method": applicationMethod,
                            "Job details": getJobDetails,
                            "Web page data": {
                                "Extra details": jobs,
                            },
                        },
                    }
                )
        with open(jsonFilePath, "w", encoding="utf-8") as Data:
            json.dump(jobData, Data, ensure_ascii=False)


def jobzatyCategory(
    folderPath: str = defaultPath,
):
    if not os.path.exists(folderPath):  # create a folder to collect the json or photos
        os.mkdir(folderPath)

    categories: dict = {
        "1": "https://www.jobzaty.com/jobs/category/big-companies",
        "2": "https://www.jobzaty.com/jobs/category/government",
        "3": "https://www.jobzaty.com/jobs/category/information-technology",
        "4": "https://www.jobzaty.com/jobs/category/business-development",
        "5": "https://www.jobzaty.com/jobs/category/secretarial-clerical-front-office",
        "6": "https://www.jobzaty.com/jobs/category/customer-support",
        "7": "https://www.jobzaty.com/jobs/category/health-medical",
        "8": "https://www.jobzaty.com/jobs/category/distribution-logistics",
        "9": "https://www.jobzaty.com/jobs/category/education",
        "10": "https://www.jobzaty.com/jobs/category/banks-job",
        "11": "https://www.jobzaty.com/jobs/category/design",
        "12": "https://www.jobzaty.com/jobs/category/business-management",
        "13": "https://www.jobzaty.com/jobs/category/fresh-graduate",
        "14": "https://www.jobzaty.com/jobs/category/jobs-for-women",
        "15": "https://www.jobzaty.com/jobs/category/hr",
        "16": "https://www.jobzaty.com/jobs/category/taqat",
        "17": "https://www.jobzaty.com/jobs/category/law-legal-affairs",
        "18": "https://www.jobzaty.com/jobs/category/public-relations",
        "19": "https://www.jobzaty.com/jobs/category/project-management",
        "20": "https://www.jobzaty.com/jobs/category/media-advertising",
        "21": "https://www.jobzaty.com/jobs/category/quality-control",
        "22": "https://www.jobzaty.com/jobs/category/data-entry",
        "23": "https://www.jobzaty.com/jobs/category/accounts-financial-services-banking",
        "24": "https://www.jobzaty.com/jobs/category/engineering",
        "25": "https://www.jobzaty.com/jobs/category/marketing",
        "26": "https://www.jobzaty.com/jobs/category/sales",
        "27": "https://www.jobzaty.com/jobs/category/manufacturing-operations",
        "28": "https://www.jobzaty.com/jobs/category/planning-development",
        "29": "https://www.jobzaty.com/jobs/category/procurement-warehousing",
        "30": "https://www.jobzaty.com/jobs/category/information-security",
        "31": "https://www.jobzaty.com/jobs/category/training",
        "32": "https://www.jobzaty.com/jobs/category/cybersecurity-jobs",
        "33": "https://www.jobzaty.com/jobs",
    }
    chosenCategory = input(
        "\nPlease choose a category:\n1. Big companies\n2. Government\n3. Information technology\n4. Business development\n5. Secretarial clerical front office\n6. Customer support\n7. Health medical\n8. Distribution logistics\n9. Education\n10. Banks\n11. Design\n12. Business management\n13. Fresh graduate\n14. Jobs for women\n15. HR\n16. Taqat\n17. Law legal affairs\n18. Public relations\n19. Project management\n20. Media advertising\n21. Quality control\n22. Data entry\n23. Accounts financial services banking\n24. Engineering\n25. Marketing\n26. Sales\n27. Manufacturing operations\n28. Planning development\n29. Procurement warehousing\n30. Information security\n31. training\n32. Cybersecurity jobs\n33. New jobs with no specification\n\nSelect number/numbers separated by comma: "
    ).split(", ")

    for category in chosenCategory:
        if category not in categories:
            print("Invalid choice. Please try again.")
            return jobzatyCategory()
        categoryName = (
            str(categories.get(category))
            .replace("https://www.jobzaty.com/jobs/category/", "")
            .replace("https://www.jobzaty.com/", "")
            .replace("-", " ")
            .upper()
        )

        job = categories[category]
        pages = int(input(f"Please choose number of pages for {categoryName}: "))
        i = 0
        jobData = []
        jsonFilePath = os.path.join(folderPath, f"{categoryName} Category at ({currentTimeString}).json")
        for page in range(pages):
            jobzaty = f"{job}?page={page+1}"
            requestJobzaty = requests.get(jobzaty)
            htmlParser = BeautifulSoup(requestJobzaty.text, "html.parser")
            for div in htmlParser.find_all("div", {"class": "jobint"}):
                i += 1
                title = div.find("a")["title"]
                jobLink = div.find("a")["href"]
                img = div.find("img")
                companyName = div.find("div", {"class": "company"})

                requestWebPageData = requests.get(jobLink)
                htmlWebPageDataParser = BeautifulSoup(
                    requestWebPageData.text, "html.parser"
                )
                header = htmlWebPageDataParser.find_all("div", {"class": "jobinfo"})
                announcementDate = header[0].find("div", {"class": "ptext"})
                jobDetailsHeader = htmlWebPageDataParser.find(
                    "div", {"class": "job-header one"}
                )
                jobDetails = jobDetailsHeader.find("ul", {"class": "jbdetail"})
                getJobDetails = extract_job_details(jobDetails.text)

                pageContent = htmlWebPageDataParser.find("div", {"class": "contentbox"})

                plainPageContent = pageContent.find("p")
                jobs = [job for job in pageContent.text.split("\n") if job != ""]

                applicationMethod = plainPageContent.find("a", {"rel": "nofollow"})[
                    "href"
                ]

                jobData.append(
                    {
                        "Category": categoryName,
                        "Link": job,
                        "Job data": {
                            f"job {i}": {
                                "Job title": title,
                                "Job link": jobLink,
                                "img": img["src"],
                                "Company name": companyName.text.rstrip(),
                                "Announcement date": announcementDate.text,
                                "Application method": applicationMethod,
                                "Job details": getJobDetails,
                                "Web page data": {
                                    "Extra details": jobs,
                                },
                            },
                        },
                    }
                )

        with open(jsonFilePath, "w", encoding="utf-8") as Data:
            json.dump(jobData, Data, ensure_ascii=False)


def jobzatyCompanies(companyPages: int = 1, folderPath: str = defaultPath):
    jobData = []
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
    jsonFilePath = os.path.join(folderPath, f"Companies data at ({currentTimeString}).json")
    i=0
    for page in range(1, companyPages + 1):
        companies = f"https://www.jobzaty.com/companies?page={page+1}"
        requestJobzaty = requests.get(companies)
        htmlParser = BeautifulSoup(requestJobzaty.text, "html.parser")

        for div in htmlParser("div", {"class": "compint"}):
            companyImg = (
                div.find("div", {"class": "imgwrap"}).find("img").get("src", "")
            )
            companyName = div.find("h2").text
            companyLocation = div.find("div", {"class": "loctext"}).text
            companyTotalJobs = div.find("div", {"class": "curentopen"}).text
            companyUrl = div.find("h2").find("a").get("href", "")

            jobData.append(
                {
                    i: {
                        "Company name": companyName,
                        "Company image": companyImg,
                        "Company location": companyLocation,
                        "Total jobs": companyTotalJobs,
                        "Company URL": companyUrl,
                    }
                }
            )

    with open(jsonFilePath, "w", encoding="utf-8") as Data:
        json.dump(jobData, Data, ensure_ascii=False)