import pandas as pd
import numpy as np

def main():
    # Load in data
    df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')

    # Drop duplicates and nan values
    df1 = df.drop_duplicates(subset=['track_id'], keep='first')
    df1 = df1.dropna()


    # Select genres only
    genres = df1.groupby('track_id')['playlist_genre'].apply(list)

    # Remove duplicate genre in a track
    genre_dict = {x:y for x, y in zip(genres.index, genres.values)}
    genre_dict1 = {key: list(dict.fromkeys(values)) for key, values in genre_dict.items()}

    # Join genres into a string, separated by a comma
    genre_dict2 = {key: ','.join(value) for key, value in genre_dict1.items()}


    # Create a new variable track_genre and assign genres
    # to respective track
    df1['track_genre'] = None
    for track, genre in genre_dict2.items():
        df1.at[df1['track_id'] == track, 'track_genre'] = genre


    df1.to_csv('spotify_cleaned1.csv', header=True, index=False)

if __name__ == "__main__":
    main()


# voila --template=gridstack Spotify/Spotify_Songs.ipynb --VoilaConfiguration.resources='{"gridstack": {"show_handles": True}}'