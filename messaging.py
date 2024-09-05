import streamlit as st
import pywhatkit as kit

def send_message_via_whatsapp_desktop(phone_number, message):
    try:
        # Send the message via WhatsApp Desktop using pywhatkit
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
        return "Message sent successfully!"
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit interface
st.title("WhatsApp Message Sender via Desktop")

phone_number = st.text_input("Phone Number (with country code, e.g., +1234567890)")
message = st.text_area("Message")

if st.button("Send"):
    if phone_number and message:
        if not phone_number.startswith("+"):
            st.error("Please include the country code in the phone number (e.g., +1234567890).")
        else:
            result = send_message_via_whatsapp_desktop(phone_number, message)
            st.success(result)
    else:
        st.error("Please provide both phone number and message.")
