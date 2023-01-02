import streamlit as st
import pandas as pd 
from datetime import datetime

st.header('Encoding to UTF8')
uploaded_file = st.file_uploader("Choose your csv:",)
df = pd.read_csv(uploaded_file)
text = st.subheader('')
text.subheader('Done! You can download it now:')

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8-sig')

csv = convert_df(df)
today = datetime.today()
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name=f'encoded-{str(today)}.csv',
    mime='text/csv',
)


