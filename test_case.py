from regex_extractors import *

with open('data_samples.txt', 'r', encoding='utf-8') as file:
    content = file.read()


print("Phone Numbers:", extract_phone_numbers(content))
print("Emails:", extract_emails(content))
print("Currency:", extract_currency(content))
print("HTML Tags:", extract_html_tags(content))
print("URLs:", extract_urls(content))
