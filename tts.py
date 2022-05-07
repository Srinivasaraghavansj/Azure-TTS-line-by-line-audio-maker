from azure.cognitiveservices.speech import SpeechSynthesizer, AudioDataStream, SpeechConfig
import time
import random


key=''
region='centralindia'

speech_config = SpeechConfig(subscription=key, region=region)
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)


str_pre = '<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="en-US-SaraNeural"><prosody rate="5%" pitch="0%">'
str_pre=str_pre.replace("</prosody>","").replace("</voice>","").replace("</speak>","")
str_post = '</prosody></voice></speak>'

if "mstts:express-as" in str_pre:
    str_pre = str_pre.replace("</mstts:express-as>","")
    str_post = "</prosody></mstts:express-as></voice></speak>"

# folder_name = 'TS audios'

folder_name = 'audio_test'

with open("/Users/ramesh/OX Drive/My files/Srini Files/tts to create wav/"+"content.txt","r") as f:
    n=1  ####THIS IS THE LINE NUMBER For output file(s)
    for u,i in enumerate(f.readlines()):
        if i == "\n":
            continue
        if n%15==0:
            rand = 10+random.randint(0,10)
            print(f"waiting for {rand} secs & Resetting")
            time.sleep(rand)
            speech_config = SpeechConfig(subscription=key, region=region)
            synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
        # speech_config = SpeechConfig(subscription=key, region=region)
        # synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
        print(str(u)+")",str(n)+")",i)
        ssml_string = str_pre + i + str_post
        result = synthesizer.speak_ssml_async(ssml_string).get()
        stream = AudioDataStream(result)
        # stream.save_to_wav_file("/Users/ramesh/OX Drive/My files/Srini Files/tts to create wav/"+f"{folder_name}/line{n}.wav")
        stream.save_to_wav_file("/Users/ramesh/Desktop/"+f"{folder_name}/line{n}.wav")
        n+=1
        # stream.save_to_wav_file("/Users/tarrun/Downloads/test audios/"+f"{folder_name}/line{n}.wav")
        # /Users/ramesh/OX Drive/My files/Srini Files/tts to create wav