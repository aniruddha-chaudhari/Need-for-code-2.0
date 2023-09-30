import json

data = [
 {
  "name": "Presidentâ€™s Scholarship for Ukraine",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$2500",
  "date": "31-Nov-23",
  "location": "united-states"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "united-states"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "united-states"
 },
 {
  "name": "Improve Menâ€™s Health Scholarship",
  "degrees": "Master, Bachelor, Phd",
  "funds": "$2000",
  "date": "31-Oct-23",
  "location": "united-states"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "united-states"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "united-states"
 },
 {
  "name": "American Indian Scholarships at Augsburg University",
  "degrees": "Bachelor",
  "funds": "Partial tuition fees",
  "date": "01-Dec-23",
  "location": "united-states"
 },
 {
  "name": "International Contest for Students Support 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "28-Nov-23",
  "location": "united-states"
 },
 {
  "name": "Scholarships for Africa",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$100 to $3000",
  "date": "24-Mar-27",
  "location": "united-states"
 },
 {
  "name": "LAPTOP Scholarships - study Supply Chains",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "up to $3000",
  "date": "06-Oct-23",
  "location": "united-states"
 },
 {
  "name": "Medicine: Fully Funded Swansea & HMRI PhD Scholarship: Ovarian Cancer Chemoresistance",
  "degrees": "Phd",
  "funds": "Full cost of tuition fees and an annual stipend",
  "date": "06-Oct-23",
  "location": "united-states"
 },
 {
  "name": "New York University - Dectember 11 Scholarships",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Pay any remaining balance.",
  "date": "30-Dec-23",
  "location": "united-states"
 },
 {
  "name": "TKS Full-Ride Scholarship",
  "degrees": "Course",
  "funds": "100% Tuition Fee [value of $6,000+]",
  "date": "31-Oct-23",
  "location": "united-states"
 },
 {
  "name": "Five scholarships of up to US$3000 for supply chain courses",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$3000",
  "date": "06-Oct-23",
  "location": "united-states"
 },
 {
  "name": "GREAT Scholarship for Bangladesh Students in UK",
  "degrees": "Master",
  "funds": "Â£10,000",
  "date": "31-Oct-23",
  "location": "united-kingdom"
 },
 {
  "name": "Diversity Scholarships for Africa and Latin American Students in UK",
  "degrees": "Master",
  "funds": "50% scholarship",
  "date": "31-Oct-23",
  "location": "united-kingdom"
 },
 {
  "name": "Beth Mead Scholarships for International Students at Teesside University",
  "degrees": "Bachelor, Master",
  "funds": "Â£1,200",
  "date": "31-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "Malaysia Scholarships at Nottingham Trent University",
  "degrees": "Master",
  "funds": "Â£4,000",
  "date": "29-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "PhD Studentships in Predictive Uncertainty in Computer Vision for International Students in UK",
  "degrees": "Master",
  "funds": "Â£16,062 p.a., tuition fees + Â£2,000 research grant",
  "date": "10-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "Strathclyde Business School MRes Scholarships in UK",
  "degrees": "Master",
  "funds": "Tuition fees",
  "location": "united-kingdom"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "united-kingdom"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "Engineering: Fully Funded MSc by Research at Swansea: Functional Construction Materials",
  "degrees": "Master",
  "funds": "Full cost of UK tuition fees and an annual stipend",
  "date": "27-Oct-23",
  "location": "united-kingdom"
 },
 {
  "name": "UEA Law School Country Specific Academic Excellence Scholarships in UK",
  "degrees": "Master",
  "funds": "Â£8,000 tuition fee reduction",
  "date": "31-Oct-23",
  "location": "united-kingdom"
 },
 {
  "name": "Saraswati Dalmia Scholarship at SOAS University of London",
  "degrees": "Phd, Master",
  "funds": "Up to Â£5,353",
  "date": "02-Oct-23",
  "location": "united-kingdom"
 },
 {
  "name": "The Professor Mike Walker OBE Scholarships for International Students in the UK",
  "degrees": "Master",
  "funds": "Up to Â£12,000 tuition fee reduction",
  "date": "11-Nov-23",
  "location": "united-kingdom"
 },
 {
  "name": "PhD Studentships in Electronic",
  "degrees": "Phd",
  "date": "03-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "canada"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "canada"
 },
 {
  "name": "Improve Menâ€™s Health Scholarship",
  "degrees": "Master, Bachelor, Phd",
  "funds": "$2000",
  "date": "31-Oct-23",
  "location": "canada"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "canada"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "canada"
 },
 {
  "name": "International Contest for Students Support 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "28-Nov-23",
  "location": "canada"
 },
 {
  "name": "Scholarships for Africa",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$100 to $3000",
  "date": "24-Mar-27",
  "location": "canada"
 },
 {
  "name": "LAPTOP Scholarships - study Supply Chains",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "up to $3000",
  "date": "06-Oct-23",
  "location": "canada"
 },
 {
  "name": "TKS Full-Ride Scholarship",
  "degrees": "Course",
  "funds": "100% Tuition Fee [value of $6,000+]",
  "date": "31-Oct-23",
  "location": "canada"
 },
 {
  "name": "Five scholarships of up to US$3000 for supply chain courses",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$3000",
  "date": "06-Oct-23",
  "location": "canada"
 },
 {
  "name": "International No-Essay Support Competition Scholarships 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000",
  "date": "20-Nov-23",
  "location": "canada"
 },
 {
  "name": "THGM MUSE Scholarship",
  "degrees": "Bachelor",
  "funds": "US$500 or C$630",
  "date": "15-Oct-23",
  "location": "canada"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
  "degrees": "Master",
  "funds": "80% off tuition fee",
  "date": "15-Oct-23",
  "location": "canada"
 },
 {
  "name": "International Students Support Contest 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "30-Dec-23",
  "location": "canada"
 },
 {
  "name": "Human Resource (HR) - Free Course From Windsor University's MBA",
  "degrees": "Master, Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "canada"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "europe"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "europe"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "europe"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "europe"
 },
 {
  "name": "International Contest for Students Support 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "28-Nov-23",
  "location": "europe"
 },
 {
  "name": "Scholarships for Africa",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$100 to $3000",
  "date": "24-Mar-27",
  "location": "europe"
 },
 {
  "name": "LAPTOP Scholarships - study Supply Chains",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "up to $3000",
  "date": "06-Oct-23",
  "location": "europe"
 },
 {
  "name": "TKS Full-Ride Scholarship",
  "degrees": "Course",
  "funds": "100% Tuition Fee [value of $6,000+]",
  "date": "31-Oct-23",
  "location": "europe"
 },
 {
  "name": "Five scholarships of up to US$3000 for supply chain courses",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$3000",
  "date": "06-Oct-23",
  "location": "europe"
 },
 {
  "name": "International No-Essay Support Competition Scholarships 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000",
  "date": "20-Nov-23",
  "location": "europe"
 },
 {
  "name": "THGM MUSE Scholarship",
  "degrees": "Bachelor",
  "funds": "US$500 or C$630",
  "date": "15-Oct-23",
  "location": "europe"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
  "degrees": "Master",
  "funds": "80% off tuition fee",
  "date": "15-Oct-23",
  "location": "europe"
 },
 {
  "name": "International Students Support Contest 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "30-Dec-23",
  "location": "europe"
 },
 {
  "name": "Becas Grisart 2023",
  "degrees": "Course",
  "funds": "Take the courses free of charge.",
  "date": "25-Oct-23",
  "location": "europe"
 },
 {
  "name": "Human Resource (HR) - Free Course From Windsor University's MBA",
  "degrees": "Master, Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "europe"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "south-africa"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "south-africa"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "south-africa"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "south-africa"
 },
 {
  "name": "International Contest for Students Support 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "28-Nov-23",
  "location": "south-africa"
 },
 {
  "name": "Scholarships for Africa",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$100 to $3000",
  "date": "24-Mar-27",
  "location": "south-africa"
 },
 {
  "name": "LAPTOP Scholarships - study Supply Chains",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "up to $3000",
  "date": "06-Oct-23",
  "location": "south-africa"
 },
 {
  "name": "TKS Full-Ride Scholarship",
  "degrees": "Course",
  "funds": "100% Tuition Fee [value of $6,000+]",
  "date": "31-Oct-23",
  "location": "south-africa"
 },
 {
  "name": "Five scholarships of up to US$3000 for supply chain courses",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$3000",
  "date": "06-Oct-23",
  "location": "south-africa"
 },
 {
  "name": "International No-Essay Support Competition Scholarships 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000",
  "date": "20-Nov-23",
  "location": "south-africa"
 },
 {
  "name": "THGM MUSE Scholarship",
  "degrees": "Bachelor",
  "funds": "US$500 or C$630",
  "date": "15-Oct-23",
  "location": "south-africa"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
  "degrees": "Master",
  "funds": "80% off tuition fee",
  "date": "15-Oct-23",
  "location": "south-africa"
 },
 {
  "name": "International Students Support Contest 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "30-Dec-23",
  "location": "south-africa"
 },
 {
  "name": "Human Resource (HR) - Free Course From Windsor University's MBA",
  "degrees": "Master, Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "south-africa"
 },
 {
  "name": "Project Management - Free Course From Windsor University's MBA",
  "degrees": "Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "south-africa"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "nigeria"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "nigeria"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "nigeria"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "nigeria"
 },
 {
  "name": "International Contest for Students Support 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "28-Nov-23",
  "location": "nigeria"
 },
 {
  "name": "Scholarships for Africa",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$100 to $3000",
  "date": "24-Mar-27",
  "location": "nigeria"
 },
 {
  "name": "LAPTOP Scholarships - study Supply Chains",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "up to $3000",
  "date": "06-Oct-23",
  "location": "nigeria"
 },
 {
  "name": "TKS Full-Ride Scholarship",
  "degrees": "Course",
  "funds": "100% Tuition Fee [value of $6,000+]",
  "date": "31-Oct-23",
  "location": "nigeria"
 },
 {
  "name": "Five scholarships of up to US$3000 for supply chain courses",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$3000",
  "date": "06-Oct-23",
  "location": "nigeria"
 },
 {
  "name": "International No-Essay Support Competition Scholarships 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000",
  "date": "20-Nov-23",
  "location": "nigeria"
 },
 {
  "name": "THGM MUSE Scholarship",
  "degrees": "Bachelor",
  "funds": "US$500 or C$630",
  "date": "15-Oct-23",
  "location": "nigeria"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
  "degrees": "Master",
  "funds": "80% off tuition fee",
  "date": "15-Oct-23",
  "location": "nigeria"
 },
 {
  "name": "International Students Support Contest 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "30-Dec-23",
  "location": "nigeria"
 },
 {
  "name": "Human Resource (HR) - Free Course From Windsor University's MBA",
  "degrees": "Master, Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "nigeria"
 },
 {
  "name": "Project Management - Free Course From Windsor University's MBA",
  "degrees": "Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "nigeria"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "pakistan"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "pakistan"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "pakistan"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "pakistan"
 },
 {
  "name": "International Contest for Students Support 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "28-Nov-23",
  "location": "pakistan"
 },
 {
  "name": "Scholarships for Africa",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$100 to $3000",
  "date": "24-Mar-27",
  "location": "pakistan"
 },
 {
  "name": "LAPTOP Scholarships - study Supply Chains",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "up to $3000",
  "date": "06-Oct-23",
  "location": "pakistan"
 },
 {
  "name": "TKS Full-Ride Scholarship",
  "degrees": "Course",
  "funds": "100% Tuition Fee [value of $6,000+]",
  "date": "31-Oct-23",
  "location": "pakistan"
 },
 {
  "name": "Five scholarships of up to US$3000 for supply chain courses",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$3000",
  "date": "06-Oct-23",
  "location": "pakistan"
 },
 {
  "name": "International No-Essay Support Competition Scholarships 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000",
  "date": "20-Nov-23",
  "location": "pakistan"
 },
 {
  "name": "THGM MUSE Scholarship",
  "degrees": "Bachelor",
  "funds": "US$500 or C$630",
  "date": "15-Oct-23",
  "location": "pakistan"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
  "degrees": "Master",
  "funds": "80% off tuition fee",
  "date": "15-Oct-23",
  "location": "pakistan"
 },
 {
  "name": "International Students Support Contest 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "30-Dec-23",
  "location": "pakistan"
 },
 {
  "name": "Human Resource (HR) - Free Course From Windsor University's MBA",
  "degrees": "Master, Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "pakistan"
 },
 {
  "name": "Project Management - Free Course From Windsor University's MBA",
  "degrees": "Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "pakistan"
 },
 {
  "name": "International Students Diversity Contest 2023-2024",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "Up to $2,000",
  "date": "23-Dec-23",
  "location": "india"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee",
  "degrees": "Master",
  "funds": "80% Tuition Fees",
  "date": "15-Dec-23",
  "location": "india"
 },
 {
  "name": "3 Month F1 Visa Study English in USA Scholarship with Windsor University",
  "degrees": "Course",
  "funds": "$1455",
  "date": "01-Nov-23",
  "location": "india"
 },
 {
  "name": "ArtUniverse",
  "degrees": "Master, Course",
  "funds": "Full or partial scholarship",
  "date": "30-Dec-23",
  "location": "india"
 },
 {
  "name": "International Contest for Students Support 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "28-Nov-23",
  "location": "india"
 },
 {
  "name": "Scholarships for Africa",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$100 to $3000",
  "date": "24-Mar-27",
  "location": "india"
 },
 {
  "name": "LAPTOP Scholarships - study Supply Chains",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "up to $3000",
  "date": "06-Oct-23",
  "location": "india"
 },
 {
  "name": "TKS Full-Ride Scholarship",
  "degrees": "Course",
  "funds": "100% Tuition Fee [value of $6,000+]",
  "date": "31-Oct-23",
  "location": "india"
 },
 {
  "name": "Five scholarships of up to US$3000 for supply chain courses",
  "degrees": "Master, Bachelor, Phd, Course",
  "funds": "$3000",
  "date": "06-Oct-23",
  "location": "india"
 },
 {
  "name": "International No-Essay Support Competition Scholarships 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000",
  "date": "20-Nov-23",
  "location": "india"
 },
 {
  "name": "THGM MUSE Scholarship",
  "degrees": "Bachelor",
  "funds": "US$500 or C$630",
  "date": "15-Oct-23",
  "location": "india"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
  "degrees": "Master",
  "funds": "80% off tuition fee",
  "date": "15-Oct-23",
  "location": "india"
 },
 {
  "name": "International Students Support Contest 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "30-Dec-23",
  "location": "india"
 },
 {
  "name": "Human Resource (HR) - Free Course From Windsor University's MBA",
  "degrees": "Master, Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "india"
 },
 {
  "name": "Project Management - Free Course From Windsor University's MBA",
  "degrees": "Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "india"
 },
 {
  "name": "LSA International Student Scholarships at Regents of the University of Michigan in USA",
  "degrees": "Bachelor",
  "funds": "Up to $10,000",
  "location": "united-states"
 },
 {
  "name": "International No-Essay Support Competition Scholarships 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000",
  "date": "20-Nov-23",
  "location": "united-states"
 },
 {
  "name": "THGM MUSE Scholarship",
  "degrees": "Bachelor",
  "funds": "US$500 or C$630",
  "date": "15-Oct-23",
  "location": "united-states"
 },
 {
  "name": "NLU Direct to Success Transfer Student Scholarship",
  "degrees": "Bachelor",
  "funds": "25% Tuition Rate",
  "date": "31-Dec-23",
  "location": "united-states"
 },
 {
  "name": "Kendell College at NLU International Opportunity Scholarship",
  "degrees": "Bachelor",
  "funds": "25% of the full-time tuition rate",
  "date": "31-Dec-23",
  "location": "united-states"
 },
 {
  "name": "NLU International Fresh Start Scholarship",
  "degrees": "Bachelor",
  "funds": "44% tuition fee",
  "date": "31-Dec-23",
  "location": "united-states"
 },
 {
  "name": "National Louis University #YouAreWelcomeHere Scholarship",
  "degrees": "Bachelor",
  "funds": "50% of full-time tuition",
  "date": "12-Nov-23",
  "location": "united-states"
 },
 {
  "name": "NLU Alumni Scholarship",
  "degrees": "Master, Bachelor, Phd",
  "funds": "15% Tuition Fee",
  "date": "31-Dec-23",
  "location": "united-states"
 },
 {
  "name": "Master in Business Administration 80% OFF your Tuition fee - Scholarship",
  "degrees": "Master",
  "funds": "80% off tuition fee",
  "date": "15-Oct-23",
  "location": "united-states"
 },
 {
  "name": "International Students Support Contest 2023-2024",
  "degrees": "Master, Bachelor, Course",
  "funds": "Up to $2,000 awards",
  "date": "30-Dec-23",
  "location": "united-states"
 },
 {
  "name": "Tiffin University International Trustee Scholarships in USA",
  "degrees": "Bachelor",
  "funds": "$16,000",
  "date": "15-Nov-23",
  "location": "united-states"
 },
 {
  "name": "Tiffin University International President Scholarships in USA",
  "degrees": "Bachelor",
  "funds": "$14,000",
  "date": "15-Nov-23",
  "location": "united-states"
 },
 {
  "name": "Graduate International Scholarships at University of Central Oklahoma",
  "degrees": "Master",
  "funds": "Up to $2,000 ($1,000 per year)",
  "date": "31-Oct-23",
  "location": "united-states"
 },
 {
  "name": "International Opportunity Awards at Texas A&M University",
  "degrees": "Bachelor",
  "funds": "$100 to $15,000 p\/a",
  "date": "01-Dec-23",
  "location": "united-states"
 },
 {
  "name": "Human Resource (HR) - Free Course From Windsor University's MBA",
  "degrees": "Master, Course",
  "funds": "100% free",
  "date": "14-Oct-23",
  "location": "united-states"
 },
 {
  "name": "Global Voices Scholarships at University of East Anglia",
  "degrees": "Master",
  "funds": "Â£20,000",
  "date": "03-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "Postgraduate International Development Scholarships for Sub Saharan African Students in UK",
  "degrees": "Master",
  "funds": "Â£8,000",
  "date": "31-Oct-23",
  "location": "united-kingdom"
 },
 {
  "name": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "nigeria"
 },
 {
  "name": "Institute for Current World Affairs - FELLOWSHIPS",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "nigeria"
 },
 {
  "name": "Adobe Research Women-in-Technology Scholarship",
  "degrees": "Bachelor",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "nigeria"
 },
 {
  "name": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "nigeria"
 },
 {
  "name": "The Boehringer Ingelheim Fonds awards PhD fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "nigeria"
 },
 {
  "name": "WCC scholarships programme (World Council of Churches)",
  "degrees": "Bachelor, Master, Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "IPRA Foundation Peace Research Grants Program",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "Mawista Scholarship for Students Studying Abroad with a Child",
  "degrees": "Bachelor, Master",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "ROTARY GLOBAL GRANTS",
  "degrees": "Master, Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "European Molecular Biology Short-Term Fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "John Dillon Fellowship - Australian Centre for International Agricultural Research (ACIAR)",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "Institute for Current World Affairs - FELLOWSHIPS",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "Adobe Research Women-in-Technology Scholarship",
  "degrees": "Bachelor",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "pakistan"
 },
 {
  "name": "International Council of Ophthalmology (ICO) - Three-Month Fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Jefferson Undergraduate Scholarship - University of Virginia",
  "degrees": "Bachelor",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Georgia College Scholarships for International Students",
  "degrees": "Bachelor, Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Brandeis University - Merit- and Need-Based Scholarships",
  "degrees": "Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "The Boehringer Ingelheim Fonds awards PhD fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "The Boehringer Ingelheim Fonds - Travel grants for Decior researchers",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Global Achievement Scholarship, Full Sail University",
  "degrees": "Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Paul Sumerall Memorial Scholarships, Merchants Bank of California",
  "degrees": "Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Harvard University-Graduate School of Arts and Sciences - Dissertation Completion Fellowships (DCF)",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Reagan-Fascell Democracy Fellows - National Endowment for Democracy",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "TransAtlantic Masters - Scholarships",
  "degrees": "Master",
  "funds": "Not Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Euromasters Scholarships",
  "degrees": "Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Horizon 2020",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Amelia Earhart Fellowship",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "The Leakey Foundationâ€™s Research Grants to doctoral students",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Axol Science Scholarship for Graduate or Undergraduate Degree Programs",
  "degrees": "Bachelor, Master, Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "ArtUniverse Scholarships",
  "degrees": "Bachelor, Master, Phd",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Kellogg Institute for International Studies - Visiting Fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "ChameleonJohn Annual $3,000 Scholarship for US Studies",
  "degrees": "Bachelor, Master, Phd",
  "funds": "Not Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "New York University Stern merit-based scholarships",
  "degrees": "Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "International Student Scholarships - University of Evansville",
  "degrees": "Bachelor, Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "International Tuition Award - University of Arizona",
  "degrees": "Bachelor",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-states"
 },
 {
  "name": "Fully-Funded PhD Studentship in Nanochemistry at University of Exeter",
  "degrees": "Phd",
  "funds": "Â£15,009",
  "location": "united-kingdom",
  "date": "Always Active"
 },
 {
  "name": "International Scholarship Program (Firdaws Academy)",
  "degrees": "Course",
  "funds": 1,
  "date": "29-Dec-23",
  "location": "united-kingdom"
 },
 {
  "name": "International Merit Postgraduate Scholarships at University of Sheffield in UK, 2017",
  "degrees": "Master, Phd",
  "funds": "25% of tuition fees",
  "date": "16-Oct-23",
  "location": "united-kingdom"
 },
 {
  "name": "University of Manchester PhD Scholarships for International Students in UK, 2017-2018",
  "degrees": "Phd",
  "date": "Varies",
  "location": "united-kingdom"
 },
 {
  "name": "UCL Undergraduate Scholarships\/Bursaries (University College London)",
  "degrees": "Bachelor",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "Erasmus Mundus European Master in Global Studies",
  "degrees": "Master",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "EMBL International PhD Programme: Fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "International Science Scholarships, Nottingham Trent University",
  "degrees": "Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "WCC scholarships programme (World Council of Churches)",
  "degrees": "Bachelor, Master, Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "IPRA Foundation Peace Research Grants Program",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "ECF (European Cultural Foundation) STEP Beyond Travel grant",
  "degrees": "Phd",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "UWE Bristol International Scholarships: Postgraduate",
  "degrees": "Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "Mawista Scholarship for Students Studying Abroad with a Child",
  "degrees": "Bachelor, Master",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "Brunel International Scholarships",
  "degrees": "Bachelor, Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "Wessex Institute of Technology - Research Studies",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "ROTARY GLOBAL GRANTS",
  "degrees": "Master, Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "Ernst Ludwig Ehrlich Studienwerk - Scholarships",
  "degrees": "Master, Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "European Molecular Biology Short-Term Fellowships",
  "degrees": "Phd",
  "funds": "Fully Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 },
 {
  "name": "BPP University, UK-Vice Chancellorâ€™s Scholarship",
  "degrees": "Bachelor, Master",
  "funds": "Partially Funded",
  "date": "Always Active",
  "location": "united-kingdom"
 }
]
