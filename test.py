import pandas as pd
import numpy as np
import json
import glob
import os
import sys

def readFiles(folderPath):
    try:
        files = glob.glob(os.path.join(folderPath, "*.json"))
        if not files:
            raise FileNotFoundError("No JSON files found in the directory.")
        data = pd.concat((
            pd.DataFrame(json.load(open(file, 'r', encoding="utf-8")))
            for file in files
        ),ignore_index=True)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None

def unique(songs):
    seen = set()
    uniqueSongs = [song[0] for song in songs if song[0] not in seen and not song[2] and not seen.add(song[0])]
    return uniqueSongs


def sort(songDict):
    # Implement merge sort on a dictionary later
    return songDict

def getNumListensPerSong(folderPath):

    df = readFiles(folderPath)
    if df is None:
        return None
    songs = df[['master_metadata_track_name','skipped']]
    songNames = df['master_metadata_track_name']
    songs = songs.to_numpy()
    songNames = songNames.to_numpy()

    uniqueSongs = unique(songs)

    # Making a dictionary to record how many times each song was played
    songDict = {s:0 for s in uniqueSongs}

    for s in songNames:
        if tuple(s) in songDict:
            songDict[s]+=1
    return songDict

folderPath = '/Users/ian/Desktop/CompSciContent/SpotifyHistory'

df = readFiles(folderPath)
if df is None:
    sys.exit()
songs = df[['master_metadata_track_name','master_metadata_album_artist_name','skipped']]
songNamesAndArtists = df[['master_metadata_track_name','master_metadata_album_artist_name']]
songs = songs.to_numpy()
songNamesAndArtists = songNamesAndArtists.to_numpy()

uniqueSongs = unique(songs)

# Making a dictionary to record how many times each song was played
songDict = {tuple(s):0 for s in uniqueSongs}

for s in songNamesAndArtists:
    if songDict.__contains__(tuple(s)):
        songDict[tuple(s)]+=1