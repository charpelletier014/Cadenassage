#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st

st.title("PDF Viewer Example")

# 2. Display a PDF from a local file (must be opened in binary mode)
with open("Cadenassage.pdf", "rb") as pdf_file:    
    PDFbyte = pdf_file.read()
    
st.download_button(
    label="beeg",
    data=PDFbyte,
    file_name="Cadenassage.pdf",
    mime="application/pdf"
)



# In[ ]:




