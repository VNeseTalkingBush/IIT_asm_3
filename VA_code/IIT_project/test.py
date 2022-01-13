from tkinter import *
import requests
import speech_recognition
from speech_recognition import UnknownValueError
import pyttsx3
import wikipedia
import datetime as Dt
from datetime import date, datetime
import webbrowser
import os
from youtube_search import YoutubeSearch
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
# from spotify_sort import *
import threading

# declare wikipedia's language
wikipedia.set_lang('en')
language = 'en'

# Declare date, time
today = date.today()
d2 = today.strftime("%B %d, %Y")
now = datetime.now()

engine = pyttsx3.init()
search = ''

# Receive data from file Jeff-answer.yml
bot = ChatBot('Bot')
trainer = ListTrainer(bot)
data = open('data/Jeff-answer.yml', 'r', encoding='utf-8').readlines()
trainer.train(data)

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





# Auto reply
def botReply():
    question = questionField.get()
    question = question.capitalize()
    textarea.insert("end", 'User: ' + str(question) + '\n')
    textarea.see("end")
    questionField.delete(0, "end")


# Function transform speech to text
def speechToText():
    textarea.insert("end", str("Jeff: I'm listening \n"))
    engine.say("I'm listening")
    while True:
        textarea.insert("end", str("Jeff:...!!") + '\n')
        engine.runAndWait()
        Jeff_microphone = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as mic:
                audio = Jeff_microphone.record(mic, duration=3)
                text = Jeff_microphone.recognize_google(audio)

                questionField.delete(0, "end")
                questionField.insert(0, text)

                textarea.delete(1.0, "end")
                botReply()

                if 'today' in text:  # DATE
                    Jeff = today.strftime("%B %d, %Y")
                    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                    engine.say(Jeff)

                elif 'time' in text:  # TIME
                    global now
                    Jeff = now.strftime("%H : %M minutes")
                    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                    engine.say(Jeff)

                elif 'search for' in text:  # WIKIPEDIA
                    searching = text.replace('search for', '')
                    contents = wikipedia.summary(searching, sentences=3).split('\n')
                    textarea.insert("end", 'Jeff: ' + str(contents) + '\n')
                    engine.say(contents)


                elif 'weather' in text:
                    Jeff = 'Where do you want to know the weather?'
                    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                    engine.say(Jeff)
                    engine.runAndWait()
                    Jeff_microphone = speech_recognition.Recognizer()
                    try:
                        with speech_recognition.Microphone() as mic:
                            audio = Jeff_microphone.record(mic, duration=3)
                            city = Jeff_microphone.recognize_google(audio)

                        textarea.insert("end", 'User: ' + str(city) + '\n')
                    except Exception as e:
                        print(e)

                    ow_url = "http://api.openweathermap.org/data/2.5/weather?"

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
                        textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                        engine.say(Jeff)
                    else:
                        Jeff = "Cannot find your area"
                        textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                        engine.say(Jeff)
                elif 'stop music' in text:
                    pause_music(spotify=spotify, device_id=deviceID)
                    Jeff = 'Paused'
                    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                    engine.say(Jeff)
                    engine.runAndWait()

                    Jeff = 'Do you want to continue or stop'
                    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                    engine.say(Jeff)
                    engine.runAndWait()
                elif 'Spotify' in text:
                    class InvalidSearchError(Exception):
                        pass
                    Jeff = 'What do you want to play?'
                    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                    engine.say(Jeff)

                    auth_manager = SpotifyOAuth(
                        client_id='55d9d6208ee448f386daf66891f00837',
                        client_secret='c015cebd6f704b918b0c236028c252cb',
                        redirect_uri='http://localhost:8888/callback/',
                        scope='user-read-private user-read-playback-state user-modify-playback-state',
                        username='31kcfzjbjfcnfz6oekqo745gintm')
                    spotify = sp.Spotify(auth_manager=auth_manager)

                    engine.runAndWait()
                    r = speech_recognition.Recognizer()
                    # while True:
                    with speech_recognition.Microphone() as mic:
                        r.adjust_for_ambient_noise(mic)
                        audio = r.listen(mic)
                        try:
                            command = r.recognize_google(audio)
                        except UnknownValueError:
                            continue
                    textarea.insert("end", 'User: ' + str(command) + '\n')

                    words = command.split()
                    if len(words) < 1:
                        Jeff = 'Could not understand. Please try again!'
                        textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                        engine.say(Jeff)
                        engine.runAndWait()

                    name = ' '.join(words[1:])
                    try:

                        if words[0] == 'play':
                            uri = get_track_uri(spotify=spotify, name=name)
                            play_track(spotify=spotify, device_id=deviceID, uri=uri)
                            Jeff = 'Playing ' + name
                            textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                            engine.say(Jeff)
                            engine.runAndWait()

                            Jeff_microphone = speech_recognition.Recognizer()
                            # try:
                            #     with speech_recognition.Microphone() as mic:
                            #         audio = Jeff_microphone.record(mic, duration=3)
                            #         choice = Jeff_microphone.recognize_google(audio)
                            #
                            #     textarea.insert("end", 'User: ' + str(choice) + '\n')
                            #     if (choice == 'stop'):
                            #         break
                            #     else:
                            #         continue
                            #
                            # except InvalidSearchError:
                            # print(InvalidSearchError)

                        else:
                            Jeff = 'Specify either "album", "artist" or "play". Try Again'
                            textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                            engine.say(Jeff)
                            engine.runAndWait()
                    except InvalidSearchError:
                        print(InvalidSearchError)

                elif 'bye' in text:  # TURN OFF
                    Jeff = 'Goodbye boss\n'
                    engine.say(Jeff)
                    textarea.insert("end", 'Jeff: ' + str(Jeff))
                    engine.runAndWait()
                    break

                else:
                    Jeff = bot.get_response(text)
                    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
                    engine.say(Jeff)

        except Exception as e:
            print(e)


def searching_youtube():
    Jeff = 'What do you looking for?'
    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
    engine.say(Jeff)

    textarea.insert("end", str("Jeff:...!!\n"))
    engine.runAndWait()
    Jeff_microphone = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            audio = Jeff_microphone.record(mic, duration=3)
            text = Jeff_microphone.recognize_google(audio)

        textarea.insert("end", 'User: ' + str(text) + '\n')
        Jeff = 'Okay boss, searching for' + text.replace('searching for', '') + '\n'
        textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
        engine.say(Jeff)
        search = text.replace('searching for', '')
        url = f"https://www.youtube.com/search?q={search}"
        webbrowser.get().open(url)
    except Exception as e:
        print(e)


def playing_youtube():
    Jeff = 'What do you want to play?'
    textarea.insert("end", 'Jeff: ' + str(Jeff) + '\n')
    engine.say(Jeff)
    engine.runAndWait()
    Jeff_microphone = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            audio = Jeff_microphone.record(mic, duration=3)
            text = Jeff_microphone.recognize_google(audio)

        textarea.insert("end", 'User: ' + str(text) + '\n')
        Jeff = 'Okay boss, playing for' + text.replace('playing for', '') + '\n'
        textarea.insert("end", 'Jeff: ' + str(Jeff))
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


def get_track_uri(spotify: Spotify, name: str) -> str:
    # Replace all spaces in name with '+'
    class InvalidSearchError(Exception):
        pass
    original = name
    name = name.replace(' ', '+')
    results = spotify.search(q=name, limit=1, type='track')
    if not results['tracks']['items']:
        raise InvalidSearchError(f'No track named "{original}"')
    track_uri = results['tracks']['items'][0]['uri']
    return track_uri


def play_track(spotify=None, device_id=None, uri=None):
    spotify.start_playback(device_id=device_id, uris=[uri])


def pause_music(spotify=None, device_id=None):
    spotify.pause_playback(device_id=device_id)


def loop():
    thread = threading.Thread(target=speechToText)
    thread.setDaemon(True)
    thread.start()


root = Tk()
root.geometry('500x700')
root.config(bg="black")

logoPic = PhotoImage(file='robot.png')
logoPicLabel = Label(root, image=logoPic, bg='black')
logoPicLabel.pack(pady=20)

centerFrame = Frame(root)
centerFrame.pack(fill="both", expand=True)

textarea = Text(centerFrame, font=('Times new roman', 15, 'bold'), height=8, bg="black", fg='white')
scrollbar = Scrollbar(centerFrame, command=textarea.yview, orient='vertical')
textarea.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
textarea.pack(side=LEFT, fill=BOTH, expand=True)

questionField = Entry(root)

buttonAgain = Button(root, text="Talk to Jeff", command=loop, font=('Times new roman', 12, 'bold'), height=2,
                     bg='dark blue', fg='white')
buttonAgain.pack(pady=20)
mainloop()
