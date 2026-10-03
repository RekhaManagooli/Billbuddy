import streamlit as st
from PIL import Image
from google import genai
from twilio.rest import Client
import json
from prompts import BILL_READING_PROMPT

st.set_page_config(page_title="BillBuddy", page_icon="🧾")

st.title("🧾 BillBuddy")
st.subheader("Bill Tracker & Splitter")

# Gemini connection
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
twilio_client=Client(
    st.secrets["TWILIO_ACCOUNT_SID"],
    st.secrets["TWILIO_AUTH_TOKEN"]
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

    if st.button("🔍 Read Bill"):

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

                st.success("Bill read successfully! ✅")

            except Exception as e:

                st.error("Unable to read the bill.")

                st.code(str(e))


# Display bill
if "bill_data" in st.session_state:

    bill_data = st.session_state["bill_data"]

    st.subheader("📋 Bill Details")

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
        f"💰 Total Bill: ₹{total_bill:.2f}"
    )

    st.divider()

    # Bill splitting
    st.subheader("➗ Split Your Bill")

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
            f"👥 Each person pays: ₹{amount_each:.2f}"
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
                "✅ Custom split is correct!"
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

st.subheader("📱 Send Bill Split to WhatsApp")

if st.button("📲 Send to WhatsApp"):

    try:
        total_bill = float(bill_data.get("total", 0))

        message_text = f"""
🧾 BillBuddy Bill Summary

💰 Total Bill: ₹{total_bill:.2f}

➗ Split Method: {split_method}
"""

        if split_method == "Equal Split":
            message_text += f"""
👥 Number of People: {int(people)}
💵 Amount per Person: ₹{amount_each:.2f}
"""

        else:
            message_text += "\n👥 Custom Split:\n"

            for i, amount in enumerate(custom_amounts):
                message_text += f"Person {i + 1}: ₹{amount:.2f}\n"

        message = twilio_client.messages.create(
            from_=st.secrets["TWILIO_WHATSAPP_NUMBER"],
            to=st.secrets["TWILIO_TO_NUMBER"],
            content_sid=st.secrets["TWILIO_CONTENT_SID"]
        )

        st.success("✅ Bill split sent to WhatsApp!")
        st.write("Message SID: ",message.sid)
        st.write("Initial status: ",message.status)

    except Exception as e:
        st.error("❌ Unable to send WhatsApp message.")
        st.code(str(e))