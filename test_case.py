from regex_extractors import *

#This will open the file data_samples.txt in read mode and i will use UTF-8 for encoding
#and this file will contain all the sample text for extraction.

with open('data_samples.txt', 'r', encoding='utf-8') as file:
    #This will read this file whole content and put it into string
    content = file.read()
    

#This will call the function for phone numbers and print the result.
print("Phone Numbers:", extract_phone_numbers(content))
#This will call the function of email and print the results.
print("Emails:", extract_emails(content))
#This will call the function for currency and print the results.
print("Currency:", extract_currency(content))
#This will call the function for html tags and print the results.
print("HTML Tags:", extract_html_tags(content))
#This will call the function for urls and print the results.
print("URLs:", extract_urls(content))
