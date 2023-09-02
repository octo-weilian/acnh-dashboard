from src import *

st.title('Catalog')

fish_tab, insects_tab, villagers_tab = st.tabs(["Fish", "Insects", "Villagers"])

critter_column_config = { "IconImage": st.column_config.ImageColumn("IconImage"),
                            "CritterpediaImage": st.column_config.ImageColumn("CritterpediaImage"),
                            "FurnitureImage": st.column_config.ImageColumn("FurnitureImage")}

villagers_column_config = { "IconImage": st.column_config.ImageColumn("IconImage"),
                            "PhotoImage": st.column_config.ImageColumn("PhotoImage"),
                            "HouseImage": st.column_config.ImageColumn("HouseImage")}

with fish_tab:
    fish_df = st.dataframe(get_data("SELECT * FROM fish;"),column_config=critter_column_config,hide_index=True,height=500)
with insects_tab:
    insects_df = st.dataframe(get_data("SELECT * FROM insects;"),column_config=critter_column_config,hide_index=True,height=500)
with villagers_tab:
    villagers_df = st.dataframe(get_data("SELECT * FROM villagers;"),column_config=villagers_column_config,hide_index=True,height=500)

source_url = "[acnh-sheet](https://tinyurl.com/acnh-sheet)"
st.markdown(f'Data from {source_url}',unsafe_allow_html=True)
