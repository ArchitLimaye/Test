import streamlit as st
st.header('Login Page', divider='rainbow')
st.title(":red[Please Login]:")
email=st.text_input("Enter Email:")
password=st.text_input("Enter Password:")
btn=st.button("Login")
if btn:
    if email=="archit@gmail.com" and password=="235656":
        st.success("Done")
        st.title('Welcome :sunglasses:')
        st.balloons()
    else:
        st.error("Login Failed")
        st.write("Attempts!:")
        st.write(attempt)
