import pandas as pd
import numpy as np
import json
import os
import sys
import glob

class DataReader:
    def __init__(self):
        self.data = None
        self.songs = None
        self.uniqueSongs = None
        self.songDictionary = None
    """
    Accepts a parameter folderPath that is a path to the folder containing the json files,
    reads the files and stores the data in the classes data instance variable
    """
    def readFiles(self,folderPath):
        try:
            files = glob.glob(os.path.join(folderPath, "*.json"))
            if not files:
                raise FileNotFoundError("No JSON files found in the directory.")
            self.data = pd.concat((
                pd.DataFrame(json.load(open(file, 'r', encoding="utf-8"))) for file in files),ignore_index=True)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")

    """
    Sets the list of unique songs stored as an instance vaiable
    """
    def unique(self):
        seen = set()
        # self.uniqueSongs = [tuple(song) for song in ]
    
    def getNumListensPerSong(self):
        df = self.data
        if df is None:
            return
        songs = df[['master_metadata_track_name','master_metadata_album_artist_name','skipped']]
        songNames = df[['master_metadata_track_name','master_metadata_album_artist_name']]
        songs = songs.to_numpy()
        songNames = songNames.to_numpy()

        uniqueSongs = self.unique(songs)

        # Making a dictionary to record how many times each song was played
        songDict = {s:0 for s in uniqueSongs}

        for s in songNames:
            if tuple(s) in songDict:
                songDict[s]+=1
        self.songDictionary = songDict
