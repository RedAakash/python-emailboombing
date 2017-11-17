import smtplib, webbrowser, getpass
def get_mail():
    servicesavailable = ['hostmail', 'gmail', 'yahoo', 'outlook']
    while True:
        mail_id = raw_input("Email: ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in servicesavailable:
                return mail_id, sp
                break
            else:
                print("We Don't Provide Service For " + sp)
                print("We Provide Service Only For: Hotmail,Outlook,Yahoo & Gmail")
                continue
        else:
            print("Invalid Email Type again Dude!!!!")
            continue
def set_smtp_domain(serviceprovider):
    if serviceprovider == "gmail" or serviceprovider == "Gmail":
        return 'smtp.gmail.com'
    elif serviceprovider == "outlook" or serviceprovider == "hotmail":
    	return 'smtp-mail.outlook.com'
    elif serviceprovider == "yahoo" or serviceprovider == "Yahoo":
    	return 'smtp.mail.yahoo.com'
print("Welcome You Cen Send Email easliy using this Application")
print("This Program Made By RedAakash YouTube Channel.")
print("Please enter your email and password: ")
e_mail , serviceprovider = get_mail()
password = getpass.getpass("Password: ")
while True:
    try:
        smtpDomain = set_smtp_domain(serviceprovider)
        connection = smtplib.SMTP(smtpDomain, 587)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail, password)
    except:
        if serviceprovider == "gmail" or serviceprovider == "Gmail":
            print("Login unsuccessfull, there are two possible reasons: ")
            print("1.) You typed wrong username or password")
            print("2.) You are using gmail there is an option in gmail 'allow less SecureApps")
            print("Do you want us to open a webpage from where you can enable this option")
            answer = raw_input("Yes or No ? : ")
            if answer == "yes" or answer == "Yes":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
            elif answer == "no" or answer == "No":
                print("We won't open webpage for you, You can go to 'https://myaccount.google.com/lesssecureapps'")
            print("Please ReType Your E-mail and Password also")
            e_mail, serviceprovider = get_mail()
            password = getpass.getpass("Password: ")
            continue
        else:
            print("Login unsuccessfull, Most possibly you typed wrong username or passord")
            print("Please ReType Your E-mail and Password")
            e_mail, serviceprovider = get_mail()
            password = getpass.getpass("Password: ")
            continue
    else:
        print("Login Successfull Great Dude!!")
        break
print("Please Enter Receiver's E-mail address Details")
receiveraddress, receiverSP = get_mail()
print("Now please type Subject and Message")
Subject = raw_input("Subject: ")
message = raw_input("Message: ")
boombing = int(input("Enter your value: "))
i = 1
while boombing != i:
	i = i + 1
	connection.sendmail(e_mail  , receiveraddress , ("Subject: " + str(Subject) + "\n\n" + str(message)))
	print("E-mail send successfull'(*.^)'")
	print("Made By RedAakash YouTube Channel")
	print("That's a URL 'https://www.youtube.com/redaakash' . If you want to contact me just open this URL")
	print("Thanks for using my Application")
connection.quit()
