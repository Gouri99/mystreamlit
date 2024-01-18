import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://images.pexels.com/photos/1212693/pexels-photo-1212693.jpeg?auto=compress&cs=tinysrgb&w=300')
st.title('New Technologies')
st.header('Hi Gouri Soni')
st.text('This is a tutorial on Streamlit Library')
if (mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video('https://youtu.be/KOmGPNS-YM8?si=vqIGmoHVWjBhv6of')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input('Choose Date of Birth')
        marks=st.slider('Choose Marks')
        k=st.form_submit_button('Submit Form')
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Downloads'):
    st.header('Downloads')
    st.download_button('Download Now','hello this is the downloaded data','data.txt')

