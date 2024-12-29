import streamlit as st
import time as t

st.title("HACKED")

st.header("hacking device.....")

progress_bar = st.progress(0)
st.caption("Copying data")

for i in range(0, 100):
    t.sleep(0.05)
    progress_bar.progress(i)

st.success("Device hacked")


with st.spinner("Wait"):
    t.sleep(5)

st.title("Fist Website")

st.header("Welcome to Data Analysis")

st.subheader("Data Manipulation")

st.info("This page will guide you how you can win in Data analysis field")

st.warning("Do not share or use your password")

st.write("Here is the Introduction")

st.error("This website may give you errors")

st.success("Taskcompleted")

st.markdown("*streamlit*")

st.caption("Welcome")

st.latex(r"a + bx^3 + c")

with st.sidebar:
    st.title("Abc")
    
    
    
st.sidebar.text_input("Enter your name")
st.sidebar.text_input("Enter your password")
st.sidebar.button("Submit")



st.markdown("🤖 Congratulations")
st.balloons()