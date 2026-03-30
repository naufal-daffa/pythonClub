import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel('Adidas.xlsx')
st.set_page_config(page_title="Adidas Sales Dashboard", layout="wide")
st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image(image=Image.open('image.png'), width=100)
    
html_title = """
<style>
.title{
    font-size: 40px;
    font-weight: bold;
    color: #1E90FF;
    text-align: center;
}
</style>
<center><h1 class="title">Adidas Sales Dashboard</h1></center>
"""

with col2:
    st.markdown(html_title, unsafe_allow_html=True) 
    
col3, col4, col5 = st.columns([0.1, 0.45, 0.45])

with col3:
    box_date = str(datetime.datetime.now().strftime('%d %B %Y'))
    st.write(f"**Date :** {box_date}")
    
with col4:
    fig = px.bar(df, x='Retailer', y='TotalSales', labels={"TotalSales": "Total Sales {$}"}, color='Product', title='Sales by Product', template='gridon',height=500)
    st.plotly_chart(fig, use_container_width=True)