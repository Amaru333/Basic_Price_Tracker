# Basic_Price_Tracker
Tracks price of an Amazon product and sends a mail if the price is less than that of what user had set.
Variables that needs to be changed by the user in the script:
  1. Replace <URL> with the URL of the product page from Amazon (Line: 6)
  2. Replace <price> with the price limit you want to set for the product (Line: 8)
  3. Google "My user agent" and replace 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36' from the below header to your user agent if it's different from yours. (Line: 11)
  4. Change the parameters of SMTP to the sender's mail service (Change it if sender is not using Gmail to send the mails). (Line: 46)
  5. Replace <sender-mail-id> with the sender's email ID (Line: 51)
  6. Replace <sender-password> with the sender's mail ID password or a 2FA password set for that mail. (Line: 52)
  7. Replace <receiver-mail-id> with the receiver's email ID (Line: 55)
