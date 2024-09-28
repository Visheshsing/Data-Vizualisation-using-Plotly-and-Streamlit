import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide' ,page_title = 'India ka Vizualisation')
df = pd.read_csv('india.csv')
list_of_states= list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India ka Viz')

selected_states = st.sidebar.selectbox('Select a  State', list_of_states)
Primary = st.sidebar.selectbox('Select Primary Parameter' ,sorted(df.columns))
Secondary = st.sidebar.selectbox('Select Secondary Parameter' ,sorted(df.columns))

plot = st.sidebar.button('Plot Graph')

if plot:




    if selected_states == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size = Primary , color = Secondary,zoom=3, mapbox_style="carto-positron" , hover_name='District')
        st.plotly_chart(fig)
    else:  
        state_df = df[df['State']] == selected_states
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size = Primary , color = Secondary,zoom=3, mapbox_style="carto-positron", hover_name='District')
        st.plotly_chart(fig)