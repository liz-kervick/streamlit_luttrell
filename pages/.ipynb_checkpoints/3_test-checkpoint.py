import streamlit as st
import pandas as pd
import numpy as np

# FORMAT TITLE
st.title('test page')

st.markdown('Narcissus Luttrell: Brief Historical Relation')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Summary','Year-By-Year','Mapping','Personal Pronouns','Catholicism'])
#SET PATHS

basepath= "/Users/lizbartoshevich/Documents/streamlit_site/"
rawpath= "/files/"
filename= "luttrell_years_metadata.csv"
#READ IN FILE

file = basepath+rawpath+filename
df = pd.read_csv(file)



df_total = pd.read_excel(r'/Users/lizbartoshevich/Downloads/luttrell_by_entry_dates_metadata_sources_coords_ffill-7.xlsx')



#df_total




# OPTIONAL DISPLAY DATA

with tab1:
    display_data = st.checkbox('Display Data')

    if display_data:
        st.dataframe(df)

        st.caption('The above table was created by Dr. Ostwald. Click on the column headers to sort by that column. Highlight cells to copy and paste them. ')

    '*** use iloc and random ***'
    # CHART OF DATA BY YEAR

    ##chose to use a bar chart because of formatting: in a line chart, the years include a comma in them on the axis (1689 = 1,689)

    #st.line_chart(data=df[['n_entries']]) 


    ## reset index to year- otherwise either the years will be graphed OR the axis will be the index instead of the eachs (1678 would be 1) 
    df = df.set_index('year')
    ##st.line_chart(data=df[['n_entries']]) 
    ###df

    st.bar_chart(data=df[['n_entries']])

    # YEAR SUMMARY COMPARE
    ## Allows the user to compare multiple years 

    col1, col2, col3 = st.columns(3)

    '*** adjust above data ***' 

    with col1:
        year_sum1 = st.number_input('Choose a year to compare:', min_value=1678, max_value=1714, step=1, key='year1', value=1678)
        year_sum_df1 = df.loc[year_sum1]
        year_sum_df1

        st.bar_chart(year_sum_df1[['ave_sent_len','ave_entry_len']])

    with col2:
        year_sum2 = st.number_input('Choose a year to compare:', min_value=1678, max_value=1714, step=1, key='year2',value=1692)
        year_sum_df2 = df.loc[year_sum2]
        year_sum_df2

        st.bar_chart(year_sum_df2[['ave_sent_len','ave_entry_len']])

    with col3:
        year_sum3 = st.number_input('Choose a year to compare:', min_value=1678, max_value=1714, step=1,key='year3',value=1710)
        year_sum_df3 = df.loc[year_sum3]
        year_sum_df3

        st.bar_chart(year_sum_df3[['ave_sent_len','ave_entry_len']])

#'idea: allow the user to choose what rows of data to show.... ask dr. o'

#'zoom in on years'

#'maybe I should make a few tabs- luttrell summary + by-the-years, then pronoun usage, then pope, and have maps <coming soon>'



#'personal pronoun explorer: options to select dif pers. pronouns and chart them. maybe build by using complex if loops and inout widgets '

    st.header("Examine the Data Variable by Variable")

    col1, col2 = st.columns([1,3.5])

    with col1:
        data_toexamine = st.selectbox('Pick a variable to examine:',['n_entries','n_sents','n_words','n_words_unique','ave_sent_len','ave_entry_length'])

    with col2:
        st.bar_chart(df[data_toexamine])

with tab2:
    
    year_toexamine= st.slider("Pick a Year to Examine:", min_value=1678, max_value=1714,step=1)
    st.bar_chart(df.loc[year_toexamine])

    display_data2 = st.checkbox('Display Data',key='second')

    if display_data2:
        st.dataframe(df)


### NEWS SOURCE INFO



df_total = df_total.rename(columns = {'sources_lat':'lat',
                                      'sources_lon':'lon'
                                     })



with tab4:
    st.dataframe(df[['I','me','we','us','them']])
    st.bar_chart(df[['I','me','we','us']])
    st.bar_chart(df['them'])
    













with tab3:
    
    '*** uncomment reading in map file ***'
    
    import io

    buffer = io.StringIO()
    df_total.info(buf=buffer)
    s = buffer.getvalue()

    st.text(s)



    df_total[['lat','lon']]

    type(df_total['lat'])
    st.write(df_total.info())


    df_loc = df_total.loc[~df_total['lat'].isnull()]

    df_loc


    #st.map(df_loc)
    import folium as folium 
    from streamlit_folium import st_folium
    from streamlit_folium import folium_static

    m = folium.Map(location=[34.8998, 11.6698],zoom_start=2,tiles='Stamen Terrain')

    for (index,row) in df_loc.iterrows():
        #folium.Marker(location=[row.loc['lat'],row.loc['lon']],
    #                   popup=row.loc['text'],
    #                   icon=
    #                   tooltip=row.loc['gpe_sources_str']).add_to(m)
        folium.CircleMarker([row.loc['lat'],row.loc['lon']],
                            radius=8,
                            popup=row.loc['text'],
                            fill_opacity= 0.1,
                            fill_color='#800080',
                            fill=True,
                            color='#000000',
                            weight=0
                           ).add_to(m)

    folium_static(m, width=1050, height=800)



    
    
    
    
    
    
    st.dataframe(df['year','I',"me",'we','us','them'])
 



