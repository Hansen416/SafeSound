import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100

duration = 10
 
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)

sd.wait()

write("password_1.wav", freq, recording)

wv.write("password_2.wav", recording, freq, sampwidth=2)