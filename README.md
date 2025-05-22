 Regex Data Extractor
This project is designed to extract structured data from raw text using Python and Regular Expressions (regex). It identifies and extracts:

Phone Numbers

Email Addresses

Currency Amounts

HTML Tags

URLs

File Structure
bash
Copy
Edit
.
├── data_samples.txt        # Text file containing sample data to extract from
├── extractor_script.py     # Main script to run the extractors
├── regex_extractors.py     # Contains all regex-based extractor functions
└── README.md               # Project documentation (this file)
 Getting Started
1. Clone or Download the Repository
bash
Copy
Edit
git clone https://github.com/your-username/regex-data-extractor.git
cd regex-data-extractor
2. Prepare the Sample Data
Edit or replace the data_samples.txt file with your own unstructured data containing phone numbers, emails, etc.

3. Run the Script
bash
Copy
Edit
python extractor_script.py
This will print extracted data in the console.

 Features & Function Descriptions
1. extract_phone_numbers(text)
Extracts phone numbers in formats like:

(555) 867-5309

555-867-5309

555.867.5309

2. extract_emails(text)
Finds email addresses using a standard regex for usernames and domains.

3. extract_currency(text)
Captures currency values like:

$0.99

$10,000.00

4. extract_html_tags(text)
Extracts all HTML tags such as:

html
Copy
Edit
<div>, <a href="...">, </span>
5. extract_urls(text)
Identifies full URLs like:

http://testsite.com/page?id=42

https://secure.site.gov

 Sample Data Example
Your data_samples.txt can include the following types of entries:

typescript
Copy
Edit
(555) 867-5309, 555-867-5309, another.user@domain.com
$0.99, <div>Sample Text</div>, http://testsite.com
The script will extract structured outputs from this messy text.

Requirements
Python 3

No external libraries required (uses re module only)

 Author 
 Tumugane ROLANDE

