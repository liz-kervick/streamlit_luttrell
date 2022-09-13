import streamlit as st
import pandas as pd
import numpy as np 
import io 
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import folium as folium 

# READ IN FILES USING FUNCTIONS - this was just. not working. 

# st.cache(suppress_st_warning=True)
# def df_sum_f():
#     df_sum=pd.read_csv(basepath+rawpath+filename_df_sum)
#     #return st.dataframe(df_sum)
#     return df_sum
    
    
basepath= "/streamlit_luttrell"
rawpath= "/files/"
filename_df_sum= "luttrell_years_metadata.csv"
filename_df_all='luttrell_by_entry_dates_metadata_sources_coords_ffill-7.csv'

df_sum=pd.read_csv(basepath+rawpath+filename_df_sum)


df_all=pd.read_csv(basepath+rawpath+filename_df_all)


# PAGE HEADING  

st.title('Narcissus Luttrell: *A Brief Historical Relation of State Affairs* 1678-1714')
st.write('Welcome to the Luttrell Dataset!')
st.write('This dataset is the basis for my Honors Thesis at Eastern Connecticut State University. Use the below tabs to explore aspects of the text via data analysis.')

# FORMAT TABS

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Introduction','Summary','Year-By-Year','Mapping','Personal Pronouns','Catholicism'])

# INTRODUCTION TAB

with tab1:
    
    st.subheader('**What is the Brief Relation of Historical Affairs?**')
    st.write('This manuscript, written in England from 1678 to 1714 was a personal chronical of news. Like a dedicated journal-keeper, Luttrell recorded each piece of news he encountered multiple times a week, resulting in a 4,000 page work (over 3x the length of the bible and Lord of the Rings!). In order to analyze such a large piece, breaking the text up into data is necessary.')
    
    st.write('This is an example of one entry, dated 11/17/1679:')
    st.subheader('*The conspiracy against Dr. Oates by Knox and Lane appears on their trial to be a most villainous design; and had it succeeded, it had rendered Dr. Oates his testimony invalid for the future.*')
    
    # display_data1= st.checkbox('Display Data',key='dd1')
    # if display_data1:
    #     st.dataframe(df_all.iloc[246:251])
    
    
    st.write('Now multiply this entry by almost 40,000...')
    
    with st.container():
        col1, col2, col3 = st.columns([1,2,4.5]) 

        with col1:
            st.button('Click for a random entry')

        with col2:
            st.write('ENTRY DATE:')

            x= np.random.randint(1,39470)
            year= df_all.iat[x,3]
            month= df_all.iat[x,4]
            day= df_all.iat[x,5]

            st.write(month,'/',day,'/',year)

        with col3:
            st.write(df_all.iat[x,2])

    st.write('As you can see by clicking the button a few times, Luttrell talks about many different figures, events, and places. By scrolling through entries in order, you will see that the information in the manuscript were often not related to the ones surrounding it.')
    
    x2 = st.slider('Select an entry number:',0,39472,value=12693,help='Use the arrow keys to change entry number by 1')

    col1, col2 = st.columns([1,4])

    with col1:
        st.write('ENTRY DATE:')

        year= df_all.iat[x2,3]
        month= df_all.iat[x2,4]
        day= df_all.iat[x2,5]

        st.write(month,'/',day,'/',year)

    with col2:
        st.write(df_all.iat[x2,2])
    
    
#display_data = st.checkbox('Display Data',key='dd2')
#if display_data:
    #st.dataframe(df_sum)

    
#st.caption('The above table was created by Dr. Ostwald from the Google Books version of a Brief Relation of Historical Affairs. Click on the column headers to sort by column. Highlight cells to copy and paste them.')

    #st.write(df.i
    
    
    
# SUMMARY TAB

with tab2:
    st.write('In order to efficiently analyze this document, my thesis mentor converted the text into a spreadsheet with each row representing one entry and containing data such as the entry date and the source of the news.')
    display_data = st.checkbox('Display Data')
    if display_data:
        st.dataframe(df_all)
    st.write('Alone, this spreadsheet is difficult to read. However, when summarized by year and visualized...')
    
    df_sum = df_sum.set_index('year')
    
    
    df_sum = df_sum.rename(columns=
                           {'n_entries':'# entries',
                            'n_sents':'# sentences',
                            'n_words':'# words',
                            'n_words_unique':'# unique words',
                            'n_nnp':'# proper nouns',
                            'n_nnp_unique':'# unique proper nouns',
                            'ave_sent_len':'average sent length',
                            'ave_entry_len':'average entry length'
                           }
                          )
    df_sum2 = df_sum[['# entries',
                     '# sentences',
                     '# words',
                     '# unique words',
                     '# proper nouns',
                     '# unique proper nouns',
                     'average sent length',
                     'average entry length'
                    ]]
    #df_sum
    
    st.bar_chart(data=df_sum2[['# entries']])
    
    st.write('... you can see that Luttrell writes different numbers of entries. Most notably, there is a major peak in 1692 with 3,491 entries.')
    
    st.header("Examine the Data Variable by Variable")
    
    st.write('Use the box below to chart other variables and look for trends, or chose the personal pronouns or Catholic tab to examine related variables.')

    col1, col2 = st.columns([1,3.5])

    with col1:
        data_toexamine = st.selectbox('Pick a variable to examine:',
                                      ['# entries',
                                       '# sentences',
                                       '# words',
                                       '# unique words',
                                       '# proper nouns',
                                       '# unique proper nouns',
                                       'average sent length',
                                       'average entry length'
                                      ]
                                     )
    with col2:
        st.bar_chart(df_sum2[data_toexamine])

    col1, col2 = st.columns([1,3.5])

    with col1:
        data_toexamine = st.selectbox('Pick a variable to examine:',
                                      ['# entries',
                                       '# sentences',
                                       '# words',
                                       '# unique words',
                                       '# proper nouns',
                                       '# unique proper nouns',
                                       'average sent length',
                                       'average entry length'
                                      ]
                                     ,key='sb2')
    with col2:
        st.bar_chart(df_sum2[data_toexamine])
    
                            
# YEAR BY YEAR TAB

with tab3: 
    st.write('We can also examine the data year-by-year to look for changes in how Luttrell wrote over time.')

    col1, col2, col3 = st.columns(3)

    with col1:
        year_sum1 = st.number_input('Choose a year to compare:', min_value=1678, max_value=1714, step=1, key='year1', value=1678)
        
    with col2:
        year_sum2 = st.number_input('Choose a year to compare:', min_value=1678, max_value=1714, step=1, key='year2',value=1692)
       
    with col3:
        year_sum3 = st.number_input('Choose a year to compare:', min_value=1678, max_value=1714, step=1,key='year3',value=1710)
       
        
    var= st.multiselect('Choose variables to display:',
                                      ['# entries',
                                       '# sentences',
                                       '# words',
                                       '# unique words',
                                       '# proper nouns',
                                       '# unique proper nouns',
                                       'average sent length',
                                       'average entry length'
                                      ],
                                     help='Notice: the scales are not consistent between charts')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        year_sum_df1 = df_sum2.loc[year_sum1]
        st.bar_chart(year_sum_df1[var])
        year_sum_df1
        
    with col2:
        year_sum_df2 = df_sum2.loc[year_sum2]
        st.bar_chart(year_sum_df1[var])
        year_sum_df2
    with col3:
        year_sum_df3 = df_sum2.loc[year_sum3]
        st.bar_chart(year_sum_df3[var])
        year_sum_df3
       
# MAPPING TAB

with tab4:
    
    
    st.subheader('**Where did all this news come from?**')
    
    st.write('Narcissus Luttrell lived during the early stages of globalization and news networks. During his life, people and the news they carried travelled around the world. As they travelled, they exchanged news through word of mouth, letters, newspapers, manuscripts, and pamphlets. Located in England, Luttrell received news from every continent except Australia and Antartica.')
    
    st.write('Luttrell often recorded the source of his news entry- using georeferencing, we are able to plot that data onto the map below. Use the buttons to center the map, or use the mouse and zoom buttons to pan around. Select points to view the associated entry.')
    
    buffer = io.StringIO()
    df_all.info(buf=buffer)
    s = buffer.getvalue()
    #st.text(s)

    df_all_ll = df_all.rename(columns = {'sources_lat':'lat',
                                      'sources_lon':'lon'
                                     })
 
    df_loc = df_all_ll.loc[~df_all_ll['lat'].isnull()]

    col1, col2, col3 = st.columns(3)
    coords = [53.4776,-2.4911]
    zoom = 6
    
    with col3:
        world = st.button('Center on: World')
        if world:
            coords= [38.5521, -2.6090]
            zoom=2.43
        
    with col2:
        europe= st.button('Center on: Europe')
        if europe:
            coords=[44.3906, 20.08370]
            zoom=3.5
    with col1:
        england= st.button('Center on: England')
        if england:
            coords=[53.477, -2.491]
            zoom=6
        
    
    m = folium.Map(location=(coords),zoom_start=zoom)

    for (index,row) in df_loc.iterrows():
        #folium.Marker(location=[row.loc['lat'],row.loc['lon']],
    #                   popup=row.loc['text'],
    #                   icon=
    #                   tooltip=row.loc['gpe_sources_str']).add_to(m)
        folium.CircleMarker([row.loc['lat'],row.loc['lon']],
                            radius=8,
                            popup=row.loc['text'],
                            fill_opacity= 0.05,
                            fill_color='#800080',
                            fill=True,
                            color='#000000',
                            weight=0
                           ).add_to(m)

    folium_static(m, width=1050, height=800)
    
    st.subheader('Explore the Map: Year by Year')
    st.write('Over the years, Luttrell may have gotten his news from different places. We can test this by examining map by year. Use the slider below to select a year to display.')
                 

    year = st.slider('Select a year:',1678,1714,1700)
    df_loc_year = df_loc.loc[df_loc['year_entry_os'] == year]
    
    m2 = 0
    m2 = folium.Map(location=(38.5521, -2.6090),zoom_start=2.43)

    for (index,row) in df_loc_year.iterrows():
        #folium.Marker(location=[row.loc['lat'],row.loc['lon']],
    #                   popup=row.loc['text'],
    #                   icon=
    #                   tooltip=row.loc['gpe_sources_str']).add_to(m)
        folium.CircleMarker([row.loc['lat'],row.loc['lon']],
                            radius=10,
                            popup=row.loc['text'],
                            fill_opacity= 0.8,
                            fill_color='#800080',
                            fill=True,
                            color='#000000',
                            weight=0
                           ).add_to(m2)

    folium_static(m2, width=1050, height=800)
    
    df_loc_year =df_loc_year.rename(columns =
                       {'year_entry_os':'year',
                        'mo_all_os_num':'month',
                        'day_all_os_num':'day',
                        'sources_country':'country',
                        
                       }
                      )
 
    
    
    display_loc_year = st.checkbox('Display Data', key='dd3')
    if display_loc_year:
        df_loc_year[['country','year','month','day','news_source','text']]

# PERSONAL PRONOUNS TAB

with tab5:
    st.header('How Did Luttrell Use Personal Pronouns?')

    st.warning('This page will be expanded in future') 

    st.write('Throughout his manuscript, Luttrell uses personal pronouns.') 


    st.bar_chart(df_sum[['I','me','we','us']])

    st.bar_chart(df_sum['them']) 

    st.write('Choose personal pronouns below to compare frequences throughout the years. Note: This data *currently* does not factor in the varience in total number of words of each year- meaning that the reason the 1692 column is so tall is partially due to the general higher word count.')

    select_pp = st.multiselect('Select Personal Pronouns to Examine:',['I','me','we','us','them'],default=['I','we'])

    st.bar_chart(df_sum[select_pp])

    

# CATHOLICISM TAB

with tab6:
    
    st.header('Luttrell and Catholicism')

    st.warning('This page will be expanded in future') 

    st.write('Throughout his manuscript, Luttrell writes about Catholicism. He started his manuscript during the Popish plot, recording the relationship between Britain and Catholicism. You can see that during the first four years of writing, he discusses Catholicism frequently') 


    st.bar_chart(df_sum['catholic_words'])
    
    st.write('This data was derived by counting each word within the entries that is also found on a list of words relating to catholicism, such as Papist or Pope.')
    
   
    
    st.bar_chart(df_sum[['# unique words','catholic_words']])
    st.caption('Eventually this will be a chart of the % of catholic words')









# 'optional show data box'

# 'map!!!'

# 'bar chart of the entries/year'

# 'bar chart of subjects over time'

# 'can you find 17thC named entities better than a computer? (using text analyzer)'
