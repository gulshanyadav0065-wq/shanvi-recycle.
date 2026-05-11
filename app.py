import streamlit as st
import urllib.parse

# App Settings
st.set_page_config(page_title="Shanvi Recycle", page_icon="♻️")
st.title("♻️ Shanvi Recycle")
st.markdown("### **Owner: Pintu Trader**")
st.write("---")

# Rates (Yahan se aap rate badal sakte hain)
with st.sidebar:
    st.header("Admin Panel")
    rate_news = st.number_input("Newspaper Rate (₹/kg)", value=20)
    rate_copy = st.number_input("Copy/Books Rate (₹/kg)", value=15)
    rate_gatta = st.number_input("Gatta Rate (₹/kg)", value=12)

st.header("Aaj ke Taaza Rate")
c1, c2, c3 = st.columns(3)
c1.metric("Newspaper", f"₹{rate_news}")
c2.metric("Copy/Books", f"₹{rate_copy}")
c3.metric("Gatta", f"₹{rate_gatta}")

st.write("---")
st.header("Pickup Request Bheinjein")

# User Form
with st.form("pickup_form"):
    name = st.text_input("Aapka Naam")
    phone = st.text_input("Mobile Number")
    items = st.multiselect("Kya bechna hai?", ["Newspaper", "Copy/Books", "Gatta"])
    weight = st.text_input("Approx Weight (kg)")
    addr = st.text_area("Pura Address")
    
    submit = st.form_submit_button("WhatsApp par Request Bheinjein")
    
    if submit:
        if name and phone and addr:
            # Aapka WhatsApp Number (Yahan apna number 91 ke saath likhein)
            my_number = "918448192949" # <--- Yahan apna real number dalein
            
            # Message taiyar karna
            message = f"Nayi Pickup Request!\n\nNaam: {name}\nPhone: {phone}\nMaal: {', '.join(items)}\nWazan: {weight}kg\nAddress: {addr}"
            
            # WhatsApp URL link banana
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{my_number}?text={encoded_message}"
            
            st.success("Details taiyar hain! Niche button par click karke Pintu Trader ko WhatsApp karein.")
            st.link_button("Confirm on WhatsApp", whatsapp_url)
        else:
            st.warning("Kripya saari details bharein!")
