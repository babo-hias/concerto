import pandas as pd
from .models import Show

def get_table_data():

    db_columns = [field.name for field in Show._meta.get_fields() if field.name != "id"]
    db_columns = [list_item.capitalize() for list_item in db_columns]
    return db_columns

def get_year_chart(df):
    #df = pd.DataFrame(list(db_shows))

    df = df.groupby(['jahr']).count()
    df.reset_index(level=0, inplace=True)
    df.rename(columns={'kategorie': 'anzahl'}, inplace=True)
    df = df[df['jahr'] != '-']
    df = df[['jahr', 'anzahl']]

    labels = list(df['jahr'])
    data = list(df['anzahl'])
    return [labels, data]


def get_artist_chart(df):
    #df = pd.DataFrame(list(db_shows))

    df = df.groupby(['artist']).count()
    df.reset_index(level=0, inplace=True)
    df.rename(columns={'kategorie': 'anzahl'}, inplace=True)
    df = df[['artist', 'anzahl']]
    df.sort_values(by=['anzahl'], ascending=False, inplace=True)

    labels = list(df['artist'])
    data = list(df['anzahl'])
    return [labels, data]


def get_location_chart(df):
    #df = pd.DataFrame(list(db_shows))

    df = df.loc[(df['location'] != 'Festival') & (df['location'] != '-')]
    df = df.groupby(['location']).count()
    df.reset_index(level=0, inplace=True)
    df.rename(columns={'kategorie': 'anzahl'}, inplace=True)
    df = df[['location', 'anzahl']]
    df.sort_values(by=['anzahl'], ascending=False, inplace=True)

    labels = list(df['location'])
    data = list(df['anzahl'])
    return [labels, data]