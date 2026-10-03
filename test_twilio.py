import streamlit as st

from twilio.rest import Client
# Read Twilio credentials from secrets.toml
account_sid=st.secrets["TWILIO_ACCOUNT_SID"]
auth_token=st.secrets["TWILIO_AUTH_TOKEN"]
content_sid=st.secrets["TWILIO_CONTENT_SID"]
twilio_whatsapp_number=st.secrets["TWILIO_WHATSAPP_NUMBER"]
your_whatsapp_number=st.secrets["TWILIO_TO_NUMBER"]

# connect to twilio
client= Client(account_sid,auth_token)

#send test whatsapp message
message= client.messages.create(from_=twilio_whatsapp_number,to=your_whatsapp_number,content_sid=content_sid)
print("Message sent successfully!")
print("Message SID: ",message.sid)




