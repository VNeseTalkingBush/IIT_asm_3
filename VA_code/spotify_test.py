# import pandas as pd
import speech_recognition
# from speech_recognition import Microphone, Recognizer, UnknownValueError
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

from spotify_sort import *
from client_cridentials import *




# Connecting to the Spotify account
auth_manager = SpotifyOAuth(
    client_id='55d9d6208ee448f386daf66891f00837',
    client_secret='c015cebd6f704b918b0c236028c252cb',
    redirect_uri='http://localhost:8888/callback/',
    scope='user-read-private user-read-playback-state user-modify-playback-state',
    username='31kcfzjbjfcnfz6oekqo745gintm')
spotify = sp.Spotify(auth_manager=auth_manager)

# Selecting device to play from

deviceID = 'e0fc382060bf171fb7b7326e458601861cf7b778'

# Voice command
r = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
        try:
            command = r.recognize_google(audio)
        except:
            command = ""
    print(command)

    words = command.split()
    if len(words) <= 1:
        print('Could not understand. Try again')


    name = ' '.join(words[1:])
    try:
        if words[0] == 'album':
            uri = get_album_uri(spotify=spotify, name=name)
            play_album(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'artist':
            uri = get_artist_uri(spotify=spotify, name=name)
            play_artist(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'play':
            uri = get_track_uri(spotify=spotify, name=name)
            play_track(spotify=spotify, device_id=deviceID, uri=uri)
        else:
            print('Specify either "album", "artist" or "play". Try Again')
    except InvalidSearchError:
        print('InvalidSearchError. Try Again')

