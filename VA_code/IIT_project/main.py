
import requests
import speech_recognition
import pyttsx3
import wikipedia
import datetime as Dt
from datetime import date, datetime
import webbrowser
from youtube_search import YoutubeSearch
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
from speech_recognition import UnknownValueError

# Connecting to the Spotify account
auth_manager = SpotifyOAuth(
    client_id='55d9d6208ee448f386daf66891f00837',
    client_secret='c015cebd6f704b918b0c236028c252cb',
    redirect_uri='http://localhost:8888/callback/',
    scope='user-read-private user-read-playback-state user-modify-playback-state',
    username='31kcfzjbjfcnfz6oekqo745gintm')
spotify = sp.Spotify(auth_manager=auth_manager)

# Selecting device to play music

deviceID = 'e0fc382060bf171fb7b7326e458601861cf7b778'

wikipedia.set_lang('en')
language = 'en'

today = date.today()
d2 = today.strftime("%B %d, %Y")
now = datetime.now()

engine = pyttsx3.init()
search = ''


def spotify_music():
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


    def pause_music(spotify=None, device_id=None):
        spotify.pause_playback(device_id=device_id)


    Jeff_microphone = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        Jeff_microphone.adjust_for_ambient_noise(mic)
        audio = Jeff_microphone.listen(mic)
        try:
            command = Jeff_microphone.recognize_google(audio)
        except UnknownValueError:
            print(UnknownValueError)
    print(command)

    words = command.split()

    name = ' '.join(words[1:])
    try:

        if words[0] == 'album':
            uri = get_album_uri(spotify=spotify, name=name)
            play_album(spotify=spotify, device_id=deviceID, uri=uri)
            engine.say('playing: ' + command)
        elif words[0] == 'artist':
            uri = get_artist_uri(spotify=spotify, name=name)
            play_artist(spotify=spotify, device_id=deviceID, uri=uri)
            engine.say('playing: ' + command)
        elif words[0] == 'play':
            uri = get_track_uri(spotify=spotify, name=name)
            play_track(spotify=spotify, device_id=deviceID, uri=uri)
            engine.say('playing: ' + command)
        elif words[0] == 'pause':
            pause_music(spotify=spotify, device_id=deviceID)
            engine.say('playing: ' + command)

    except InvalidSearchError as e:
        print(e)

while True:

    engine.runAndWait()
    Jeff_microphone = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            audio = Jeff_microphone.record(mic, duration=3)
            text = Jeff_microphone.recognize_google(audio)

            if 'today' in text:  # DATE
                Jeff = today.strftime("%B %d, %Y")

                engine.say(Jeff)
            elif 'music' in text:
                Jeff = 'What woud you like to hear'
                engine.say(Jeff)
                spotify_music()


            elif 'time' in text:  # TIME

                Jeff = now.strftime("%H : %M minutes")

                engine.say(Jeff)

            elif 'search for' in text:  # WIKIPEDIA
                searching = text.replace('search for', '')
                contents = wikipedia.summary(searching, sentences=3).split('\n')

                engine.say(contents)

            elif 'video' in text:
                Jeff = 'Do you want to search or play video?'

                engine.say(Jeff)

                engine.runAndWait()
                Jeff_microphone = speech_recognition.Recognizer()
                try:
                    with speech_recognition.Microphone() as mic:
                        audio = Jeff_microphone.record(mic, duration=3)
                        choice = Jeff_microphone.recognize_google(audio)

                    if 'search' in choice:

                        searching_youtube()
                    elif 'play' in choice:

                        playing_youtube()
                except Exception as e:
                    print(e)


            elif 'weather' in text:
                ow_url = "http://api.openweathermap.org/data/2.5/weather?"
                city = text.replace('weather in ', '')
                print(city)
                if not city:
                    pass
                api_key = "48c83d5a3e5349f9fb561e779315a8b4"
                call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
                print(call_url)
                response = requests.get(call_url)
                data = response.json()
                if data["cod"] != "404":
                    city_res = data["main"]
                    current_temperature = city_res["temp"]
                    current_pressure = city_res["pressure"]
                    current_humidity = city_res["humidity"]
                    suntime = data["sys"]
                    sunrise = Dt.datetime.fromtimestamp(suntime["sunrise"])
                    sunset = Dt.datetime.fromtimestamp(suntime["sunset"])
                    now = Dt.datetime.now()
                    content = f"""Today is {today.strftime("%B %d, %Y")} \n 
                        Sunrise at {sunrise.hour} : {sunrise.minute} minutes \n
                        Sunset at {sunset.hour} : {sunset.minute} minutes \n
                        Temperature is {current_temperature} degree \n
                        Pressure is {current_pressure} hector Pascal \n
                        Humidity is {current_humidity}%
                        """
                    Jeff = content

                    engine.say(Jeff)
                else:
                    Jeff = "Cannot find your area"

                    engine.say(Jeff)






            elif 'bye' in text:  # TURN OFF
                Jeff = 'Goodbye master\n'
                engine.say(Jeff)

                engine.runAndWait()
                break


    except Exception as e:
        print(e)


    def searching_youtube():
        Jeff = 'What do you looking for?'

        engine.say(Jeff)

        engine.runAndWait()
        Jeff_microphone = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as mic:
                audio = Jeff_microphone.record(mic, duration=3)
                text = Jeff_microphone.recognize_google(audio)

            Jeff = 'Okay master, searching for' + text.replace('searching for', '') + '\n'

            engine.say(Jeff)
            search = text.replace('searching for', '')
            url = f"https://www.youtube.com/search?q={search}"
            webbrowser.get().open(url)
        except Exception as e:
            print(e)



    def playing_youtube():
        Jeff = 'What do you want to play?'

        engine.say(Jeff)

        engine.runAndWait()
        Jeff_microphone = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as mic:
                audio = Jeff_microphone.record(mic, duration=3)
                text = Jeff_microphone.recognize_google(audio)

            Jeff = 'Okay master, playing for' + text.replace('playing for', '') + '\n'

            engine.say(Jeff)
            play = text.replace('playing for', '')
            while True:
                result = YoutubeSearch(play, max_results=10).to_dict()
                if result:
                    break
            url = f"https://www.youtube.com" + result[0]['url_suffix']
            webbrowser.get().open(url)
            print(result)

        except Exception as e:
            print(e)
