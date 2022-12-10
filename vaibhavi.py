# 1. WAP to check if the given contact number is valid or invalid using regular expressions-
import re
pattern = r'([+]?\d?[-+(\s]?\d{3}[-).\s]*\d{3}[\s.-]?\d{4})'
input_num = input("Enter a number - ")
res = re.search(pattern,input_num)
if res:
    print("valid")
else:
    print("Not valid Number")


# 2. WAP to get the Social Links, Email & Contacts details of a website on user input.
input_val = input("Enter Website Link ---:")
pattern = r'^https://[\w.]+$'
ans = re.search(pattern,input_val)
if ans:
    print("Website Link : ",input_val)
    name = input_val.split('//')[1]
    print("Social Links :")
    print("https://www.facebook.com/"+(name)+"/")
    print("https://www.linkedin.com/company/"+(name).replace('.','-')+"/")
    print()
    print("Email/s :")
    print("support@"+name)
else:
    print("Envalid website Name")

