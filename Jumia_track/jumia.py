import requests
from bs4 import BeautifulSoup
import smtplib
import getpass
import stdiomask
import time

URL = input('Enter the URL of the product here: \n')

user = input('Enter your user agent here: \n')

headers = {
    "User-Agent": user
}

page = requests.get(URL, headers = headers)

def check_price():    
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find_all("h1")[0].get_text()
    price = soup.find('span', {'class': '-b -ltr -tal -fs24'}).get_text()

    real_price = int(price[4:10].replace(',',''))
    
    price = int(input('enter your desired price:\n'))

    if (real_price > price):
        send_mail()

    print(title)
    print(real_price)

def send_mail():
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    email = input('Enter your email address:\n')

    password = stdiomask.getpass()
    
    server.login(email, password)

    subject = 'Price of your product favourable!'

    body = f'The price of the product you were waiting for is finally here!! Check the Jumia link of the product you were interested in by clicking the following link:{URL}'

    msg = f"Subject: {subject}\n\n{body}"
    
    recepient = input('Enter alternative email to send mail to: \n')

    server.sendmail(
        email,
        recepient,
        msg
    )

    print('We got the product at a cheaper price!!')

    server.quit()


while(True):
    check_price()
    time.sleep(86400)
