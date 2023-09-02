from src import *
import plotly.express as px
import statistics as stat

st.title('Charts')

fish_df = get_data("SELECT * FROM fish;")
insects_df = get_data("SELECT * FROM insects;")
villagers_df = get_data("SELECT * FROM villagers;")

animal_tab, villagers_tab = st.tabs(["Fish and insects", "Villagers"])

with animal_tab:
    sr_fish_col, sh_fish_col = st.columns([1,1])

    with sr_fish_col:
        st.subheader('Fish spawn rate and selling price')
        fish_df['SpawnRates'] = fish_df['SpawnRates'].str.split('–').str[1].fillna(fish_df['SpawnRates']).astype(int)
        fig = px.scatter(fish_df,x="SpawnRates",y="Sell",color='CatchDifficulty')
        st.plotly_chart(fig, use_container_width=True)

    with sh_fish_col:
        st.subheader('Fish shadow and location')
        fig = px.scatter(fish_df,x="WhereOrHow",y="Shadow",color='Name')
        st.plotly_chart(fig, use_container_width=True)

    sr_insects_col,wh_insects_col = st.columns([1,1])

    with sr_insects_col:
        st.subheader('Insects spawn rate and selling price')
        insects_df['SpawnRates'] = insects_df['SpawnRates'].str.split('–').str[1].fillna(insects_df['SpawnRates']).astype(int)
        fig = px.bar(insects_df,x="SpawnRates",y="Sell",color='Weather')
        st.plotly_chart(fig, use_container_width=True)

    with wh_insects_col:
        st.subheader('Insects weather and location')
        fig = px.bar(insects_df,x="WhereOrHow",y="Weather",color='Name')
        st.plotly_chart(fig, use_container_width=True)

with villagers_tab:
    st.subheader('Villagers personality')
    fig = px.scatter(villagers_df,x="Species",y="Personality",color='Name')
    st.plotly_chart(fig, use_container_width=True)
    


