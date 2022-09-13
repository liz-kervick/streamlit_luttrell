import streamlit as st
import pandas as pd
import numpy as np 

    
basepath= "/Users/lizbartoshevich/Documents/streamlit_site/"
rawpath= "/files/"
filename='/realdonaldtrump_nolink.csv'

df=pd.read_csv(basepath+rawpath+filename)


st.title('Donald Trump Twitter Analysis')
st.header('Analyzing Donald Trump Tweets - A Project in Linguistic Anthropology and Digital Humanities')

st.warning('This page will be expanded in future to interactively analyze the below data.') 

st.dataframe(df[['date','content','retweets','favorites','mentions','hashtags']])



