import requests
from bs4 import BeautifulSoup
import smtplib
#Read the README file to see the variables need to be changed by the user
#Replace <URL> with the URL of the product page from Amazon
URL = '<URL>'
#Replace <price> with the price limit you want to set for the product
price_limit = <price>

#Google "My user agent" and replace 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36' from the below header to your user agent if it is different
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

#Gets the price of the product from product page
def check_price():
    global title, price
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title_old = soup.find(id = "productTitle").get_text()
    title = non_ascii(title_old)
    try:
        price_str = soup.find(id = "priceblock_ourprice").get_text()
        price_list = []
        for num in price_str:
            if num.isdigit():
                price_list.append(num)
        price_list.pop()
        price_list.pop()
        price_strings = [str(price_integer) for price_integer in price_list]
        a_string = "".join(price_strings)
        price = int(a_string)

        if price < price_limit:
            send_mail()

        print(title.strip())
        print(price)
    except:
        print("The product is out of stock")
        
#Removes Non-ASCII characters from the title of the product
def non_ascii(message):
    return ''.join(i for i in message if ord(i)<128)

#Function to send a mail (Sender must send using Gmail, or can change the parameters to match their own mail hosting service)
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #Replace <sender-mail-id> with the sender's email ID and <sender-password> with the sender's mail ID password or a 2FA password for that mail.
    sender_mail = '<sender-mail-id>'
    sender_pass = '<sender-password>'
    
    #Replace <receiver-mail-id> with the receiver's email ID
    receiver_mail = '<receiver-mail-id>'
    server.login(sender_mail, sender_pass)
    subject = 'Price down alert'
    body = 'The price of the product '+title.strip()+' has reduced to Rs.'+str(price)+'. The link of the product is: '+URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        sender_mail,
        receiver_mail,
        msg
    )
    print("Mail sent successfully")
    server.quit()
    
check_price() #Nice
