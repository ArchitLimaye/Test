import streamlit as st
st.title("Login Page")
st.title(":red[Please Login]:")
email=st.text_input("Enter Email:")
password=st.text_input("Enter Password:")
btn=st.button("Login")
if btn:
    if email=="archit@gmail.com" and password=="235656":
        st.success("Done")
        st.balloons()
    else:
        st.error("Login Failed")
