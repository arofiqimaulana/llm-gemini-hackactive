import streamlit as st

st.title("Aplikasi Ku")
st.markdown("Ini adalah aplikasi buatan ku")

username = st.text_input("Nama")
user_age = st.number_input("Umur")
submit_button = st.button("Submit")
if submit_button:
    st.markdown(f"Hello {username} ")
    st.markdown(f"Umur {user_age} tahun")