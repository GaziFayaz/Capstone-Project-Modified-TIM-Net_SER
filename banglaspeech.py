from banglaspeech2text import Speech2Text

stt = Speech2Text()

transcription = stt.transcribe("sound recordings/ang_21.wav")
print(transcription)
f = open("transcript.txt", "w", encoding="utf-8")
f.write(transcription)
f.close()
