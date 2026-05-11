import streamlit as st

# App Header
st.set_page_config(page_title="Shanvi Recycle", page_icon="♻️")
st.title("♻️ Shanvi Recycle")
st.markdown("### **Owner: Pintu Trader**")
st.write("---")

# Admin Section for Rates
with st.sidebar:
    st.header("Admin Panel")
    st.info("Pintu bhai, yahan se rate badlein")
    rate_news = st.number_input("Newspaper Rate (₹/kg)", value=20)
    rate_copy = st.number_input("Copy/Books Rate (₹/kg)", value=15)
    rate_gatta = st.number_input("Gatta Rate (₹/kg)", value=12)

# User View
st.header("Aaj ke Taaza Rate")
c1, c2, c3 = st.columns(3)
c1.metric("Newspaper", f"₹{rate_news}")
c2.metric("Copy/Books", f"₹{rate_copy}")
c3.metric("Gatta", f"₹{rate_gatta}")

st.write("---")
st.header("Pickup Request Bheinjein")

with st.form("pickup_form"):
    name = st.text_input("Aapka Naam")
    phone = st.text_input("Mobile Number")
    items = st.multiselect("Kya bechna hai?", ["Newspaper", "Copy/Books", "Gatta"])
    addr = st.text_area("Pura Address aur Landmark")
    
    submit = st.form_submit_button("Request Bheinjein")
    
    if submit:
        if name and phone and addr:
            st.success(f"Dhanyawad {name}! Pintu Trader ko aapki request mil gayi hai.")
            st.balloons()
        else:
            st.warning("Kripya saari details bharein!")
