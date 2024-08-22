# reverse.py
#
# Usage:
#
# python reverse.py sori.wav reversed.wav
#
import sys
import wave
import random
import struct

sampleRate = 8000.0 # hertz

infilename = sys.argv[1]
outfilename = sys.argv[2]
sound = wave.open(infilename, "r")
newsound = wave.open(outfilename, "w")
params = sound.getparams()
newsound.setnchannels(params.nchannels)
newsound.setsampwidth(params.sampwidth)
newsound.setframerate(params.framerate)

newsoundframes = b''
n = sound.getnframes()
for i in range(n):
    sound.setpos(n-i-1)
    newsound.writeframesraw(sound.readframes(1))

newsound.close()
