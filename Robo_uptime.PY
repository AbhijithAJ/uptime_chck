# import sys
# sys.setrecursionlimit(3000)

import requests
import time
import datetime
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = input('Enter Emai:')
password = input('Enter password')
send_to_email = input('enter target mailid')
subject = 'ROBO_UPTIME'
# message = 'message'  # ------------------------------------------------------------
lst = []
settime = 60 #float(input("enter time"))  # in sec
count = 0

while True:
    try:
        def send_mail(Message):
            try:
                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject
                msg.attach(MIMEText(Message, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                try:
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                except Exception as a:
                    print(a)
            except Exception as a:
                print('\n---------------------------------------------------NOTE------------------------------------------------------')
                print("Error:", a, datetime.datetime.now())
                print('\n**************************************************************************************')
                print('FAILD TO SEND MAIL \n ')
                print(Message)
                print('\n**************************************************************************************')
                print('\n-------------------------------------------------------------------------------------------------------------')
            finally:
            	return result
        def req(site):
            # print(site)
            if site[:8] == 'https://' or site[:7] == 'http://':
                pass
            else:
                site = 'https://' + site
                # print('site--',site)
            try:
                r = requests.get(site)
                code = r.status_code
                code = str(code)
                
                if code == '200':
                    #print(r)
                    #print(r.content)
                    pass
                else:
                    currentDT = datetime.datetime.now()
                    currentDT = str(currentDT)
                    # print('DATE AND TIME ',currentDT)
                    Message = 'The monitor ' + site + 'is backup(HTTP 200 - OK) is down at' + currentDT + '     \nHave a great day,     \nFor any further Query please fell free to contact ar info@gybervie.com'
                    print('\nSITE DOWN :\n', site + " is Down at " + currentDT + " Response code: " + code)
                    #send_mail(Message)
                    for i in range(10):
                        r = requests.get(site)
                        code = r.status_code
                        code = str(code)
                    if code == '200':
                        print(code)
                       
                        pass
                    else:
                        currentDT = datetime.datetime.now()
                        currentDT = str(currentDT)
                        print('DATE AND TIME ', currentDT)
                        Message = '*The monitor ' + site + 'is backup(HTTP 200 - OK) is down at' + currentDT + '     \nHave a great day,     \nFor any further Query please fell free to contact ar info@gybervie.com'
                        print('\nSITE DOWN FOR ANOTHER 10 IMIDIATE REQUESTS : \n',
                              site + " is Down at " + currentDT + " Response code: " + code)
                        send_mail(Message)
            except Exception as a:
                a = str(a)
                print('Exception:', a)
                print('----ERROR IN REQUESTING SITE----'+site+" ", datetime.datetime.now())

        def startit():
            while True:
                global count
                global lst
                print("Running "+str(count)+" "+str(datetime.datetime.now()),end ='\r')                
                if count > 500:
                    count = 0
                    time.sleep(3)
                    break
                count += 1
                #sys.stdout.write("\r%d%%" % count)
                #sys.stdout.flush()
                prvlst = lst
                lst = []
                try:
                    with open('siteslist.txt', 'rb') as f:
                        for i in f:
                            site = str.strip(i.decode())
                            if not '.' in site or not site:
                                # print(site)
                                pass
                            else:
                                lst.append(site)
                    if lst != prvlst and count != 1:
                        print(lst)
                        print("checking all sites simeltaniously")
                    if count == 1:
                    	print(lst)
                    	print("checking all sites simeltaniously")
                    start_time = time.time()
                    for i in lst:
                        req(i)
                    exicution_time = time.time() - start_time
                    if exicution_time >= settime:
                        pass
                    else:
                        time.sleep(settime - exicution_time)
                except Exception as a:
                    print(a, datetime.datetime.now())
        startit()
    except Exception as a:
        print('______________________________________________________________________________________________________')
        print(a)
        print('______________________________________________________________________________________________________')
