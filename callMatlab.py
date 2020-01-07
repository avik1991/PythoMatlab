import matlab.engine
eng = matlab.engine.start_matlab()
tf = eng.isprime(37)
print(tf)
import webbrowser
webbrowser.open('https://i.imgur.com/FVldYF4.png')