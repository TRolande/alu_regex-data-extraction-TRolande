import re

def extract_phone_numbers(text):
    pattern = r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
    return re.findall(pattern, text)

def extract_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    return re.findall(pattern, text)

def extract_currency(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

def extract_html_tags(text):
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://[^\s<>"\']+|www\.[^\s<>"\']+'
    return re.findall(pattern, text)
