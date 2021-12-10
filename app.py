import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import helper

df = pd.read_csv(r'C:\Users\hp\PycharmProjects\criket_match project\match.csv')
df['start_date']=pd.to_datetime(df['start_date'])
df['year_of_match']=df['start_date'].dt.year
df['month_of_match'] = df['start_date'].dt.month

Monu = st.sidebar.radio(
    'Select Option',
    ('Home','Analysis')
)
if Monu == 'Home':
    st.image('https://th.bing.com/th/id/R.b36b36787758687950420518088dc7cb?rik=lNXuLF5jDkYFyA&riu=http%3a%2f%2fwww.latrobe.edu.au%2fnews%2fimages%2farticles%2fcricket-resized.jpg&ehk=YGGdepDhThbwS6CGkOM%2ffYQlEM3NVclO%2feIvdowqEPY%3d&risl=&pid=ImgRaw&r=0')
    st.title('Cricket Match Analysis 2004 - 2021')
    st.header('All Country Counts Of Match')
    df['name'] = df['name'].astype(str)
    contry_name_list = df['name'].unique().tolist()
    contry_name_list.sort()
    contry_name_list.insert(0, 'Overall')
    country = st.selectbox('Select on Countrys',contry_name_list)

    matchcoounts = helper.countsmatch(df,country)
    st.table(matchcoounts)

if Monu == 'Analysis':

    yealymatch = helper.yearlycountmatch(df)

    color = ['#800000', '#808000', '#008000', '#800080', '#008080', '#000080']
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(x=yealymatch['year'], y=yealymatch['counts of match'], palette=color)
    plt.title('Counts Of Yearly Matchs', weight='bold', fontsize=20)
    sns.despine()
    st.pyplot(plt)

    countrymatchparticipate = helper.participate_all_match_each_country(df)

    color = ['#800000', '#808000', '#008000', '#800080', '#008080', '#000080']
    fig = plt.figure(figsize=(15, 6))
    sns.barplot(x=countrymatchparticipate['countrys'],y=countrymatchparticipate['particepate match'], palette=color)
    plt.title('Counts Of Participate Each Country', weight='bold', fontsize=20)
    plt.tick_params(axis='x', rotation=90)
    sns.despine()
    st.pyplot(plt)

    t20match = helper.t20(df)
    color = ['#800000', '#808000', '#008000', '#800080', '#008080', '#000080']
    fig = plt.figure(figsize=(15, 6))
    sns.barplot(x=t20match['country'], y=t20match['t20match'], palette=color)
    plt.title('Counts Of Participate Each Country of T20 Match', weight='bold', fontsize=20)
    plt.tick_params(axis='x', rotation=90)
    sns.despine()
    st.pyplot(plt)

    odimatch = helper.odi(df)
    color = ['#800000', '#808000', '#008000', '#800080', '#008080', '#000080']
    fig = plt.figure(figsize=(15, 6))
    sns.barplot(x=odimatch['country'], y=odimatch['odimatch'], palette=color)
    plt.title('Counts Of Participate Each Country of ODI Match', weight='bold', fontsize=20)
    plt.tick_params(axis='x', rotation=90)
    sns.despine()
    st.pyplot(plt)

    testmatch = helper.test(df)
    color = ['#800000', '#808000', '#008000', '#800080', '#008080', '#000080']
    fig = plt.figure(figsize=(15, 6))
    sns.barplot(x=testmatch['country'], y=testmatch['testmatch'], palette=color)
    plt.title('Counts Of Participate Each Country of Test Match', weight='bold', fontsize=20)
    plt.tick_params(axis='x', rotation=90)
    sns.despine()
    st.pyplot(plt)





