import json

data = [
    {
     "Column1": 1,
     "title": "Presidentâ€™s Scholarship for Ukraine",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$2500",
     "date": "31-Jul-22",
     "location": "united-states"
    },
    {
     "Column1": 1,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 3,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "united-states"
    },
    {
     "Column1": 4,
     "title": "Improve Menâ€™s Health Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$2000",
     "date": "31-May-22",
     "location": "united-states"
    },
    {
     "Column1": 5,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "united-states"
    },
    {
     "Column1": 6,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 7,
     "title": "American Indian Scholarships at Augsburg University",
     "degrees": "Bachelor",
     "funds": "Partial tuition fees",
     "date": "01-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 8,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "united-states"
    },
    {
     "Column1": 9,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "united-states"
    },
    {
     "Column1": 10,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "united-states"
    },
    {
     "Column1": 11,
     "title": "Medicine: Fully Funded Swansea & HMRI PhD Scholarship: Ovarian Cancer Chemoresistance",
     "degrees": "Phd",
     "funds": "Full cost of tuition fees and an annual stipend",
     "date": "06-May-22",
     "location": "united-states"
    },
    {
     "Column1": 12,
     "title": "New York University - September 11 Scholarships",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Pay any remaining balance.",
     "date": "30-Jun-23",
     "location": "united-states"
    },
    {
     "Column1": 13,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "united-states"
    },
    {
     "Column1": 14,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "united-states"
    },
    {
     "Column1": 15,
     "title": "GREAT Scholarship for Bangladesh Students in UK",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 16,
     "title": "Diversity Scholarships for Africa and Latin American Students in UK",
     "degrees": "Master",
     "funds": "50% scholarship",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 17,
     "title": "Beth Mead Scholarships for International Students at Teesside University",
     "degrees": "Bachelor, Master",
     "funds": "Â£1,200",
     "date": "31-Aug-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 18,
     "title": "Malaysia Scholarships at Nottingham Trent University",
     "degrees": "Master",
     "funds": "Â£4,000",
     "date": "29-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 19,
     "title": "PhD Studentships in Predictive Uncertainty in Computer Vision for International Students in UK",
     "degrees": "Master",
     "funds": "Â£16,062 p.a., tuition fees + Â£2,000 research grant",
     "date": "10-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 21,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 22,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 23,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 24,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 25,
     "title": "Engineering: Fully Funded MSc by Research at Swansea: Functional Construction Materials",
     "degrees": "Master",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "27-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 26,
     "title": "UEA Law School Country Specific Academic Excellence Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£8,000 tuition fee reduction",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 27,
     "title": "Saraswati Dalmia Scholarship at SOAS University of London",
     "degrees": "Phd, Master",
     "funds": "Up to Â£5,353",
     "date": "02-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 28,
     "title": "The Professor Mike Walker OBE Scholarships for International Students in the UK",
     "degrees": "Master",
     "funds": "Up to Â£12,000 tuition fee reduction",
     "date": "11-Jul-22",
     "location": "united-kingdom"
    },

    {
     "Column1": 30,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 31,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "canada"
    },
    {
     "Column1": 32,
     "title": "Improve Menâ€™s Health Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$2000",
     "date": "31-May-22",
     "location": "canada"
    },
    {
     "Column1": 33,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "canada"
    },
    {
     "Column1": 34,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 35,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "canada"
    },
    {
     "Column1": 36,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "canada"
    },
    {
     "Column1": 37,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "canada"
    },
    {
     "Column1": 38,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "canada"
    },
    {
     "Column1": 39,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "canada"
    },
    {
     "Column1": 40,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "canada"
    },
    {
     "Column1": 41,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "canada"
    },
    {
     "Column1": 42,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "canada"
    },
    {
     "Column1": 43,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "canada"
    },
    {
     "Column1": 44,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "canada"
    },
    {
     "Column1": 45,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 46,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "europe"
    },
    {
     "Column1": 47,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "europe"
    },
    {
     "Column1": 48,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 49,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "europe"
    },
    {
     "Column1": 50,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "europe"
    },
    {
     "Column1": 51,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "europe"
    },
    {
     "Column1": 52,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "europe"
    },
    {
     "Column1": 53,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "europe"
    },
    {
     "Column1": 54,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "europe"
    },
    {
     "Column1": 55,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "europe"
    },
    {
     "Column1": 56,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "europe"
    },
    {
     "Column1": 57,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "europe"
    },
    {
     "Column1": 58,
     "title": "Becas Grisart 2022",
     "degrees": "Course",
     "funds": "Take the courses free of charge.",
     "date": "25-May-22",
     "location": "europe"
    },
    {
     "Column1": 59,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "europe"
    },
    {
     "Column1": 60,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 61,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "south-africa"
    },
    {
     "Column1": 62,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "south-africa"
    },
    {
     "Column1": 63,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 64,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "south-africa"
    },
    {
     "Column1": 65,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "south-africa"
    },
    {
     "Column1": 66,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "south-africa"
    },
    {
     "Column1": 67,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "south-africa"
    },
    {
     "Column1": 68,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "south-africa"
    },
    {
     "Column1": 69,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "south-africa"
    },
    {
     "Column1": 70,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "south-africa"
    },
    {
     "Column1": 71,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "south-africa"
    },
    {
     "Column1": 72,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "south-africa"
    },
    {
     "Column1": 73,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "south-africa"
    },
    {
     "Column1": 74,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "south-africa"
    },
    {
     "Column1": 75,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 76,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "nigeria"
    },
    {
     "Column1": 77,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "nigeria"
    },
    {
     "Column1": 78,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 79,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "nigeria"
    },
    {
     "Column1": 80,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "nigeria"
    },
    {
     "Column1": 81,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "nigeria"
    },
    {
     "Column1": 82,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "nigeria"
    },
    {
     "Column1": 83,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "nigeria"
    },
    {
     "Column1": 84,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "nigeria"
    },
    {
     "Column1": 85,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "nigeria"
    },
    {
     "Column1": 86,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "nigeria"
    },
    {
     "Column1": 87,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "nigeria"
    },
    {
     "Column1": 88,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "nigeria"
    },
    {
     "Column1": 89,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "nigeria"
    },
    {
     "Column1": 90,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 91,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "pakistan"
    },
    {
     "Column1": 92,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "pakistan"
    },
    {
     "Column1": 93,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 94,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "pakistan"
    },
    {
     "Column1": 95,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "pakistan"
    },
    {
     "Column1": 96,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "pakistan"
    },
    {
     "Column1": 97,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "pakistan"
    },
    {
     "Column1": 98,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "pakistan"
    },
    {
     "Column1": 99,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "pakistan"
    },
    {
     "Column1": 100,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "pakistan"
    },
    {
     "Column1": 101,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "pakistan"
    },
    {
     "Column1": 102,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "pakistan"
    },
    {
     "Column1": 103,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "pakistan"
    },
    {
     "Column1": 104,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "pakistan"
    },
    {
     "Column1": 105,
     "title": "International Students Diversity Contest 2022-2023",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Up to $2,000",
     "date": "22-Dec-22",
     "location": "india"
    },
    {
     "Column1": 106,
     "title": "Master in Business Administration 80% OFF your Tuition fee",
     "degrees": "Master",
     "funds": "80% Tuition Fees",
     "date": "15-Sep-22",
     "location": "india"
    },
    {
     "Column1": 107,
     "title": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
     "degrees": "Course",
     "funds": "$1455",
     "date": "01-Jul-22",
     "location": "india"
    },
    {
     "Column1": 108,
     "title": "ArtUniverse",
     "degrees": "Master, Course",
     "funds": "Full or partial scholarship",
     "date": "30-Dec-22",
     "location": "india"
    },
    {
     "Column1": 109,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "india"
    },
    {
     "Column1": 110,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "india"
    },
    {
     "Column1": 111,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "india"
    },
    {
     "Column1": 112,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "india"
    },
    {
     "Column1": 113,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "india"
    },
    {
     "Column1": 114,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "india"
    },
    {
     "Column1": 115,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "india"
    },
    {
     "Column1": 116,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "india"
    },
    {
     "Column1": 117,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "india"
    },
    {
     "Column1": 118,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "india"
    },
    {
     "Column1": 119,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "india"
    },
    {
     "Column1": 120,
     "title": "LSA International Student Scholarships at Regents of the University of Michigan in USA",
     "degrees": "Bachelor",
     "funds": "Up to $10,000",
     "location": "united-states"
    },
    {
     "Column1": 121,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "united-states"
    },
    {
     "Column1": 122,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "united-states"
    },
    {
     "Column1": 123,
     "title": "NLU Direct to Success Transfer Student Scholarship",
     "degrees": "Bachelor",
     "funds": "25% Tuition Rate",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 124,
     "title": "Kendell College at NLU International Opportunity Scholarship",
     "degrees": "Bachelor",
     "funds": "25% of the full-time tuition rate",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 125,
     "title": "NLU International Fresh Start Scholarship",
     "degrees": "Bachelor",
     "funds": "44% tuition fee",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 126,
     "title": "National Louis University #YouAreWelcomeHere Scholarship",
     "degrees": "Bachelor",
     "funds": "50% of full-time tuition",
     "date": "12-Jul-22",
     "location": "united-states"
    },
    {
     "Column1": 127,
     "title": "NLU Alumni Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15% Tuition Fee",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 128,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "united-states"
    },
    {
     "Column1": 129,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "united-states"
    },
    {
     "Column1": 130,
     "title": "Tiffin University International Trustee Scholarships in USA",
     "degrees": "Bachelor",
     "funds": "$16,000",
     "date": "15-Jul-22",
     "location": "united-states"
    },
    {
     "Column1": 131,
     "title": "Tiffin University International President Scholarships in USA",
     "degrees": "Bachelor",
     "funds": "$14,000",
     "date": "15-Jul-22",
     "location": "united-states"
    },
    {
     "Column1": 132,
     "title": "Graduate International Scholarships at University of Central Oklahoma",
     "degrees": "Master",
     "funds": "Up to $2,000 ($1,000 per year)",
     "date": "31-May-22",
     "location": "united-states"
    },
    {
     "Column1": 133,
     "title": "International Opportunity Awards at Texas A&M University",
     "degrees": "Bachelor",
     "funds": "$100 to $15,000 p\/a",
     "date": "01-Aug-22",
     "location": "united-states"
    },
    {
     "Column1": 134,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "united-states"
    },
    {
     "Column1": 135,
     "title": "Global Voices Scholarships at University of East Anglia",
     "degrees": "Master",
     "funds": "Â£20,000",
     "date": "03-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 136,
     "title": "Postgraduate International Development Scholarships for Sub Saharan African Students in UK",
     "degrees": "Master",
     "funds": "Â£8,000",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 137,
     "title": "Goodenough Scholarships",
     "degrees": "Master",
     "funds": "Up to Â£12,000",
     "date": "01-Jan-23",
     "location": "united-kingdom"
    },
    {
     "Column1": 138,
     "title": "International Contest for Students Support 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "28-Apr-23",
     "location": "united-kingdom"
    },
    {
     "Column1": 139,
     "title": "Scholarships for Africa",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$100 to $3000",
     "date": "24-Mar-27",
     "location": "united-kingdom"
    },
    {
     "Column1": 140,
     "title": "LAPTOP Scholarships - study Supply Chains",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "up to $3000",
     "date": "06-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 141,
     "title": "Sports Science: Fully Funded Swansea \/ DSTL PhD: Human response to prolonged heat exposure",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "25-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 142,
     "title": "Medicine: Fully Funded Swansea & HMRI PhD Scholarship: Ovarian Cancer Chemoresistance",
     "degrees": "Phd",
     "funds": "Full cost of tuition fees and an annual stipend",
     "date": "06-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 143,
     "title": "Nanotechnology: Fully Funded Swansea University and European Commission PhD",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "04-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 144,
     "title": "Materials Engineering: Fully Funded Swansea University and CISM PhD: Advanced Dielectrics",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "06-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 145,
     "title": "Sanctuary Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "Full-fee and Â£10,000 a year towards study costs",
     "date": "09-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 146,
     "title": "Dean's International Excellence Scholarship",
     "degrees": "Master",
     "funds": "Full-fee",
     "location": "united-kingdom"
    },
    {
     "Column1": 147,
     "title": "Dean's UK Excellence Scholarship",
     "degrees": "Master",
     "funds": "100% of fees",
     "date": "31-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 148,
     "title": "Masters Excellence Scholarship",
     "degrees": "Master",
     "funds": "50% of fees",
     "date": "30-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 149,
     "title": "TKS Full-Ride Scholarship",
     "degrees": "Course",
     "funds": "100% Tuition Fee [value of $6,000+]",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 150,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "canada"
    },
    {
     "Column1": 151,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 152,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "canada"
    },
    {
     "Column1": 153,
     "title": "John and Lena Graham Commonwealth Bursary at Dalhousie University",
     "degrees": "Phd, Master",
     "funds": "At least $2,000",
     "date": "31-Oct-22",
     "location": "canada"
    },
    {
     "Column1": 154,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "canada"
    },
    {
     "Column1": 155,
     "title": "Excellence Scholarships for African Students Studying in English",
     "degrees": "Bachelor",
     "funds": "$17,500 - $25,000 tuition fee reduction",
     "location": "canada"
    },
    {
     "Column1": 156,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 157,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "canada"
    },
    {
     "Column1": 158,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 159,
     "title": "Brock University Emerging Market Entrance International Awards",
     "degrees": "Bachelor",
     "funds": "$2,500",
     "location": "canada"
    },
    {
     "Column1": 160,
     "title": "UBC International Talent Scholarships in Canada",
     "degrees": "Master",
     "funds": "$10,000 - $30,000",
     "date": "05-Jun-22",
     "location": "canada"
    },
    {
     "Column1": 161,
     "title": "P.E.O. International Scholar Awards",
     "degrees": "Phd",
     "funds": "$20,000",
     "location": "canada"
    },
    {
     "Column1": 162,
     "title": "Ted Rogers School Graduate Entrance Scholarships for International Students at Ryerson University",
     "degrees": "Master",
     "funds": "$20,000",
     "location": "canada"
    },
    {
     "Column1": 163,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "canada"
    },
    {
     "Column1": 164,
     "title": "Entrance international awards at LaSalle College Vancouver",
     "degrees": "Master, Bachelor",
     "funds": "Up to $10,000",
     "location": "canada"
    },
    {
     "Column1": 165,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "europe"
    },
    {
     "Column1": 166,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 167,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "europe"
    },
    {
     "Column1": 168,
     "title": "Anonymous Hope Fund",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "15-Jan-26",
     "location": "europe"
    },
    {
     "Column1": 169,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "europe"
    },
    {
     "Column1": 170,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 171,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "europe"
    },
    {
     "Column1": 172,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 173,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "europe"
    },
    {
     "Column1": 174,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 175,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 176,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 177,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "europe"
    },
    {
     "Column1": 178,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "europe"
    },
    {
     "Column1": 179,
     "title": "KDS Competition Scholarship 2021",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "europe"
    },
    {
     "Column1": 180,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 181,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "south-africa"
    },
    {
     "Column1": 182,
     "title": "Anonymous Hope Fund",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "15-Jan-26",
     "location": "south-africa"
    },
    {
     "Column1": 183,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "south-africa"
    },
    {
     "Column1": 184,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 185,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "south-africa"
    },
    {
     "Column1": 186,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 187,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "south-africa"
    },
    {
     "Column1": 188,
     "title": "UFIC Diane Fisher Awards for International Students in USA",
     "degrees": "Bachelor",
     "location": "south-africa"
    },
    {
     "Column1": 189,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 190,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 191,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "south-africa"
    },
    {
     "Column1": 192,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "south-africa"
    },
    {
     "Column1": 193,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "south-africa"
    },
    {
     "Column1": 194,
     "title": "Thomas A Plein Endowed funding for International Students at University of Queensland",
     "degrees": "Bachelor",
     "location": "south-africa"
    },
    {
     "Column1": 195,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 196,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "nigeria"
    },
    {
     "Column1": 197,
     "title": "Anonymous Hope Fund",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "15-Jan-26",
     "location": "nigeria"
    },
    {
     "Column1": 198,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "nigeria"
    },
    {
     "Column1": 199,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 200,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "nigeria"
    },
    {
     "Column1": 201,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 202,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "nigeria"
    },
    {
     "Column1": 203,
     "title": "UFIC Diane Fisher Awards for International Students in USA",
     "degrees": "Bachelor",
     "location": "nigeria"
    },
    {
     "Column1": 204,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 205,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 206,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "nigeria"
    },
    {
     "Column1": 207,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "nigeria"
    },
    {
     "Column1": 208,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "nigeria"
    },
    {
     "Column1": 209,
     "title": "Thomas A Plein Endowed funding for International Students at University of Queensland",
     "degrees": "Bachelor",
     "location": "nigeria"
    },
    {
     "Column1": 210,
     "title": "PEEF Scholarships",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "Tuition fees and basic expenses",
     "date": "28-Feb-00",
     "location": "pakistan"
    },
    {
     "Column1": 211,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 212,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "pakistan"
    },
    {
     "Column1": 213,
     "title": "Anonymous Hope Fund",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "15-Jan-26",
     "location": "pakistan"
    },
    {
     "Column1": 214,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "pakistan"
    },
    {
     "Column1": 215,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 216,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "pakistan"
    },
    {
     "Column1": 217,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 218,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "pakistan"
    },
    {
     "Column1": 219,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 220,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 221,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "pakistan"
    },
    {
     "Column1": 222,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "pakistan"
    },
    {
     "Column1": 223,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "pakistan"
    },
    {
     "Column1": 224,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "pakistan"
    },
    {
     "Column1": 225,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "india"
    },
    {
     "Column1": 226,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "india"
    },
    {
     "Column1": 227,
     "title": "Anonymous Hope Fund",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "15-Jan-26",
     "location": "india"
    },
    {
     "Column1": 228,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "india"
    },
    {
     "Column1": 229,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "india"
    },
    {
     "Column1": 230,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "india"
    },
    {
     "Column1": 231,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "india"
    },
    {
     "Column1": 232,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "india"
    },
    {
     "Column1": 233,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "india"
    },
    {
     "Column1": 234,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "india"
    },
    {
     "Column1": 235,
     "title": "50% scholarship for students based in India - University of Essex Online",
     "degrees": "Master, Bachelor, Course",
     "funds": "50% scholarship for all courses",
     "date": "21-Jul-22",
     "location": "india"
    },
    {
     "Column1": 236,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "india"
    },
    {
     "Column1": 237,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "india"
    },
    {
     "Column1": 238,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "india"
    },
    {
     "Column1": 239,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "india"
    },
    {
     "Column1": 240,
     "title": "CalArts Merit Scholarships for International Students in USA",
     "degrees": "Bachelor, Master",
     "funds": "$10,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 241,
     "title": "International Merit-Based Scholarships at Valparaiso University",
     "degrees": "Bachelor",
     "funds": "Financial aid",
     "location": "united-states"
    },
    {
     "Column1": 242,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "united-states"
    },
    {
     "Column1": 243,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 244,
     "title": "E-waste Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "location": "united-states"
    },
    {
     "Column1": 245,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "united-states"
    },
    {
     "Column1": 246,
     "title": "Orangesoft Women in Technology Scholarship Program",
     "degrees": "Master, Bachelor",
     "funds": "$1,000",
     "date": "31-Oct-22",
     "location": "united-states"
    },
    {
     "Column1": 247,
     "title": "International Graduate Scholarships in USA",
     "degrees": "Master",
     "funds": "Up to $2,000",
     "location": "united-states"
    },
    {
     "Column1": 248,
     "title": "LCBAS and Applied Sciences International Merit Awards in USA",
     "degrees": "Bachelor, Master",
     "funds": "$1,500",
     "date": "01-May-22",
     "location": "united-states"
    },
    {
     "Column1": 249,
     "title": "International Student Scholarships at Castleton University",
     "degrees": "Bachelor",
     "funds": "Up to $2,500 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 250,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "united-states"
    },
    {
     "Column1": 251,
     "title": "Assisi Academic Scholarships for International Students at Marian University",
     "degrees": "Bachelor",
     "funds": "$8,000",
     "location": "united-states"
    },
    {
     "Column1": 252,
     "title": "International Scholarships at Lake Region State College",
     "degrees": "Bachelor, Master",
     "funds": "50% off tuition fees",
     "location": "united-states"
    },
    {
     "Column1": 253,
     "title": "Merit-Based Scholarships for International Students at Hartwick College",
     "degrees": "Bachelor, Master",
     "funds": "$15,000 - $28,000 p.a.",
     "date": "01-Oct-22",
     "location": "united-states"
    },
    {
     "Column1": 254,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 255,
     "title": "Five scholarships of up to US$3000 for supply chain courses",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "06-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 256,
     "title": "University of Sussex International PhD Studentships in Mind and Material Culture",
     "degrees": "Phd",
     "funds": "Tuition fee, Â£15,609 p.a. + Â£2,000 research grant",
     "date": "10-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 257,
     "title": "University of East Anglia Nigeria Awards in UK",
     "degrees": "Master",
     "funds": "Up to Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 258,
     "title": "International Women in Business Scholarships at Queen Mary University of London",
     "degrees": "Bachelor",
     "funds": "Â£4,000",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 259,
     "title": "Deanâ€™s International Bursary in Faculty of Arts",
     "degrees": "Bachelor",
     "funds": "Â£1,000 p.a. for two years",
     "date": "30-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 260,
     "title": "Lancashire School of Business and Enterprise PhD Studentships in UK",
     "degrees": "Phd",
     "funds": "Tuition fees + Â£15,609 p.a.",
     "date": "30-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 261,
     "title": "Kolade Scholarships for International Students at University of Exeter Business School",
     "degrees": "Master",
     "funds": "Â£12,500",
     "date": "30-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 262,
     "title": "Global Excellence Scholarships at Queen Mary University of London",
     "degrees": "Master",
     "funds": "Â£2,000",
     "date": "02-Sep-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 263,
     "title": "Niloufar Ebrahim Scholarships for International Students at Kingston University London",
     "degrees": "Master",
     "funds": "Up to Â£11,100.",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 264,
     "title": "University of Manchester Merit-based Masterâ€™s International Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£6,000",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 265,
     "title": "Medical Engineering: Fully Funded EPSRC PhD Scholarship: AI approaches to cell imaging data",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "03-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 266,
     "title": "Biosciences: Fully Funded PhD Scholarship at Swansea: Seagrass Restoration",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "06-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 267,
     "title": "International No-Essay Support Competition Scholarships 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "20-Jan-23",
     "location": "united-kingdom"
    },
    {
     "Column1": 268,
     "title": "THGM MUSE Scholarship",
     "degrees": "Bachelor",
     "funds": "US$500 or C$630",
     "date": "15-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 269,
     "title": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
     "degrees": "Master",
     "funds": "80% off tuition fee",
     "date": "15-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 270,
     "title": "Silver Anniversary Recruitment Graduate International Fellowships in Canada",
     "degrees": "Phd",
     "funds": "$20,000",
     "location": "canada"
    },
    {
     "Column1": 271,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 272,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 273,
     "title": "Mehran Bibi Sheikh Memorial Entrance Scholarships for International Students at Queenâ€™s University",
     "degrees": "Bachelor",
     "funds": "$1,500",
     "location": "canada"
    },
    {
     "Column1": 274,
     "title": "Engineering International Student Entrance Scholarships at University of Waterloo",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "canada"
    },
    {
     "Column1": 275,
     "title": "Caribbean Scholarships at Niagara College",
     "degrees": "Bachelor",
     "funds": "$2,000",
     "location": "canada"
    },
    {
     "Column1": 276,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 277,
     "title": "University of Waterloo Graduate international awards in Canada",
     "degrees": "Master, Phd",
     "funds": "Up to $3,000",
     "location": "canada"
    },
    {
     "Column1": 278,
     "title": "Regional Graduate Program Entrance Scholarships for International Students at Conestoga College",
     "degrees": "Master",
     "funds": "$1,500",
     "location": "canada"
    },
    {
     "Column1": 279,
     "title": "HEC MontrÃ©al MSc Entrance international awards in Canada",
     "degrees": "Master",
     "funds": "$5,000",
     "location": "canada"
    },
    {
     "Column1": 280,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "canada"
    },
    {
     "Column1": 281,
     "title": "English Proficiency Entrance Scholarships for International Students at Durham College",
     "degrees": "Bachelor",
     "funds": "Up to $1,500",
     "location": "canada"
    },
    {
     "Column1": 282,
     "title": "B.C. Access Grants in Canada",
     "degrees": "Bachelor",
     "funds": "Up to $4,000 p.a.",
     "location": "canada"
    },
    {
     "Column1": 283,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "canada"
    },
    {
     "Column1": 284,
     "title": "Differential Tuition Fee Exemption international awards at University of Ottawa",
     "degrees": "Master, Bachelor",
     "funds": "Variable",
     "location": "canada"
    },
    {
     "Column1": 285,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "europe"
    },
    {
     "Column1": 286,
     "title": "FindDataLab Research Grant Programme in USA and EU",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to $1,000 towards web scraping serivces",
     "location": "europe"
    },
    {
     "Column1": 287,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "europe"
    },
    {
     "Column1": 288,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "europe"
    },
    {
     "Column1": 289,
     "title": "Scholarship for Online Learner at IU International University of Applied Sciences â€“ Online",
     "degrees": "Master, Bachelor",
     "funds": "Up to â‚¬ 13.000",
     "location": "europe"
    },
    {
     "Column1": 290,
     "title": "Scholarship for Academics at IU International University of Applied Sciences â€“ Online",
     "degrees": "Master, Bachelor",
     "funds": "up to â‚¬13.000",
     "location": "europe"
    },
    {
     "Column1": 291,
     "title": "Scholarship for Future Entrepreneur at IU International University of Applied Sciences - Online",
     "degrees": "Master, Bachelor",
     "funds": "not specified",
     "location": "europe"
    },
    {
     "Column1": 292,
     "title": "Scholarship for STEM\/MINT Professionals at IU International University of Applied Sciences - Online",
     "degrees": "Master, Bachelor",
     "funds": "Up to â‚¬13.000",
     "location": "europe"
    },
    {
     "Column1": 293,
     "title": "Scholarship for Women in Leadership and Management at IU International University of Applied Sciences - Online",
     "degrees": "Master, Bachelor",
     "funds": "Up to â‚¬13.000",
     "location": "europe"
    },
    {
     "Column1": 294,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "europe"
    },
    {
     "Column1": 295,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "europe"
    },
    {
     "Column1": 296,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 297,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 298,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 299,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 300,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "south-africa"
    },
    {
     "Column1": 301,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "south-africa"
    },
    {
     "Column1": 302,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "south-africa"
    },
    {
     "Column1": 303,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "south-africa"
    },
    {
     "Column1": 304,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "south-africa"
    },
    {
     "Column1": 305,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 306,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 307,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 308,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 309,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 310,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 311,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 312,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 313,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 314,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 315,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "nigeria"
    },
    {
     "Column1": 316,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "nigeria"
    },
    {
     "Column1": 317,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "nigeria"
    },
    {
     "Column1": 318,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "nigeria"
    },
    {
     "Column1": 319,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "nigeria"
    },
    {
     "Column1": 320,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 321,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 322,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 323,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 324,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 325,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 326,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 327,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 328,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 329,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 330,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "pakistan"
    },
    {
     "Column1": 331,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "pakistan"
    },
    {
     "Column1": 332,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "pakistan"
    },
    {
     "Column1": 333,
     "title": "Scholarships at the Superior College in Pakistan",
     "degrees": "Bachelor, Master",
     "funds": "The sponsorship will provide the educational fund for your studies.",
     "location": "pakistan"
    },
    {
     "Column1": 334,
     "title": "April 2019 -Scholarship Application Open! Faculty of Global Studies",
     "degrees": "Bachelor",
     "funds": "30-100% tuition fee",
     "location": "pakistan"
    },
    {
     "Column1": 335,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "pakistan"
    },
    {
     "Column1": 336,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 337,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 338,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 339,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 340,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 341,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 342,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 343,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 344,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 345,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "india"
    },
    {
     "Column1": 346,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "india"
    },
    {
     "Column1": 347,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "india"
    },
    {
     "Column1": 348,
     "title": "April 2019 -Scholarship Application Open! Faculty of Global Studies",
     "degrees": "Bachelor",
     "funds": "30-100% tuition fee",
     "location": "india"
    },
    {
     "Column1": 349,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "india"
    },
    {
     "Column1": 350,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 351,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 352,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 353,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 354,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 355,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 356,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 357,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 358,
     "title": "Visiting Student Program (VSP) - Raman Research Institute",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 359,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 360,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "united-states"
    },
    {
     "Column1": 361,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 362,
     "title": "Academic Scholar- Distinction International Awards in USA",
     "degrees": "Bachelor",
     "funds": "$500 + tuition fee reduction",
     "date": "15-Oct-22",
     "location": "united-states"
    },
    {
     "Column1": 363,
     "title": "CS\/IS International Graduate Achievement Scholarships in USA",
     "degrees": "Master",
     "funds": "$500",
     "date": "01-Nov-22",
     "location": "united-states"
    },
    {
     "Column1": 364,
     "title": "Leaders of Tomorrow international awards in USA",
     "degrees": "Bachelor",
     "funds": "$33,000 ($8,250 p.a.)",
     "date": "01-May-22",
     "location": "united-states"
    },
    {
     "Column1": 365,
     "title": "P.E.O. International Scholar Awards",
     "degrees": "Phd",
     "funds": "$20,000",
     "location": "united-states"
    },
    {
     "Column1": 366,
     "title": "VCU Out-of-State Scholarships in the USA",
     "degrees": "Bachelor",
     "funds": "$7,500",
     "location": "united-states"
    },
    {
     "Column1": 367,
     "title": "Future Leaders in Tech Scholarship",
     "degrees": "Bachelor",
     "funds": "$20,000",
     "date": "19-Aug-22",
     "location": "united-states"
    },
    {
     "Column1": 368,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "united-states"
    },
    {
     "Column1": 369,
     "title": "INTO SLU Undergraduate Regional Scholarships at Saint Louis University",
     "degrees": "Bachelor",
     "funds": "$500 - $15,000",
     "location": "united-states"
    },
    {
     "Column1": 370,
     "title": "North Central College International Honors Scholarship in USA",
     "degrees": "Bachelor",
     "funds": "$27,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 371,
     "title": "Global Citizen Scholarships at Saint Leo University",
     "degrees": "Bachelor",
     "funds": "$3,000",
     "location": "united-states"
    },
    {
     "Column1": 372,
     "title": "International Presidential Scholarships at North Central College",
     "degrees": "Bachelor",
     "funds": "$29,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 373,
     "title": "OAS Scholarships for International Students at Marconi International University",
     "degrees": "Master, Bachelor",
     "funds": "55% of tuition fees",
     "location": "united-states"
    },
    {
     "Column1": 374,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 375,
     "title": "Engineering: Fully Funded EPSRC PhD Scholarship at Swansea University: solid-state batteries",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "26-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 376,
     "title": "International Students Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "30-Jun-23",
     "location": "united-kingdom"
    },
    {
     "Column1": 377,
     "title": "Becas Grisart 2022",
     "degrees": "Course",
     "funds": "Take the courses free of charge.",
     "date": "25-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 378,
     "title": "BLACA Awards for International Students in UK",
     "degrees": "Master",
     "funds": "Up to Â£9,000 towards tuition fees",
     "date": "01-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 379,
     "title": "GREAT Scholarships for International Students at University of York",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "27-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 380,
     "title": "University of Exeter Business School Online International Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£5,000 or Â£750",
     "date": "12-Sep-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 381,
     "title": "Postgraduate Taught International Scholarships at Hull York Medical School",
     "degrees": "Master",
     "funds": " 5% fee reduction",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 382,
     "title": "Human Resource (HR) - Free Course From Windsor University's MBA",
     "degrees": "Master, Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 383,
     "title": "Maths and Physics Undergraduate International Scholarships in UK",
     "degrees": "Bachelor",
     "funds": "Â£5,000",
     "date": "31-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 384,
     "title": "Postgraduate International Development Scholarships for South Korea Students",
     "degrees": "Master",
     "funds": "Â£6,000",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 385,
     "title": "Computer Science Scholarships for International Students in UK",
     "degrees": "Master",
     "funds": "Â£2,000 or Â£4,000 tuition fee discount.",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 386,
     "title": "African & Caribbean Excellence Awards at University of Glasgow",
     "degrees": "Master",
     "funds": "Full tuition fee waiver",
     "location": "united-kingdom"
    },
    {
     "Column1": 387,
     "title": "Project Management - Free Course From Windsor University's MBA",
     "degrees": "Course",
     "funds": "100% free",
     "date": "14-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 388,
     "title": "Global No-Essay Contest Scholarships for International Students 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000 awards",
     "date": "31-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 389,
     "title": "Engineering: Fully Funded PhD at Swansea: Capture and reduction of carbon emissions",
     "degrees": "Phd",
     "funds": "Full cost of tuition fees and an annual stipend",
     "date": "02-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 390,
     "title": "Entrance international awards at Sault College",
     "degrees": "Master, Bachelor",
     "funds": "Up to $4,000",
     "location": "canada"
    },
    {
     "Column1": 391,
     "title": "International Entrance Scholarships at Memorial University of Newfoundland",
     "degrees": "Bachelor",
     "funds": "$4,400",
     "location": "canada"
    },
    {
     "Column1": 392,
     "title": "International Postdoctoral Positions in Clinical Neurosciences",
     "degrees": "Phd",
     "funds": "$55,000 p.a. + benefits",
     "location": "canada"
    },
    {
     "Column1": 393,
     "title": "McMaster University Award of Excellence in Canada",
     "degrees": "Bachelor",
     "funds": "$3,000",
     "location": "canada"
    },
    {
     "Column1": 394,
     "title": "KDS Competition Scholarship 2021",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 395,
     "title": "University Canada West Americas Tuition Awards in Canada",
     "degrees": "Master, Bachelor",
     "funds": "Discounted courses",
     "location": "canada"
    },
    {
     "Column1": 396,
     "title": "University Canada West Second Language Excellence international awards",
     "degrees": "Bachelor, Master",
     "funds": "Up to $8,000",
     "location": "canada"
    },
    {
     "Column1": 397,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "canada"
    },
    {
     "Column1": 398,
     "title": "Deanâ€™s Circle ESB International Student Awards in Canada",
     "degrees": "Bachelor",
     "funds": "$5,000",
     "location": "canada"
    },
    {
     "Column1": 399,
     "title": "University of Waterloo Arthur F. Church Mechanical Engineering international awards",
     "degrees": "Bachelor",
     "funds": "Up to $5,000",
     "location": "canada"
    },
    {
     "Column1": 400,
     "title": "University of Ottawa International Admission Doctorate Scholarships in Canada",
     "degrees": "Phd",
     "funds": "$9,000 p.a.",
     "location": "canada"
    },
    {
     "Column1": 401,
     "title": "Emerging Market Entrance Awards for International Students at Brock University",
     "degrees": "Bachelor",
     "funds": "$1,000-$4,000",
     "location": "canada"
    },
    {
     "Column1": 402,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "canada"
    },
    {
     "Column1": 403,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "canada"
    },
    {
     "Column1": 404,
     "title": "One-year Entrance Scholarships at McGill University",
     "degrees": "Bachelor",
     "funds": "$12,000",
     "location": "canada"
    },
    {
     "Column1": 405,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 406,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 407,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 408,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 409,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 410,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 411,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 412,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 413,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 414,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 415,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 416,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 417,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 418,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 419,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 420,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 421,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 422,
     "title": "SAIIA Bradlow Fellowship Programme",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 423,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 424,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 425,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 426,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 427,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 428,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 429,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 430,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 431,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "south-africa"
    },
    {
     "Column1": 432,
     "title": "DRD Scholarships for Sub-Saharan Africans",
     "location": "south-africa"
    },
    {
     "Column1": 433,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 434,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 435,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 436,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 437,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 438,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 439,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 440,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 441,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 442,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 443,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "nigeria"
    },
    {
     "Column1": 444,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 445,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 446,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 447,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 448,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 449,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 450,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 451,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 452,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 453,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 454,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 455,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "pakistan"
    },
    {
     "Column1": 456,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 457,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 458,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 459,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 460,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 461,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 462,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 463,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 464,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 465,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 466,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 467,
     "title": "The Indian Technical and Economic Cooperation (ITEC) Programme",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 468,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "india"
    },
    {
     "Column1": 469,
     "title": "Wichita International Student Hardship Fund in the United States",
     "degrees": "Bachelor",
     "funds": "Up to $1,000",
     "location": "united-states"
    },
    {
     "Column1": 470,
     "title": "merit awards for International Students at Columbia College",
     "degrees": "Bachelor",
     "funds": "Up to $12,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 471,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 472,
     "title": "Meistersinger music awards for International Students at Wartburg College",
     "degrees": "Bachelor",
     "funds": "Up to $5,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 473,
     "title": "Musicians Institute Musicianship international awards in USA",
     "degrees": "Bachelor",
     "funds": "$1,000",
     "location": "united-states"
    },
    {
     "Column1": 474,
     "title": "Merit-Based Scholarships for International Students at St. Francis College",
     "degrees": "Bachelor",
     "funds": "Up to $7,500",
     "location": "united-states"
    },
    {
     "Column1": 475,
     "title": "College of Lake County International Student Scholarships in USA",
     "degrees": "Bachelor",
     "funds": "$1,000",
     "location": "united-states"
    },
    {
     "Column1": 476,
     "title": "Catherine T. McNamee International Student Scholarships in USA",
     "degrees": "Bachelor",
     "funds": "Up to $30,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 477,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 478,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "united-states"
    },
    {
     "Column1": 479,
     "title": "International Presidential Scholarships at Stratford University",
     "degrees": "Bachelor, Master",
     "funds": "25% tuition discount",
     "location": "united-states"
    },
    {
     "Column1": 480,
     "title": "International Opportunity Scholarships at National Louis University",
     "degrees": "Bachelor",
     "funds": "10% of the full-time tuition rate",
     "location": "united-states"
    },
    {
     "Column1": 481,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "united-states"
    },
    {
     "Column1": 482,
     "title": "John Barras DDS Autism Scholarships",
     "degrees": "Phd, Master, Bachelor, Course",
     "funds": "$1,000",
     "location": "united-states"
    },
    {
     "Column1": 483,
     "title": "Merit-Based Scholarships for International Students at Kalamazoo College",
     "degrees": "Bachelor",
     "funds": "$21,000-35,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 484,
     "title": "Sports Science: Fully Funded PhD at Swansea: The effect of mineral rich Algae",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "04-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 485,
     "title": "Physics: Fully Funded PhD Scholarship at Swansea: Photovoltaic Applications",
     "degrees": "Phd",
     "funds": "Full cost of UK tuition fees and an annual stipend",
     "date": "18-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 486,
     "title": "Eon Essay Contest on The Precipice",
     "degrees": "Master, Bachelor, Phd",
     "funds": "15,000 USD top prize; 42,000 USD total prizes",
     "date": "15-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 487,
     "title": "Anonymous Hope Fund",
     "degrees": "Master, Bachelor, Phd, Course",
     "funds": "$3000",
     "date": "15-Jan-26",
     "location": "united-kingdom"
    },
    {
     "Column1": 488,
     "title": "University of Sussex Hornsey Scholarship in UK",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "01-Aug-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 489,
     "title": "David Sainsbury Full MSc Scholarships for International Students in UK",
     "degrees": "Master",
     "funds": "Full tuition fees + Â£15,609 p.a. stipend",
     "date": "31-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 490,
     "title": "Think Big About Education International Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£5,000",
     "date": "13-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 491,
     "title": "Lebanon Bursaries at University of Warwick",
     "degrees": "Master",
     "funds": "25% tuition fee discount",
     "location": "united-kingdom"
    },
    {
     "Column1": 492,
     "title": "Chancellors International Business School Scholarships at University of Sussex",
     "degrees": "Bachelor",
     "funds": "Â£5,000 p.a.",
     "date": "01-Aug-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 493,
     "title": "Chancellors International Engineering and Informatics Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Â£5,000 p.a.",
     "date": "01-Aug-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 494,
     "title": "University of St Andrews EU Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£8,000",
     "date": "28-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 495,
     "title": "Blockchain in Business and Society International Scholarships",
     "degrees": "Master",
     "funds": "Â£15,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 496,
     "title": "GREAT Scholarships for International Students at Falmouth University",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 497,
     "title": "Intake Education Taiwan Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£2,000",
     "date": "31-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 498,
     "title": "INTO Progressors International Scholarships at Queenâ€™s University Belfast",
     "degrees": "Phd, Master, Bachelor",
     "funds": "10% of tuition fees",
     "date": "16-Sep-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 499,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "canada"
    },
    {
     "Column1": 500,
     "title": "Graduate Deanâ€™s Entrance Scholarship at University of British Columbia",
     "degrees": "Master",
     "funds": " $5,000",
     "location": "canada"
    },
    {
     "Column1": 501,
     "title": "International Scholarship Program (Firdaws Academy)",
     "degrees": "Course",
     "funds": 1,
     "date": "29-Dec-22",
     "location": "canada"
    },
    {
     "Column1": 502,
     "title": "MPOWER Global Citizen Scholarship",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fixed interest rates for amounts between $2,001.00 and $50,000.00",
     "location": "canada"
    },
    {
     "Column1": 503,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "canada"
    },
    {
     "Column1": 504,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 505,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 506,
     "title": "Centre for Studies in Religion and Society (CSRS) Visiting Research Fellowships",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 507,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 508,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 509,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 510,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 511,
     "title": "Konrad von Moltke Research Grants for the young researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 512,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 513,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 514,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 515,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "europe"
    },
    {
     "Column1": 516,
     "title": "KU Full-tuition International Excellence Awards in USA",
     "degrees": "Bachelor",
     "funds": "Up to a full tuition waiver ($25,000+\/year)",
     "location": "united-states"
    },
    {
     "Column1": 517,
     "title": "International Undergraduate Commitment Scholarships at Western Illinois University",
     "degrees": "Bachelor",
     "funds": "Up to $8,000",
     "location": "united-states"
    },
    {
     "Column1": 518,
     "title": "international awards at Anderson University",
     "degrees": "Bachelor",
     "funds": "Variable",
     "location": "united-states"
    },
    {
     "Column1": 519,
     "title": "International Student Emergency Relief Scholarships in USA",
     "degrees": "Bachelor",
     "funds": "Up to $1,000",
     "location": "united-states"
    },
    {
     "Column1": 520,
     "title": "KDS Competition Scholarship 2021",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 521,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "united-states"
    },
    {
     "Column1": 522,
     "title": "Graduate Studies international awards at University of Southern Maine",
     "degrees": "Master",
     "funds": "Up to $3,000",
     "location": "united-states"
    },
    {
     "Column1": 523,
     "title": "Charger Award for International Students at University of New Haven",
     "degrees": "Bachelor",
     "funds": "Up to $14,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 524,
     "title": "Freshman Scholarships for International Students at Wilkes University in USA",
     "degrees": "Bachelor",
     "funds": "$14,000 â€“ $21,000",
     "location": "united-states"
    },
    {
     "Column1": 525,
     "title": "Presidentâ€™s Entrance international awards at Ryerson University in Canada",
     "degrees": "Bachelor",
     "funds": "$40,000",
     "location": "united-states"
    },
    {
     "Column1": 526,
     "title": "John Foy & Associates Strong Arm Leukemia funding for International Students in USA",
     "degrees": "Bachelor, Master",
     "funds": "$1,000",
     "location": "united-states"
    },
    {
     "Column1": 527,
     "title": "James B. Duke Scholarships for International Students at Furman University",
     "degrees": "Bachelor, Master",
     "funds": "Full tuition + stipend",
     "location": "united-states"
    },
    {
     "Column1": 528,
     "title": "University of Findlay International Scholar Awards in USA",
     "degrees": "Bachelor",
     "funds": "Variable",
     "location": "united-states"
    },
    {
     "Column1": 529,
     "title": "Musicians Institute Melodic Soloing Guitar international awards in USA",
     "degrees": "Bachelor, Master",
     "funds": "$1,500",
     "location": "united-states"
    },
    {
     "Column1": 530,
     "title": "FindDataLab Research Grant Programme in USA and EU",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to $1,000 towards web scraping serivces",
     "location": "united-states"
    },
    {
     "Column1": 531,
     "title": "Mischon de Reya Scholarships for International Students at Queen Mary University of London",
     "degrees": "Master",
     "funds": "Full tuition fees",
     "date": "03-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 532,
     "title": "CU Group Undergraduate International Scholarships in UK",
     "degrees": "Bachelor",
     "funds": "Â£5,000",
     "date": "30-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 533,
     "title": "International Student Support Contest 2022-2023",
     "degrees": "Master, Bachelor, Course",
     "funds": "Multiple awards",
     "date": "31-Jan-23",
     "location": "united-kingdom"
    },
    {
     "Column1": 534,
     "title": "Department of Meteorology International PhD Scholarships in UK",
     "degrees": "Phd",
     "funds": "Up to Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 535,
     "title": "Postgraduate International Studentships in Marketing",
     "degrees": "Master",
     "funds": "Â£5,900",
     "date": "05-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 536,
     "title": "Online Islamic classes for kids",
     "degrees": "Course",
     "funds": "40% off over all of our Islamic courses",
     "date": "31-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 537,
     "title": "The Annual IELTS from 6 to 9 Scholarship",
     "degrees": "Master, Bachelor, Phd",
     "funds": "$1,000",
     "date": "01-Apr-23",
     "location": "united-kingdom"
    },
    {
     "Column1": 538,
     "title": "Scholarship for families want to learn Quran online",
     "degrees": "Course",
     "funds": "50% off over all of our Quran courses",
     "date": "31-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 539,
     "title": "African Scholarships at University of Essex",
     "degrees": "Master",
     "funds": "Â£4,500",
     "date": "16-Sep-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 540,
     "title": "GREAT Scholarships for Mexican Students at Queenâ€™s University Belfast",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "31-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 541,
     "title": "GREAT China Scholarships for Justice and Law",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 542,
     "title": "Great Scholarship for Chinese Students at University of Sussex",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "15-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 543,
     "title": "Warwick WMG Bursaries for Iranian Students in UK",
     "degrees": "Master",
     "funds": "25% of tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 544,
     "title": "International School Undergraduate Outstanding Achievement Scholarships in UK",
     "degrees": "Bachelor",
     "funds": "Â£2,500",
     "date": "27-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 545,
     "title": "University of Glasgow Angela Adams Scholarship 2022",
     "degrees": "Master",
     "funds": "Â£5,000",
     "date": "23-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 546,
     "title": "Mount Saint Vincent University - Graduate Student Scholarships",
     "degrees": "Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 547,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 548,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 549,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 550,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 551,
     "title": "McGill University - Entrance Law Scholarships",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 552,
     "title": "McGill University - Graduate Law Scholarships, funds and bursaries",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 553,
     "title": "University of Manitoba - Graduate Fellowship (UMGF)",
     "degrees": "Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 554,
     "title": "York University - International Entrance Scholarship",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 555,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 556,
     "title": "The Humane Studies Fellowship - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 557,
     "title": "IIASA Funded Postdoctoral Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 558,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 559,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 560,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 561,
     "title": "International Merit Awards at Culinary Institute of America",
     "degrees": "Course",
     "funds": "Tuition fee reduction.",
     "location": "united-states"
    },
    {
     "Column1": 562,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "united-states"
    },
    {
     "Column1": 563,
     "title": "Quran Learning Scholarship Program",
     "degrees": "Course",
     "funds": "Up to $300",
     "location": "united-states"
    },
    {
     "Column1": 564,
     "title": "Need-Based Grants for International Students in the United States",
     "degrees": "Bachelor",
     "funds": "Up to $10,000 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 565,
     "title": "Global Leader Scholarships in the USA",
     "degrees": "Bachelor",
     "funds": "approx. $10,656 p.a.",
     "location": "united-states"
    },
    {
     "Column1": 566,
     "title": "4WARD Graduation Scholarships for International Students",
     "degrees": "Bachelor",
     "funds": "50% of tuition over 4 years",
     "location": "united-states"
    },
    {
     "Column1": 567,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "united-states"
    },
    {
     "Column1": 568,
     "title": "International Merit Scholarship at University of Memphis",
     "degrees": "Bachelor, Master",
     "funds": "Varying award amount",
     "location": "united-states"
    },
    {
     "Column1": 569,
     "title": "$2,500 for Graduate School: GradCAS Breakthrough Scholarship",
     "degrees": "Master, Phd",
     "funds": "$2,500",
     "location": "united-states"
    },
    {
     "Column1": 570,
     "title": "$2,500 for Engineering Students: EngineeringCAS Breakthrough Scholarship",
     "degrees": "Master, Phd",
     "funds": "$2,500",
     "location": "united-states"
    },
    {
     "Column1": 571,
     "title": "$2,500 for Business School: BusinessCAS Breakthrough Scholarship",
     "degrees": "Master, Phd",
     "funds": "$2,500",
     "location": "united-states"
    },
    {
     "Column1": 572,
     "title": "Invitation to Idaho funding for International Students at University of Idaho",
     "degrees": "Bachelor",
     "funds": "$15,084",
     "location": "united-states"
    },
    {
     "Column1": 573,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "united-states"
    },
    {
     "Column1": 574,
     "title": "Carr Academic Scholarship",
     "degrees": "Bachelor",
     "funds": "$15,000",
     "location": "united-states"
    },
    {
     "Column1": 575,
     "title": "Global Scholars Program to Study at Babson College",
     "degrees": "Bachelor, Course",
     "funds": "full scholarship",
     "location": "united-states"
    },
    {
     "Column1": 576,
     "title": "University of Birmingham Bellerbys Outstanding Achievement International Scholarship in UK",
     "degrees": "Bachelor",
     "funds": "Â£2,500",
     "date": "27-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 577,
     "title": "GREAT Scholarships for Ghana Students at University of Warwick",
     "degrees": "Master",
     "funds": "Â£15,000",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 578,
     "title": "Great Scholarships for India and Singapore Students at University of Plymouth",
     "degrees": "Master",
     "funds": "Â£10,000",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 579,
     "title": "Latin American Taught Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£5,000",
     "date": "31-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 580,
     "title": "Advanced Chemical Engineering Professorâ€™s International Scholarship in UK",
     "degrees": "Master",
     "funds": "Up to Â£11,075",
     "date": "13-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 581,
     "title": "ULMS Indian Subcontinent Excellence Scholarships in UK",
     "degrees": "Master",
     "funds": "50% of tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 582,
     "title": "Sir Ray Tindle international awards at University of Creative Arts",
     "degrees": "Bachelor",
     "funds": "Â£1,000 p.a.",
     "date": "30-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 583,
     "title": "Great Scholarships for International Students at University of Derby",
     "degrees": "Master",
     "funds": "Â£11,000",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 584,
     "title": "UCA Creative Europe Scholarships in UK",
     "degrees": "Bachelor, Phd, Master",
     "funds": "Tuition fee reduction to UK home fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 585,
     "title": "UCA Nick Jack Scholarships for International Students in UK",
     "degrees": "Master",
     "funds": "Â£5,000",
     "date": "31-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 586,
     "title": "ULMS European Union Excellence Scholarships in UK",
     "degrees": "Master",
     "funds": "50% of tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 587,
     "title": "Aberystwyth University IBERS international awards in UK",
     "degrees": "Master",
     "funds": "40% tuition fee discount",
     "location": "united-kingdom"
    },
    {
     "Column1": 588,
     "title": "Contest Scholarship Programme for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 589,
     "title": "EU Grant Award at the University of Gloucestershire",
     "degrees": "Phd, Master, Bachelor",
     "funds": "Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 590,
     "title": "Robert Lethbridge international awards in Modern Language",
     "degrees": "Master",
     "funds": "Â£1,250",
     "date": "31-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 591,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 592,
     "title": "PhD Position in Fiber Devices for International Students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 593,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 594,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 595,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 596,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 597,
     "title": "Carleton University Entrance Scholarships for International Students",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 598,
     "title": "International Student Scholarships - Western University (UWO)",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "canada"
    },
    {
     "Column1": 599,
     "title": "National Buckeye Scholarship",
     "degrees": "Bachelor",
     "funds": "$54,000",
     "location": "united-states"
    },
    {
     "Column1": 600,
     "title": "Spirit of Giving Scholarship",
     "degrees": "Bachelor, Course",
     "funds": " $3,000",
     "location": "united-states"
    },
    {
     "Column1": 601,
     "title": "Global Spartan Leadership Program for International Students at Michigan State University",
     "degrees": "Bachelor",
     "funds": "$8000 ",
     "location": "united-states"
    },
    {
     "Column1": 602,
     "title": "International Scholarship Program (Firdaws Academy)",
     "degrees": "Course",
     "funds": 1,
     "date": "29-Dec-22",
     "location": "united-states"
    },
    {
     "Column1": 603,
     "title": "MIT THINK Scholarship Program",
     "degrees": "Course",
     "funds": "$7,000 worth of prizes",
     "location": "united-states"
    },
    {
     "Column1": 604,
     "title": "University of Maine Intensive English Institute Discovery Scholarship in the USA",
     "degrees": "Bachelor",
     "funds": "US $2,000",
     "location": "united-states"
    },
    {
     "Column1": 605,
     "title": "Presidentâ€™s Postdoctoral Fellowship Program at University of California in USA",
     "degrees": "Phd",
     "funds": "$50,760",
     "location": "united-states"
    },
    {
     "Column1": 606,
     "title": "Family Empowerment program",
     "degrees": "Bachelor",
     "funds": "The scholarship amount is the lesser of the schoolâ€™s tuition and fees or the calculated scholarship amount ",
     "location": "united-states"
    },
    {
     "Column1": 607,
     "title": "Rentkidz Annual Scholarship",
     "degrees": "Bachelor, Course",
     "funds": "$750",
     "location": "united-states"
    },
    {
     "Column1": 608,
     "title": "MPOWER Global Citizen Scholarship",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fixed interest rates for amounts between $2,001.00 and $50,000.00",
     "location": "united-states"
    },
    {
     "Column1": 609,
     "title": "Prodigy Finance â€“ International Student Loans",
     "location": "united-states"
    },
    {
     "Column1": 610,
     "title": "MPOWER Financing â€“ Education Loans for International Students",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fixed interest rates for amounts between $2,001.00 and $50,000.00",
     "location": "united-states"
    },
    {
     "Column1": 611,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "united-states"
    },
    {
     "Column1": 612,
     "title": "Ratingle Scholarship Program",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "$1000",
     "location": "united-states"
    },
    {
     "Column1": 613,
     "title": "Embry-Riddle Aeronautical University Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 614,
     "title": "UCB EU Transition Awards in UK",
     "degrees": "Master, Bachelor",
     "funds": "Tuition fee discount",
     "location": "united-kingdom"
    },
    {
     "Column1": 615,
     "title": "University of Strathclyde Access Bursary for ROI Students in UK",
     "degrees": "Bachelor",
     "funds": "Up to Â£3000",
     "date": "01-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 616,
     "title": "Lady Eileen McDonald EU & International Student Funds in UK",
     "degrees": "Phd, Master, Bachelor",
     "funds": "Â£300-Â£500",
     "date": "01-Jan-30",
     "location": "united-kingdom"
    },
    {
     "Column1": 617,
     "title": "LPDP Indonesia Scholarships at Cranfield University",
     "degrees": "Master, Phd",
     "funds": "Variable funds",
     "location": "united-kingdom"
    },
    {
     "Column1": 618,
     "title": "Cranfield Water Scholarships for Malawian Students in UK",
     "degrees": "Master",
     "funds": "Â£6,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 619,
     "title": "John Gilbert Vause Memorial International Scholarship in the UK",
     "degrees": "Bachelor",
     "funds": "Â£500",
     "location": "united-kingdom"
    },
    {
     "Column1": 620,
     "title": "International Scholarships at Durham University",
     "degrees": "Master, Bachelor",
     "funds": "Â£5,000 p.a.",
     "date": "29-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 621,
     "title": "International College Dundee Entrant Scholarships in UK",
     "degrees": "Master",
     "funds": "Up to Â£4,500 p.a.",
     "location": "united-kingdom"
    },
    {
     "Column1": 622,
     "title": "International Scholarship Student Competition 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2,000",
     "date": "01-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 623,
     "title": "Global Contest Scholarships for International Students 2022",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $2000 awards",
     "date": "31-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 624,
     "title": "Swansea University EU Transitional Bursary in UK",
     "degrees": "Bachelor",
     "funds": "Tuition fee reduction",
     "location": "united-kingdom"
    },
    {
     "Column1": 625,
     "title": "50% scholarship for students based in India - University of Essex Online",
     "degrees": "Master, Bachelor, Course",
     "funds": "50% scholarship for all courses",
     "date": "21-Jul-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 626,
     "title": "ITESM Doble Grado Tuition Fee Discount for International Students in UK",
     "degrees": "Master",
     "funds": "50% of tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 627,
     "title": "High Achiever Scholarships for UK and Ireland Students at University of Buckingham",
     "degrees": "Bachelor",
     "funds": " Â£2,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 628,
     "title": "LLM Master of Law Scholarships for International Students at University of Roehampton",
     "degrees": "Master",
     "funds": "Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 629,
     "title": "NYU Wagner Merit Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 630,
     "title": "Scholarships and Financial Aid for International Students - University of Oregon",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 631,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 632,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 633,
     "title": "Jefferson Fellowship",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 634,
     "title": "East Tennessee University - General Undergraduate Scholarships",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 635,
     "title": "The Nieman Foundation - Journalism Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 636,
     "title": "Scholarships at Church Divinity School â€¨of the Pacific",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 637,
     "title": "Rajawali Fellows Program - Harvard Kennedy School",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 638,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 639,
     "title": "East Tennessee State University - International Students Academic Merit Scholarship",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 640,
     "title": "Emory University scholarships for International Students",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 641,
     "title": "Illinois Wesleyan University - International Student Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 642,
     "title": "Bereaâ€™s Tuition Promise Scholarship",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 643,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 644,
     "title": "Lancaster EU Transition Scholarships in UK",
     "degrees": "Master, Bachelor",
     "funds": "Â£7,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 645,
     "title": "Heads of School Scholarships for EU Students at Bangor University",
     "degrees": "Phd",
     "funds": "10% of tuition fee p.a.",
     "location": "united-kingdom"
    },
    {
     "Column1": 646,
     "title": "University of Leeds Faculty of Engineering and Physical Sciences International Undergraduate Excellence Scholarships in UK",
     "degrees": "Bachelor",
     "funds": "Up to Â£6,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 647,
     "title": "UEA Turkish Awards in the UK",
     "degrees": "Master",
     "funds": "Up to Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 648,
     "title": "PGR Transitional Bursary for International Students at Swansea University",
     "degrees": "Master, Phd",
     "funds": "Reduced tuition fee",
     "location": "united-kingdom"
    },
    {
     "Column1": 649,
     "title": "University of Roehampton EU Transition Scholarships in UK",
     "degrees": "Master, Bachelor",
     "funds": "Tuition fee discount",
     "location": "united-kingdom"
    },
    {
     "Column1": 650,
     "title": "University of Birmingham Poynting Excellence international awards in UK",
     "degrees": "Bachelor",
     "funds": "Up to Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 651,
     "title": "EU\/EEA Scholarships at Middlesex University London in UK",
     "degrees": "Bachelor",
     "funds": "Reduced tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 652,
     "title": "Africa postgraduate placements at University of Dundee in UK",
     "degrees": "Master",
     "funds": "Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 653,
     "title": "Postgraduate Research international awards in Theory and Simulations of Frequency",
     "degrees": "Phd",
     "funds": "Fees, stipend + benefits",
     "location": "united-kingdom"
    },
    {
     "Column1": 654,
     "title": "KDS International Scholarship Competition 2021-22",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 655,
     "title": "Professional Development Grants for International Students at University of Twente",
     "degrees": "Course, Master",
     "funds": "Up to $6,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 656,
     "title": "International PhD Studentships in Metamaterial Nano-Machines",
     "degrees": "Phd",
     "funds": "Tuition fees + limited funding",
     "location": "united-kingdom"
    },
    {
     "Column1": 657,
     "title": "International Excellent Student Scholarships at University of Derby",
     "degrees": "Master, Bachelor",
     "funds": "Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 658,
     "title": "international awards at Brockenhurst College",
     "degrees": "Bachelor",
     "funds": "Up to 50% tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 659,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 660,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 661,
     "title": "Kingston University - International Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 662,
     "title": "Thomas College - Graduate International Scholarship Program",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 663,
     "title": "Hamilton College Scholarships for International Students",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 664,
     "title": "Konrad von Moltke Research Grants for the young researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 665,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 666,
     "title": "Fulbright Foreign Student Program",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 667,
     "title": "The American Indian Graduate Center - Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 668,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 669,
     "title": "Fellowships and Scholarships at Pardee RAND Graduate School",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 670,
     "title": "Loyola University Undergraduate Scholarships",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 671,
     "title": "John Lennon Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 672,
     "title": "New York Film Academy (NYFA) Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 673,
     "title": "University of Dayton Scholarships for Undergraduate International Students",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 674,
     "title": "University of Leeds MBA EEA Excellence Scholarships in UK",
     "degrees": "Master",
     "funds": "Half-fee",
     "location": "united-kingdom"
    },
    {
     "Column1": 675,
     "title": "South Asia Scholarships at University of Dundee",
     "degrees": "Bachelor",
     "funds": "$5,000 p.a., up to Â£25,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 676,
     "title": "EU Bursary at University of Reading",
     "degrees": "Bachelor",
     "funds": "Up to Â£6,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 677,
     "title": "Engagement Bursary for UK and EU Students at University of East London",
     "degrees": "Bachelor",
     "funds": "Up to Â£2,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 678,
     "title": "East African Scholarships at University of Edinburgh",
     "degrees": "Master",
     "funds": "100% tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 679,
     "title": "University of Leeds MBA Americas Excellence Scholarships in UK",
     "degrees": "Master",
     "funds": "Half-fee",
     "location": "united-kingdom"
    },
    {
     "Column1": 680,
     "title": "International Students Contest Scholarships 2021-2022",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1500",
     "date": "01-Oct-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 681,
     "title": "EU Transition Bursary at University of Derby",
     "degrees": "Bachelor, Master",
     "funds": "Â£4,500 p.a.",
     "location": "united-kingdom"
    },
    {
     "Column1": 682,
     "title": "Dr George Moore Data Science International Student Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 683,
     "title": "EU postgraduate placements at University of Stirling",
     "degrees": "Master",
     "funds": "40% fee discount",
     "location": "united-kingdom"
    },
    {
     "Column1": 684,
     "title": "University of Manchester International Mathematics Scholarships in UK",
     "degrees": "Bachelor",
     "funds": "Â£1,000 p.a.",
     "location": "united-kingdom"
    },
    {
     "Column1": 685,
     "title": "University of Liverpool International College (UoLIC) Excellence Scholarships in UK",
     "degrees": "Bachelor",
     "funds": "Â£5,000 tuition fee reduction",
     "location": "united-kingdom"
    },
    {
     "Column1": 686,
     "title": "University of Liverpool Management School European Union Excellence Scholarships",
     "degrees": "Master",
     "funds": "50% tuition fee waiver",
     "location": "united-kingdom"
    },
    {
     "Column1": 687,
     "title": "University of Manchester Global Futures Scholarships in UK",
     "degrees": "Master, Bachelor",
     "funds": "Variable",
     "location": "united-kingdom"
    },
    {
     "Column1": 688,
     "title": "Stirling Postgraduate Bangladesh Scholarships in UK",
     "degrees": "Master",
     "funds": "Â£4,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 689,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 690,
     "title": "Jefferson Undergraduate Scholarship - University of Virginia",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 691,
     "title": "Georgia College Scholarships for International Students",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 692,
     "title": "Brandeis University - Merit- and Need-Based Scholarships",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 693,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 694,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 695,
     "title": "Global Achievement Scholarship, Full Sail University",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 696,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 697,
     "title": "Harvard University-Graduate School of Arts and Sciences - Dissertation Completion Fellowships (DCF)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 698,
     "title": "Reagan-Fascell Democracy Fellows - National Endowment for Democracy",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 699,
     "title": "TransAtlantic Masters - Scholarships",
     "degrees": "Master",
     "funds": "Not Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 700,
     "title": "Euromasters Scholarships",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 701,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 702,
     "title": "The Humane Studies Fellowship - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 703,
     "title": "Kutztown University of Pennsylvania - International Student Scholarships",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 704,
     "title": "Aberdeen Global Scholarships for EU Students in UK",
     "degrees": "Master",
     "funds": "Up to Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 705,
     "title": "International Excellence Scholarships at University of East Anglia",
     "degrees": "Phd",
     "funds": "Â£4,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 706,
     "title": "University of Plymouth Mayflower funding for USA students",
     "degrees": "Bachelor",
     "funds": "Â£1,620 tuition fee discount",
     "location": "united-kingdom"
    },
    {
     "Column1": 707,
     "title": "EU Scholarships at University of Southampton",
     "degrees": "Bachelor, Master",
     "funds": "Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 708,
     "title": "Katrina Honeyman Scholarships for International Students in UK",
     "degrees": "Bachelor",
     "funds": "Â£2,000 p.a.",
     "location": "united-kingdom"
    },
    {
     "Column1": 709,
     "title": "Materials Science Entry Scholarships for International Students at University of Birmingham",
     "degrees": "Bachelor",
     "funds": "Up to Â£3,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 710,
     "title": "Queenâ€™s Excellence International Awards in UK",
     "degrees": "Bachelor",
     "funds": "Â£2,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 711,
     "title": "International Excellence Scholarships at University of Birmingham",
     "degrees": "Bachelor",
     "funds": "Â£1,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 712,
     "title": "Postgraduate Taught International Student Scholarships at University of Plymouth",
     "degrees": "Master",
     "funds": "Â£2,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 713,
     "title": "International Academic Excellence Scholarships at University of Plymouth",
     "degrees": "Bachelor, Master",
     "funds": "50% off tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 714,
     "title": "University of York Maths Academic Excellence international awards",
     "degrees": "Bachelor",
     "funds": "Â£1,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 715,
     "title": "International music awards at Swansea University",
     "degrees": "Bachelor",
     "funds": "Value of Â£1000 p.a.",
     "location": "united-kingdom"
    },
    {
     "Column1": 716,
     "title": "Fulbright Commission Awards for USA Students at University of Warwick in UK",
     "degrees": "Master",
     "funds": "Up to Â£26,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 717,
     "title": "45 Durham University Business School Masters international awards in UK",
     "degrees": "Master",
     "funds": "Up to Â£6,000 off tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 718,
     "title": "Rolls Royce PhD Positionsat University of Nottingham for UK and EU Students",
     "degrees": "Phd",
     "funds": "Tuition fees + Â£18,000 p.a. stipend",
     "location": "united-kingdom"
    },
    {
     "Column1": 719,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 720,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 721,
     "title": "Study in the USA as an exchange student (1-2 semesters)",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 722,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 723,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 724,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 725,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 726,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 727,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 728,
     "title": "Kellogg Institute for International Studies - Visiting Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 729,
     "title": "ChameleonJohn Annual $3,000 Scholarship for US Studies",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Not Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 730,
     "title": "New York University Stern merit-based scholarships",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 731,
     "title": "International Student Scholarships - University of Evansville",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 732,
     "title": "International Tuition Award - University of Arizona",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-states"
    },
    {
     "Column1": 733,
     "title": "UN-Nippon Fellowship Programme in Ocean Affairs for Coastal Developing Countries",
     "location": "united-states"
    },
    {
     "Column1": 734,
     "title": "Academic Achievement International Foundation Progression Scholarships in UK",
     "degrees": "Bachelor",
     "funds": "Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 735,
     "title": "University of Derby International merit awards in UK",
     "degrees": "Master, Bachelor",
     "funds": "Â£1,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 736,
     "title": "Lancaster University Global Scholarships for African Students in UK",
     "degrees": "Master",
     "funds": "Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 737,
     "title": "KDS Competition Scholarship 2021",
     "degrees": "Master, Bachelor",
     "funds": "Up to $1,500",
     "date": "01-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 738,
     "title": "2021 Contest Scholarships for International Students",
     "degrees": "Master, Bachelor, Course",
     "funds": "Up to $1,500",
     "date": "01-Jun-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 739,
     "title": "PhD in Advanced Manufacture for UK and EU Students in UK",
     "degrees": "Phd",
     "funds": "Â£15,285 p.a.",
     "location": "united-kingdom"
    },
    {
     "Column1": 740,
     "title": "PhDs (Cotutelle) Scholarships for EU Students at University of Kent",
     "degrees": "Phd",
     "funds": "50% Tuition fee",
     "location": "united-kingdom"
    },
    {
     "Column1": 741,
     "title": "Queenâ€™s University Belfast Vice-Chancellorâ€™s International Attainment postgraduate placements",
     "degrees": "Master",
     "funds": "50% discount on tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 742,
     "title": "Vice-Chancellorâ€™s Postgraduate International Excellence Scholarships at University of Brighton",
     "degrees": "Master",
     "funds": "Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 743,
     "title": "FindDataLab Research Grant Programme in USA and EU",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to $1,000 towards web scraping serivces",
     "location": "united-kingdom"
    },
    {
     "Column1": 744,
     "title": "Warwick School of Engineering PhD International Studentships in Pharmacometric Modelling",
     "degrees": "Phd",
     "funds": "Â£15,250 p.a. + tuition fees",
     "location": "united-kingdom"
    },
    {
     "Column1": 745,
     "title": "Google Anita Borg Memorial Scholarships for International Students at Arizona State University",
     "degrees": "Bachelor",
     "funds": "$10,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 746,
     "title": "LLM Academic Excellence Scholarships for International Students at University of East Anglia",
     "degrees": "Master",
     "funds": "Up to Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 747,
     "title": "Richard and Susan Hayden Academy Fellowship for Worldwide Students in UK",
     "degrees": "Phd",
     "funds": "Â£2,365 monthly stipend",
     "location": "united-kingdom"
    },
    {
     "Column1": 748,
     "title": "Anniversary Scholarships at London School of Economics and Political Science",
     "degrees": "Master",
     "funds": "Â£5,000-Â£25,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 749,
     "title": "Rotary Peace Fellowships",
     "location": "united-states"
    },
    {
     "Column1": 750,
     "title": "Full Tuition PhD Positionsfor UK and EU Students at University of Warwick",
     "degrees": "Phd",
     "funds": "Full university fees + allowance\/award",
     "location": "united-kingdom"
    },
    {
     "Column1": 751,
     "title": "IU International University of Applied Sciences Online Scholarships for International Students in Germany",
     "degrees": "Master, Bachelor",
     "funds": "Up to 85% of tuition fee",
     "location": "united-kingdom"
    },
    {
     "Column1": 752,
     "title": "Cranfield University international awards in the UK",
     "degrees": "Master",
     "location": "united-kingdom"
    },
    {
     "Column1": 753,
     "title": "Built Environment Undergraduate Silver Award for International Students at University of Salford",
     "degrees": "Bachelor",
     "funds": "Â£2000",
     "location": "united-kingdom"
    },
    {
     "Column1": 754,
     "title": "University of Portsmouth Faculty of Business and Law Postgraduate funding for UK and EU Students in UK",
     "degrees": "Bachelor, Master",
     "location": "united-kingdom"
    },
    {
     "Column1": 755,
     "title": "Coventry University EU Academic Excellence Award in the UK",
     "degrees": "Bachelor, Master",
     "funds": "Â£1,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 756,
     "title": "St Maryâ€™s University Vice-Chancellorâ€™s Excellence funding for UK and EU Students in UK",
     "degrees": "Bachelor",
     "funds": "Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 757,
     "title": "University of Liverpool Management School Future Leaders Masterâ€™s funding for UK and EU Students in UK",
     "degrees": "Master",
     "funds": "Full fee waiver",
     "location": "united-kingdom"
    },
    {
     "Column1": 758,
     "title": "Leicester Castle Business School International Postgraduate Taught Merit Scholarship in UK",
     "degrees": "Master",
     "funds": "Â£2,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 759,
     "title": "University of Bradford International MSc Scholarship in UK",
     "degrees": "Master",
     "funds": "Scholarship ",
     "location": "united-kingdom"
    },
    {
     "Column1": 760,
     "title": "Global MBA International Scholarship at De Montfort University",
     "degrees": "Bachelor, Master",
     "funds": " Â£2,500,",
     "location": "united-kingdom"
    },
    {
     "Column1": 761,
     "title": "UCL DPU Health in Urban Development International Scholarship in UK",
     "degrees": "Master",
     "funds": "Â£10,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 762,
     "title": "International Excellence\/Achievement Scholarship at University of Birmingham",
     "degrees": "Bachelor",
     "funds": " Â£7,500",
     "location": "united-kingdom"
    },
    {
     "Column1": 763,
     "title": "Scholarship for Online Learner at IU International University of Applied Sciences â€“ Online",
     "degrees": "Master, Bachelor",
     "funds": "Up to â‚¬ 13.000",
     "location": "united-kingdom"
    },
    {
     "Column1": 764,
     "title": "Scholarship for Academics at IU International University of Applied Sciences â€“ Online",
     "degrees": "Master, Bachelor",
     "funds": "up to â‚¬13.000",
     "location": "united-kingdom"
    },
    {
     "Column1": 765,
     "title": "Scholarship for Future Entrepreneur at IU International University of Applied Sciences - Online",
     "degrees": "Master, Bachelor",
     "funds": "not specified",
     "location": "united-kingdom"
    },
    {
     "Column1": 766,
     "title": "Scholarship for STEM\/MINT Professionals at IU International University of Applied Sciences - Online",
     "degrees": "Master, Bachelor",
     "funds": "Up to â‚¬13.000",
     "location": "united-kingdom"
    },
    {
     "Column1": 767,
     "title": "Scholarship for Women in Leadership and Management at IU International University of Applied Sciences - Online",
     "degrees": "Master, Bachelor",
     "funds": "Up to â‚¬13.000",
     "location": "united-kingdom"
    },
    {
     "Column1": 768,
     "title": "International Sporting Excellence Award at University of Nottingham",
     "degrees": "Bachelor, Master",
     "funds": "Â£5,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 769,
     "title": "International Foundation Year Scholarship at the University of Leeds in the UK",
     "degrees": "Bachelor",
     "funds": "Â£3,000",
     "location": "united-kingdom"
    },
    {
     "Column1": 770,
     "title": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
     "degrees": "Phd",
     "funds": "Â£15,009",
     "location": "united-kingdom"
    },
    {
     "Column1": 771,
     "title": "Merit funding for International Students at University of Central Lancashire",
     "degrees": "Bachelor, Master",
     "funds": "Â£2,000 per year",
     "location": "united-kingdom"
    },
    {
     "Column1": 772,
     "title": "International Scholarship Program (Firdaws Academy)",
     "degrees": "Course",
     "funds": 1,
     "date": "29-Dec-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 773,
     "title": "international awards at the University of South Wales in the UK",
     "degrees": "Master, Bachelor",
     "funds": "Â£2,250",
     "location": "united-kingdom"
    },
    {
     "Column1": 774,
     "title": "PGT Excellence International Scholarship at the University of Glasgow in the UK",
     "degrees": "Master",
     "funds": " Â£5000",
     "location": "united-kingdom"
    },
    {
     "Column1": 775,
     "title": "Oxford Leo Tong Chen Scholarships for International Students in the UK",
     "degrees": "Master",
     "funds": "Â£15,000 ",
     "location": "united-kingdom"
    },
    {
     "Column1": 776,
     "title": "Prodigy Finance â€“ International Student Loans",
     "location": "united-kingdom"
    },
    {
     "Column1": 777,
     "title": "Marine Stewardship Council scholarship research program ",
     "degrees": "Bachelor, Master, Phd, Course",
     "funds": "Up to Â£4000",
     "location": "united-kingdom"
    },
    {
     "Column1": 778,
     "title": "Goldsmiths, University of London International Response Scholarships",
     "degrees": "Bachelor, Master",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 779,
     "title": "International Merit Postgraduate Scholarships at University of Sheffield in UK, 2017",
     "degrees": "Master, Phd",
     "funds": "25% of tuition fees",
     "date": "16-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 780,
     "title": "University of Manchester PhD Scholarships for International Students in UK, 2017-2018",
     "degrees": "Phd",
     "date": "Varies",
     "location": "united-kingdom"
    },
    {
     "Column1": 781,
     "title": "UCL Undergraduate Scholarships\/Bursaries (University College London)",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 782,
     "title": "Erasmus Mundus European Master in Global Studies",
     "degrees": "Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 783,
     "title": "EMBL International PhD Programme: Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 784,
     "title": "International Science Scholarships, Nottingham Trent University",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 785,
     "title": "WCC scholarships programme (World Council of Churches)",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 786,
     "title": "IPRA Foundation Peace Research Grants Program",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 787,
     "title": "ECF (European Cultural Foundation) STEP Beyond Travel grant",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 788,
     "title": "UWE Bristol International Scholarships: Postgraduate",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 789,
     "title": "Mawista Scholarship for Students Studying Abroad with a Child",
     "degrees": "Bachelor, Master",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 790,
     "title": "Brunel International Scholarships",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 791,
     "title": "Wessex Institute of Technology - Research Studies",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 792,
     "title": "ROTARY GLOBAL GRANTS",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 793,
     "title": "Ernst Ludwig Ehrlich Studienwerk - Scholarships",
     "degrees": "Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 794,
     "title": "European Molecular Biology Short-Term Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 795,
     "title": "BPP University, UK-Vice Chancellorâ€™s Scholarship",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 796,
     "title": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 797,
     "title": "Konrad von Moltke Research Grants for the young researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 798,
     "title": "Institute for Current World Affairs - FELLOWSHIPS",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 799,
     "title": "Airbus Group PhD opportunities",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 800,
     "title": "Adobe Research Women-in-Technology Scholarship",
     "degrees": "Bachelor",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 801,
     "title": "Pirbright Institute",
     "degrees": "Phd",
     "funds": "Not Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 802,
     "title": "BATH University - Sport Scholarship Scheme",
     "degrees": "Bachelor, Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 803,
     "title": "The Engineering Doctorate (EngD) - Bath and Bournemouth Universities, Centre for Doctoral Training",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Invalid date",
     "location": "united-kingdom"
    },
    {
     "Column1": 804,
     "title": "Exchange Student Programme at SOAS",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 805,
     "title": "Study Abroad at SOAS",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 806,
     "title": "Alliance Manchester Business School Scholarships",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 807,
     "title": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 808,
     "title": "Boustany Foundation - Cambridge University MBA Scholarship",
     "degrees": "Master",
     "funds": "Â£30,000",
     "date": "15-May-22",
     "location": "united-kingdom"
    },
    {
     "Column1": 809,
     "title": "The Boehringer Ingelheim Fonds awards PhD fellowships",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 810,
     "title": "The Boehringer Ingelheim Fonds - Travel grants for junior researchers",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 811,
     "title": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 812,
     "title": "University of Hertfordshire - Scholarships for international students",
     "degrees": "Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 813,
     "title": "TransAtlantic Masters - Scholarships",
     "degrees": "Master",
     "funds": "Not Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 814,
     "title": "Euromasters Scholarships",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 815,
     "title": "London Met University - Funding your studies",
     "degrees": "Master, Bachelor, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 816,
     "title": "London Met University - Funding your studies",
     "degrees": "Master, Bachelor, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 817,
     "title": "Hayek Fund for Scholars - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 818,
     "title": "The Humane Studies Fellowship - Institute for Humane Studies at George Mason University",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 819,
     "title": "Wessex Institute of Technology - Research Studies",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 820,
     "title": "Erasmus Exchange Programme",
     "degrees": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 821,
     "title": "YFU (Youth for Undestanding) - Youth Exchange",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 822,
     "title": "Be an exchange student for 1-2 semesters",
     "degrees": "Not Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 823,
     "title": "Birmingham Masters Scholarships",
     "degrees": "Master",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 824,
     "title": "Horizon 2020",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 825,
     "title": "Amelia Earhart Fellowship",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 826,
     "title": "The Leakey Foundationâ€™s Research Grants to doctoral students",
     "degrees": "Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 827,
     "title": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Fully Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 828,
     "title": "ArtUniverse Scholarships",
     "degrees": "Bachelor, Master, Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 829,
     "title": "High Achievers Scholarship - Edge Hill University",
     "degrees": "Bachelor",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    },
    {
     "Column1": 830,
     "title": "Wolfson Postgraduate Scholarships in the Humanities - The Wolfson Foundation",
     "degrees": "Phd",
     "funds": "Partially Funded",
     "date": "Always Active",
     "location": "united-kingdom"
    }
   ]

fields_to_keep = ["Column", "age"]

# Create a new list with filtered JSON objects
filtered_data = [{field: item[field] for field in fields_to_keep} for item in data]

# Convert the filtered list back to JSON
filtered_json = json.dumps(filtered_data, indent=2)

print(filtered_json)




