import re
import csv

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
print("You can run this application from the directory where your csv file from linkedin is saved or downloaded.")
file_name = str(input("Enter the full name of your file and the extension, like: 'Connections.csv': "))
#email_file_name = str(input("Enter the name of your file without any the extension, like: 'Connections_emails.csv': "))
with open(file_name, "rt", encoding="utf-8") as new_file:
    all_records = csv.reader(new_file, delimiter=',')
    email_count = 0
    email_address = []
    
    for row in all_records:
        if(re.search(regex,row[0]) or re.search(regex,row[1]) or re.search(regex,row[2])):
            valid_email = f'\n{row[0]}, {row[2]}'
            email_count = email_count + 1
            email_address.append(valid_email)
            #print(valid_email)
            
    with open("Connections_emails.txt", "wt") as nemails:
        nemails.writelines(email_address)
        print("All saved...")
    print(email_count, " emails saved.")
