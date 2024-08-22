# sinewave.py
#
# Generate sinewave
#
# set default framerate = 8000, sampwidth = 2
#
# Usage:
#
# python sinewave.py frequency amplitude duration sinewave.wav
#
# eg) python sinewave.py 440 0.5 3 sinewave.wav
#
#
import sys
import wave 
import math, struct

sine = wave.open("sine.wav", "w")

sampleRate = 8000
sine.setframerate(sampleRate)
sine.setnchannels(1)
sine.setsampwidth(2)

frequency = 440   # Hz
amplitude = 0.5   # 0 to 1
duration = 3      # seconds

framerate = 8000
sampwidth = 2
maxVolume = 2**(sampwidth*8 - 1) - 1

volume = int(amplitude * maxVolume)
n = int(duration * framerate)   # number of frames

packed = bytearray(b'')
for i in range(n) :
    t = i / sampleRate
    y = int(volume * math.sin(2*math.pi * frequency * t))
    packed.extend(struct.pack('<h', int(y)))

sine.writeframesraw(packed)
sine.close()