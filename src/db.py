from src import *

def load_tables(path,engine):
    for f in Path(path) .glob('*.csv'):
        df = pd.read_csv(f)
        df.columns = [col.replace('#','Number').replace('/','Or').replace(' ','') for col in df.columns]
        
        if 'fish' in f.stem:
            icon_image = "https://acnhcdn.com/latest/MenuIcon/{IconFilename}.png"
            critterpedia_image = "https://acnhcdn.com/latest/BookFishIcon/{CritterpediaFilename}.png"
            furniture_image = "https://acnhcdn.com/latest/FtrIcon/{FurnitureFilename}.png"
            df['IconImage']=df['IconFilename'].apply(lambda x:icon_image.replace('{IconFilename}',x))
            df['CritterpediaImage']=df['CritterpediaFilename'].apply(lambda x:critterpedia_image.replace('{CritterpediaFilename}',x))
            df['FurnitureImage']=df['FurnitureFilename'].apply(lambda x:furniture_image.replace('{FurnitureFilename}',x))

        elif 'insects' in f.stem:
            icon_image = "https://acnhcdn.com/latest/MenuIcon/{IconFilename}.png"
            critterpedia_image = "https://acnhcdn.com/latest/BookInsectIcon/{CritterpediaImage}.png"
            furniture_image = "https://acnhcdn.com/latest/FtrIcon/{FurnitureFilename}.png"
            df['IconImage']=df['IconFilename'].apply(lambda x:icon_image.replace('{IconFilename}',x))
            df['CritterpediaImage']=df['CritterpediaFilename'].apply(lambda x:critterpedia_image.replace('{CritterpediaImage}',x))
            df['FurnitureImage']=df['FurnitureFilename'].apply(lambda x:furniture_image.replace('{FurnitureFilename}',x))
        
        if 'villagers' in f.stem:
            icon_image = "https://acnhcdn.com/latest/NpcIcon/{Filename}.png"
            photo_image = "https://acnhcdn.com/latest/NpcBromide/NpcNml{Filename}.png"
            house_image = "https://acnhcdn.com/drivesync/render/houses/{Filename}.png"
            df['IconImage']=df['Filename'].apply(lambda x:icon_image.replace('{Filename}',x))
            df['PhotoImage']=df['Filename'].apply(lambda x:photo_image.replace('{Filename}',x.capitalize()))
            df['HouseImage']=df['Filename'].apply(lambda x:house_image.replace('{Filename}',x))

        df.to_sql(f.stem, engine, if_exists='replace', index=False)

