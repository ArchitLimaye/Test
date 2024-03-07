import streamlit as st
email=st.text_input("Enter Email:")
password=st.text_input("Enter Password:")
btn=st.button("Login")
if btn:
    if email=="archit@gmail.com" and password=="235656":
        st.success("Done")
        st.balloons()
    else:
        st.error("Login Failed")