import smtplib
from email.mime.text import MIMEText

SENDER = "rekhamanaguli123@gmail.com"
APP_PASSWORD = "fcqztavselfjyqzc"   # 16 chars, no spaces
RECEIVER = "rekhamanaguli123@gmail.com"

msg = MIMEText("Test mail from BillBuddy", "plain", "utf-8")
msg["From"] = SENDER
msg["To"] = RECEIVER
msg["Subject"] = "SMTP test"

with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as s:
    s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(SENDER, APP_PASSWORD)
    s.send_message(msg)
print("SENT")