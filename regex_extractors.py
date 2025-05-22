import re
# This will help to import the regular expressions module thati am going to use.

def extract_phone_numbers(text):
    # This Function will help to extract phone numbers from the ones entered.
    pattern = r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
     # This Pattern will match formats like (123) 456-7890, 123-456-7890, 123.456.7890, or 123 456 7890
    return re.findall(pattern, text)

# Function will extract email addresses from the entries
def extract_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    return re.findall(pattern, text)
#This function will extract the currency following the condition which is in the regex expression
def extract_currency(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)
#This function will be for the html tags and their conditions which are written in the expression.
def extract_html_tags(text):
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)
#This will be the fuction for extracting url 
def extract_urls(text):
    pattern = r'https?://[^\s<>"\']+|www\.[^\s<>"\']+'
    return re.findall(pattern, text)
