from gtts import gTTS
import os
fh=open("text.txt","r")
mytext=fh.read()
l='en'
output=gTTS(text=mytext,lang=l,slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")
