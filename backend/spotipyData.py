from concurrent.futures import process
import pandas as pd
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import matplotlib.pyplot as plt
import seaborn as sns
import math

"""## Set up Spotify credentials"""
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def playlistDetails(playlist):
  playlists.get(playlist)
  playlist_tracks = spotify.playlist_tracks(playlist_id=playlist)
  songIDs, artistIDs = [], []

  #Find the name, artist, and ID for each song in the playlist
  for i in range(len(playlist_tracks['items'])):
    artistIDs.append(playlist_tracks['items'][i]['track']['artists'][0]['id']) #Append artist IDs to a list
    songIDs.append(playlist_tracks['items'][i]['track']['id']) #Append song IDs to a list

  # print(songIDs)
  # print(artistIDs)
  
  return artistIDs, songIDs

def songViewer(songs):
  for i in range(6):
    Mix1 = playlistDF[playlistDF['mix'] == 1].sample(songs)
    Mix2 = playlistDF[playlistDF['mix'] == 2].sample(songs)
    Mix3 = playlistDF[playlistDF['mix'] == 3].sample(songs)
    Mix4 = playlistDF[playlistDF['mix'] == 4].sample(songs)
    Mix5 = playlistDF[playlistDF['mix'] == 5].sample(songs)
    Mix6 = playlistDF[playlistDF['mix'] == 6].sample(songs)
    Sampler = pd.concat([Mix1, Mix2, Mix3, Mix4, Mix5, Mix6])
  return Sampler

def normFeatures(MixNum):
  features = values[values.groupby(values.danceability, group_keys=False).apply(lambda x: x.mix == MixNum)]
  mean_features = features.describe().loc['mean']
  mean_features['duration_ms'] = mean_features['duration_ms']/60000/3.28 # ms in min / average song length in 2020
  mean_features['loudness'] = mean_features['loudness']/-160 # min decibal val
  mean_features['tempo'] = mean_features['tempo']/120 # standard walking tempo
  mean_features['key'] = (mean_features['key']+1)/12 #shift from [-1,11] to [0,12] then normalize
  mean_features['time_signature'] = (mean_features['time_signature']-3)/4 #shift from [3,7] to [0,4] then normalize
  return mean_features

def trueFeatures(MixNum):
  features = values[values.groupby(values.danceability, group_keys=False).apply(lambda x: x.mix == MixNum)]
  mean_features = features.describe().loc['mean']
  return mean_features

def recommend(recommendations):

  for i in range(len(recommendations['tracks'])): #returns 20 recommendations
    rec_song_names.append(recommendations['tracks'][i]['name'])
    rec_song_IDs.append(recommendations['tracks'][i]['id'])
    rec_previews.append(recommendations['tracks'][i]['preview_url'])
    
  return(rec_song_names, rec_song_IDs, rec_previews)


#Enter your own playlist for custom results
PLAYLIST_ID = 'spotify:playlist:37i9dQZF1E3ak8b8mVNAGr'
playlist_tracks = spotify.playlist_tracks(playlist_id=PLAYLIST_ID)

"""## Save Playlist Information"""

playlists =  {'daily_mix_1': 'spotify:playlist:37i9dQZF1E38Nwtqw1UQOl',
              'daily_mix_2': 'spotify:playlist:37i9dQZF1E3524Ob8eyv9s',
              'daily_mix_3': 'spotify:playlist:37i9dQZF1E36nHwFi7oNca',
              'daily_mix_4': 'spotify:playlist:37i9dQZF1E3ak8b8mVNAGr',
              'daily_mix_5': 'spotify:playlist:37i9dQZF1E39aNp3OqG1mF',
              'daily_mix_6': 'spotify:playlist:37i9dQZF1E37NF4nKqilXC'}

# playlists.get('daily_mix_1')

artistIDs = playlistDetails(playlists.get('daily_mix_3'))[0]
songIDs = playlistDetails(playlists.get('daily_mix_3'))[1]

"""##Retrieve & Analyze Song Features
##### More information at https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
"""

features_list = []

for i in range(len(songIDs)): #for each song in the user's playlist
  thing = spotify.audio_features(songIDs)
  
  for features in thing: #save each feature in the audio features json dict
    features_list.append([features['energy'], features['liveness'], features['tempo'], features['speechiness'], features['acousticness'], features['instrumentalness'],
                          features['time_signature'], features['danceability'], features['key'], features['duration_ms'], features['loudness'], features['valence'], 
                          features['mode']])

#Read features into a df
df = pd.DataFrame(features_list, columns=['energy', 'liveness', 'tempo', 'speechiness', 'acousticness', 'instrumentalness', 'time_signature', 'danceability', 'key', 'duration_ms', 
                                          'loudness', 'valence', 'mode'])

# print(df.head())

# df.describe().loc['mean']

playlistDF = pd.DataFrame()
j = 1
songNames, preview, songID, artistNames, mixNumber = [], [], [], [], []

for key in playlists:
  playlist = playlists[key]
  playlist_tracks = spotify.playlist_tracks(playlist_id=playlist)
  

  #Find the name, artist, and ID for first 16 songs in the playlist
  for i in range(math.floor(len(playlist_tracks['items'])/3)):  
    songNames.append(playlist_tracks['items'][i]['track']['name']) #Append song names to a list
    preview.append(playlist_tracks['items'][i]['track']['preview_url']) #Append snippet url to a list
    songID.append(playlist_tracks['items'][i]['track']['id']) #Append song names to a list
    artistNames.append(playlist_tracks['items'][i]['track']['artists'][0]['name']) #Append artist names to a list
    mixNumber.append(j)
  
  j+= 1

rows = [songNames, preview, songID, artistNames, mixNumber]
playlistDF = pd.DataFrame(rows).T
playlistDF.columns =['song', 'preview', 'ID', 'artist', 'mix']
# print(playlistDF.head(10))

Sampler = songViewer(2)

output = pd.DataFrame()
for i in range(len(songID)): #for each song in the user's playlist
  features = spotify.audio_features(songID[i])
  output = output.append(thing, ignore_index=True)

output = output.drop(['analysis_url', 'track_href', 'type', 'uri'], axis = 1)

together = pd.concat([playlistDF, output], axis = 1, sort=False).drop('id', axis = 1)
values = together.iloc[:, 3:]

# print(together.head(2))

corrHeatMap = values.corr()
plt.figure(figsize=(16, 9))
heatMap = sns.heatmap(corrHeatMap, annot = True, fmt = '.1g', vmin = -1, vmax = 1, center = 0, cmap = 'inferno', linewidths = 1, linecolor = 'Black')
heatMap.set_title('daily mix variable correlations')
heatMap.set_xticklabels(heatMap.get_xticklabels(), rotation = 90)
plt.savefig('dailyMixHeatmap.png', dpi = 100)

mix_1_features = normFeatures(1)
mix_2_features = normFeatures(2)
mix_3_features = normFeatures(3)
mix_4_features = normFeatures(4)
mix_5_features = normFeatures(5)
mix_6_features = normFeatures(6)

allFeatures = pd.concat([mix_1_features, mix_2_features, mix_3_features, mix_4_features, mix_5_features, mix_6_features], axis = 1, sort=False)
allFeatures.columns = ['1', '2', '3', '4', '5', '6']

f = plt.figure(figsize=(32, 24))

with sns.axes_style("darkgrid"):
    sns.set_palette("magma", 6)
    ax = f.add_subplot()
    sns.lineplot(data=allFeatures, dashes=False, markers=True, linewidth= 5)
    ax.set_title('Daily Mix Feature Comparison', fontsize = 30)
    for item in ax.get_xticklabels():
        item.set_rotation(45)
        item.set_fontsize(fontsize = 20)
    for item in ax.get_yticklabels():
        item.set_fontsize(fontsize = 20)
    plt.legend(labels=["Mix1","Mix2","Mix3","Mix4","Mix5","Mix6"], loc = 2, bbox_to_anchor = (1,1), fontsize = 20)
plt.savefig('FeatureComparison.png')

#Recommendation 1
recommendations1 = spotify.recommendations(seed_tracks = songIDs[0:5]) #based on the first 5 songs from user playlist

#Recommendation 2
recommendations2 = spotify.recommendations(seed_artists = artistIDs[0:5]) #based on the first 5 artists from user playlist

rec_song_names, rec_song_IDs, rec_previews = [],[],[]
  
#Find recommended songs based on 'recommendations1'
recommend(recommendations1)

recRows = [rec_song_names, rec_song_IDs, rec_previews]
recPlaylistDF = pd.DataFrame(recRows).T
recPlaylistDF.columns =['song', 'id', 'preview']
print(recPlaylistDF.head(2))