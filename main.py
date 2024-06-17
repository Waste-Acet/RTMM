import streamlit as st
import index1

#from PAGE2 import PAGE2

# Define user credentials (you can replace this with a more secure authentication method)
#st.set_page_config(page_title="Powder coating", page_icon="lls.png",layout = 'wide')
VALID_USERNAME = "u"
VALID_PASSWORD = "pass"
#st.set_page_config(page_title="Powder coating", page_icon="lls.png")

def login():
    with open("style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

 
    st.title("LLS-POWDER COATING DEPARTMENT!")
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True

            st.rerun() 
           # int(a=5) 
           #Rerun the app to reflect the logged-in state
           # page1()
           # index()
            return a
        else:
            st.error("Invalid username or password")

def main():
    #st.title("LLS-POWDER COATING DEPARTMENT!")

    # Check if user is logged in
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login()
       # index()
        return

    #index()
  #  st.success("welome to OEE!")

    # Add navigation buttons
    page = st.sidebar.radio("LLS-U1", ["OEE"])
    #page = st.sidebar.radio("LLS-U1", ["OEE", "Conveyor"])

    if page == "OEE":
        index1.index1()
        st.write("This is Page 1")
    #if a==5:
      #  index()

       # page1()
      #  st.write("This is Page 1")


   # elif page == "Conveyor":
     #   PAGE2()
     #   st.write("This is Page 2")


if __name__ == "__main__":
    main()
