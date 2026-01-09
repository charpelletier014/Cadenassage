#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
from streamlit_jupyter import StreamlitPatcher
StreamlitPatcher().jupyter() # Enable Jupyter-compatible wrappers


# In[11]:


from streamlit_pdf_viewer import pdf_viewer

pdf_viewer(
input="Cadenassage.pdf",
width=700,
height=1000,
zoom_level=1.2, # 120% zoom
viewer_align="center", # Center alignment
show_page_separator=True # Show separators between pages
)


# In[ ]:




