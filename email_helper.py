# -*- coding: utf-8 -*-
import csv
import re

def find_email(body):
    email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", body)
    try:
        if email[0] == "marketing@jdl-us.com":  
           if email[1] not in email_list:
                email_list.append(email[1])
        elif email[0] not in email_list:
            email_list.append(email[0])
    except IndexError:
        return

def jdl_or_jd(row, body,undefine, switch):
    if "The mail system" in body:
        find_email(body)
    elif "The following addresses had permanent fatal errors" in body:
        find_email(body)
    elif "Delivery has failed to these recipients or groups" in body:
        find_email(body)
    elif "Your message couldn't be delivered" in body:
        find_email(body)
    elif "Your message to " in body and "couldn't be delivered." in body:
        find_email(body)
    elif "The following message to " in body and " was undeliverable." in body:
        find_email(body)
    elif "A message that you sent could not be delivered to one or more of its" in body:
        find_email(body)
    elif "Delivery to the following recipient" in body and "failed permanently:" in body:
        find_email(body)
    elif "Your message wasn't delivered to " in body:
        find_email(body)
    elif "did not reach the following recipient(s):" in body:
        find_email(body)
    elif "Message blocked " in body:
        find_email(body)
    elif "was not delivered to:" in body:
        find_email(body)
    elif "I'm sorry to inform you that the message below could not be delivered." in body:
        find_email(body)
    elif "This is a delivery failure notification message indicating that" in body:
        find_email(body)
    elif "Delivery has failed to these recipients or distribution lists:" in body:
        find_email(body)
    elif "I'm sorry to have to inform you that your message could not" in body:
        find_email(body)
    elif "Failed to deliver to \'" in body:
        find_email(body)
    elif "I was unable to deliver your message to the following addresses:" in body:
        find_email(body)
    elif "no longer" in body or "NO LONGER" in body:
        if row[0] not in email_list:
            email_list.append(row[0])
    elif "Thank you" in body:
        pass
    elif "Hello" in body:
        pass
    elif "rejected by system" in body:
        pass
    elif "Your email is undeliverable.  The email address used is invalid." in body:
        pass
    elif "The intended recipient did not receive your email. For" in body:
        pass
    elif "out of the office" in body:
        pass
    elif "out of office" in body:
        pass
    elif "out-of-office" in body:
        pass
    elif switch == 'jd':
        if "MAILER-DAEMON@" not in row[3] and "postmaster@" not in row[3]:
            find_email(body)
        else:
            undefine.append(row[3].replace('MAILER-DAEMON@','').replace('postmaster@',''))
    else:
        undefine.append(row[0] + '\n' + row[1])


    
    
    
    
    
    
    
email_list=["marketing@jdl-us.com"]
undefine=[]
try:
    with open("jdl.csv", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            try:
                body = row[1]
            except:
                line_count += 1
                continue
            if line_count >= 8:
                if len(body) > 110 and len(body) < 5000:
                    jdl_or_jd(row, body, undefine, "jdl")
                
            elif line_count > 8:
                break
            line_count += 1
    csv_file.close()
except:
    print("Filename must be jd.csv")
email_list.pop(0)

with open('Email list.txt','w', encoding="utf8") as f:
    for i in email_list:
        f.write(i)
        f.write('\n')
f.close()
with open('Undefine.txt','w',encoding="utf8") as f:
    for i in undefine:
        f.write(i)
        f.write('\n')
        f.write('\n----------------------------------------------------------------------------------------------------------------------------------------\n')
f.close()

