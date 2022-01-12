
import speech_recognition
from speech_recognition import UnknownValueError
from spotipy import  Spotify
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth


laptop = '9b4a3abeee0b6b5e35ed744bbc6e7dccb4a71fa8'
desktop =  'e0fc382060bf171fb7b7326e458601861cf7b778'
selfphone = 'ac7d723f2c932725fcfb9e766f5c296d89d3037f'

class InvalidSearchError(Exception):
    pass


def get_album_uri(spotify: Spotify, name: str) -> str:


    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='album')
    if not results['albums']['items']:
        raise InvalidSearchError(f'No album named "{original}"')
    album_uri = results['albums']['items'][0]['uri']
    return album_uri


def get_artist_uri(spotify: Spotify, name: str) -> str:

    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='artist')
    if not results['artists']['items']:
        raise InvalidSearchError(f'No artist named "{original}"')
    artist_uri = results['artists']['items'][0]['uri']
    print(results['artists']['items'][0]['name'])
    return artist_uri


def get_track_uri(spotify: Spotify, name: str) -> str:


    # Replace all spaces in name with '+'
    original = name
    name = name.replace(' ', '+')

    results = spotify.search(q=name, limit=1, type='track')
    if not results['tracks']['items']:
        raise InvalidSearchError(f'No track named "{original}"')
    track_uri = results['tracks']['items'][0]['uri']
    return track_uri


def play_album(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_artist(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, context_uri=uri)


def play_track(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, uris=[uri])
def pause_music(spotify = None,device_id = None):
    spotify.pause_playback(device_id=device_id)
def device_select():
    r = speech_recognition.Recognizer()
    print('where do you want to play')
    while True:
        with speech_recognition.Microphone() as mic:
            r.adjust_for_ambient_noise(mic)
            audio = r.record(mic, duration=3)
            try:
                command = r.recognize_google(audio)
            except UnknownValueError:
                continue
        print('user: ' + command)
        try:
            if command == 'cell phone':
                deviceID = selfphone
                break
            elif command == 'laptop':
                break
                deviceID = laptop
            elif command == 'desktop':
                deviceID = desktop
                break
        except Exception as e:
            print('wrong device')
            continue
    return deviceID
deviceID = device_select()


# Connecting to the Spotify account
auth_manager = SpotifyOAuth(
    client_id='55d9d6208ee448f386daf66891f00837',
    client_secret='c015cebd6f704b918b0c236028c252cb',
    redirect_uri='http://localhost:8888/callback/',
    scope='user-read-private user-read-playback-state user-modify-playback-state',
    username='31kcfzjbjfcnfz6oekqo745gintm')
spotify = sp.Spotify(auth_manager=auth_manager)

# Selecting device to play from





# Voice command
r = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
        try:
            command = r.recognize_google(audio)
        except UnknownValueError:
            continue
    print('user: '+command)

    words = command.split()
    if len(words) <= 1:
        print('Could not understand. Try again')


    name = ' '.join(words[1:])
    try:

        if words[0] == 'album':
            uri = get_album_uri(spotify=spotify, name=name)
            play_album(spotify=spotify, device_id=deviceID, uri=uri)
            print('playing: ' + name)
        elif words[0] == 'artist':
            uri = get_artist_uri(spotify=spotify, name=name)
            play_artist(spotify=spotify, device_id=deviceID, uri=uri)
            print('playing: ' + name)
        elif words[0] == 'play':
            uri = get_track_uri(spotify=spotify, name=name)
            play_track(spotify=spotify, device_id=deviceID, uri=uri)
            print('playing: ' + name)
        elif words[0] == 'pause':
            pause_music(spotify=spotify, device_id=deviceID)
        else:
            print('Specify either "album", "artist" or "play". Try Again')
    except InvalidSearchError:
        print(InvalidSearchError)

