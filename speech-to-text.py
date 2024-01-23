import os
from pydub import AudioSegment
import speech_recognition as sr

fm = input("Do you want to read data from your microphone or from a file? Enter 'microphone' or 'file': ")
match fm:
    case 'microphone':
        language = input("In what language will you record? Enter 'ru', 'en' or 'de': ")
        with sr.Microphone() as source:
            # initialize the recognizer
            r = sr.Recognizer()
            # adjust to a noise level
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            # read the audio data from the default microphone
            audio_data = r.listen(source)
            print("Recognizing...")
            # convert speech to text
            match language:
                case 'ru':
                    text = r.recognize_google(audio_data, language="ru-RU")
                case 'en':
                    text = r.recognize_google(audio_data, language="en-EN")
                case 'de':
                    text = r.recognize_google(audio_data, language="de-DE")
            print(text)
    case 'file':
        filename = input("Enter a valid pathname to an audio file: ")
        if not os.path.isfile(filename):
            print(filename, "is not a valid path name.")
            quit()
        # convert .mp3 to .wav if needed
        flag = False
        if filename[filename.find('.'):] == '.mp3':
            flag = True
            sound = AudioSegment.from_mp3(filename)
            sound.export(f"{filename[:-4]}.wav", format="wav")
            filename = f"{filename[:-4]}.wav"
        # initialize the recognizer
        r = sr.Recognizer()
        # choose a language
        language = input("In what language is the recording? Enter 'ru', 'en' or 'de': ")
        # open the file
        with sr.AudioFile(filename) as source:
            # adjust to a noise level
            r.adjust_for_ambient_noise(source)
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            match language:
                case 'ru':
                    text = r.recognize_google(audio_data, language="ru-RU")
                case 'en':
                    text = r.recognize_google(audio_data, language="en-EN")
                case 'de':
                    text = r.recognize_google(audio_data, language="de-DE")
            # print text
            print(text)
        if flag:
            os.remove(filename)
    case _:
        print(fm, "is not an option.")
        quit()
