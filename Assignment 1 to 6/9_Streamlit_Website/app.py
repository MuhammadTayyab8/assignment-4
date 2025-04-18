import streamlit as st

# Page config
st.set_page_config(
    page_title="Quick Website",
    page_icon="🌐",
    layout="centered"
)


# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go To", ["Home", "About", "Contact"])

# Home Page
if section == "Home":
    st.title("👋 Welcome to My Streamlit Website")

    with st.container():
        st.subheader("Let’s get to know you!")
        name = st.text_input("Enter your name:")
        if name:
            st.success(f"Nice to meet you, {name}!")
        st.write("This is a simple multipage website using Streamlit.")

# About Page
elif section == "About":
    st.title("📖 About This Website")
    st.markdown("""
        This is a minimal multi-page app made with **Streamlit**.
        
        ✨ It's fast, simple, and runs in your browser!  
    """)
    st.write("### Projects")
    st.write("Data Sweeper \n\n Link: [https://data-sweeper-1234.streamlit.app/]\n\n")
    st.write("Password Generator \n\n Link: [https://password-generator-tayyab.streamlit.app/]\n\n")

    st.write("Built by Muhammad Tayyab \n\n Github: [https://github.com/MuhammadTayyab8]")


# Contact Page
elif section == "Contact":
    st.title("📬 Get in Touch")
    st.markdown("Fill out the form below, and we'll get back to you!")

    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")
    if st.button("Send Message"):
        if name and email and message:
            st.success("✅ Message sent successfully!")
        else:
            st.warning("⚠️ Please fill in all the fields.")

