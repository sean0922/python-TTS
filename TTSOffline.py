import pyttsx3

# init
engine = pyttsx3.init() 
# get details of speaking rate
rate = engine.getProperty("rate")
print(rate)
# setting new voice rate (faster)
engine.setProperty("rate", 200)
# get details of all voices available
voices = engine.getProperty("voices")
print(voices)
#start 
print('開始語音撥放...')
engine.say('我叫做王小明，大家好～')
#waiting 
engine.runAndWait()