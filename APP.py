import streamlit as st

#TITLE
st.title("Title")
#Header
st.header("Header")
#subheader
st.subheader("subheader")
#text
st.text("this is swapna")

#markdown for different levels of heading using #

st.markdown('#hi')
st.markdown('## hi')
st.markdown('### hi')
st.markdown('#### hi')
st.markdown('##### hi')


#success
st.success("success message")
#info
st.info("info")
#warning and error
st.warning("warning")
st.error("error")
st.exception(ZeroDivisionError("cant divide by 0")) #exception
st.help(ZeroDivisionError) #detailed information about any function u provide in help
#display a wide range of data types - formatting the content and displays appropriately
st.write("range(2,20)")
st.write(range(2,20))
st.write(1+2+3+4)
#code if u want to display a code in a beautiful way

st.code('x = 10\n'
 'for i in range(1,10):\n'
 '\tprint(i)')

#checkbox
st.checkbox("Male")
if(st.checkbox("Female")):
    st.write("you are a female")


#radiobutton

radiobutton = st.radio('select your choice:',('Male','Female','Other'))
if(radiobutton == "Male"):
    st.write("You are a Male")
elif(radiobutton == "Female"):
    st.write("You are a Female")
if(radiobutton == "Other"):
    st.write("You are a Other Gender")


st.subheader("selectbox")

sb = st.selectbox("select : ",['Data Analysis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("you selected: ",sb)

st.subheader("multi select box")
sb = st.multiselect("select : ",['Data Analysis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("you selected: ",len(sb),"courses")


st.subheader("button")
if(st.button("click me ")):
    st.write("thanks for clicking me!!!")

st.subheader("slider")
v = st.slider("volume:",0,100,step=2)
st.write("The selected volume for soundbar is: ",v)


st.subheader("text area")
st.text_area("tell me something interesting about yourself in 100 words only",max_chars = 100)

#input text,number,date and time
st.subheader("input text")
uname = st.text_input("Enter Username:")
password = st.text_input("Enter your password:",type = 'password')

number = st.number_input("Enter a number from 1 to 100",1,100)
date = st.date_input("enter date")
time= st.time_input("enter time")
