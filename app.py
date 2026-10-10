import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PIL import Image
from google import genai
import json
from prompts import BILL_READING_PROMPT

st.set_page_config(page_title="BillBuddy", page_icon="🧾")

st.title(" BillBuddy")
st.subheader("Welcome to BillBuddy!")

user_name = st.text_input("Enter your name")
user_email = st.text_input("Enter your email ID")

if user_name:
    st.success(
        f"Hi {user_name}!  Upload your bill image to get the details and split your bill easily."
    )

st.subheader("Bill Tracker & Splitter")

# Gemini connection
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Upload bill
uploaded_file = st.file_uploader(
    "Upload your bill image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Bill",
        width="stretch"
    )

    if st.button(" Read Bill"):

        with st.spinner("Reading your bill..."):

            prompt = BILL_READING_PROMPT

            try:

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=[prompt, image]
                )

                result = response.text.strip()

                # Remove markdown JSON markers if Gemini adds them
                result = result.replace("```json", "")
                result = result.replace("```", "")
                result = result.strip()

                bill_data = json.loads(result)

                st.session_state["bill_data"] = bill_data

                st.success("Bill read successfully! ")

            except Exception as e:

                st.error("Unable to read the bill.")
                st.code(str(e))


# Display bill
if "bill_data" in st.session_state:

    bill_data = st.session_state["bill_data"]

    st.subheader(" Bill Details")

    items = bill_data.get("items", [])

    # Create table
    table_data = []

    for item in items:

        table_data.append({
            "Item": item.get("item", ""),
            "Quantity": item.get("quantity", 1),
            "Price": f"₹{float(item.get('price', 0)):.2f}",
            "GST": f"₹{float(item.get('gst', 0)):.2f}",
            "Subtotal": f"₹{float(item.get('subtotal', 0)):.2f}"
        })

    st.table(table_data)

    # Total
    total_bill = float(bill_data.get("total", 0))

    st.success(
        f" Total Bill: ₹{total_bill:.2f}"
    )

    st.divider()

    # Bill splitting
    st.subheader(" Split Your Bill")

    split_method = st.radio(
        "Choose splitting method:",
        ["Equal Split", "Custom Split"]
    )

    # Equal split
    if split_method == "Equal Split":

        people = st.number_input(
            "Number of people",
            min_value=1,
            max_value=50,
            value=2,
            step=1
        )

        amount_each = total_bill / people

        st.success(
            f" Each person pays: ₹{amount_each:.2f}"
        )

    # Custom split
    else:

        people = st.number_input(
            "Number of people",
            min_value=1,
            max_value=50,
            value=2,
            step=1
        )

        st.write("Enter the amount for each person:")

        custom_amounts = []

        for i in range(int(people)):

            amount = st.number_input(
                f"Person {i + 1}",
                min_value=0.0,
                step=10.0,
                key=f"custom_person_{i}"
            )

            custom_amounts.append(amount)

        custom_total = sum(custom_amounts)

        st.write(
            f"Entered total: ₹{custom_total:.2f}"
        )

        difference = total_bill - custom_total

        if abs(difference) < 0.01:

            st.success(
                " Custom split is correct!"
            )

        elif difference > 0:

            st.warning(
                f"₹{difference:.2f} is still remaining."
            )

        else:

            st.error(
                f"₹{abs(difference):.2f} is more than the bill total."
            )
            st.divider()
st.subheader(" Send Bill to Your Email")

if st.button(" Send Bill to My Email"):

    try:
        sender_email = st.secrets["GMAIL_ADDRESS"]
        sender_password = st.secrets["GMAIL_APP_PASSWORD"]

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = user_email
        message["Subject"] = "BillBuddy - Bill Summary"

        message_text = f"""
Hello {user_name},

Here is your BillBuddy bill summary.

Total Bill: ₹{total_bill:.2f}

Split Method: {split_method}
"""

        if split_method == "Equal Split":
            message_text += f"""
Number of People: {int(people)}
Amount per Person: ₹{amount_each:.2f}
"""

        else:
            message_text += "\nCustom Split:\n"

            for i, amount in enumerate(custom_amounts):
                message_text += f"Person {i + 1}: ₹{amount:.2f}\n"

       
        # Connect to Gmail
        message.attach(MIMEText(message_text,"plain"))
        with smtplib.SMTP_SSL("smtp.gmail.com",465,timeout=30)as server:
            server.login(sender_email,sender_password)
            server.send_message(message)
        st.success("Bill summary sent successfuly to your email!")
    except Exception as e:
                st.error(f"Unable to send email:{e}")
     















    