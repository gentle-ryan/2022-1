# slow.py
#
# 실습08 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#
# Generates 0.5x slowed down sound
#
# Usage:
#
# python slow.py orignal.wav slow.wav 
#
import sys
import wave
import struct

infilename = sys.argv[1]
outfilename = sys.argv[2]
sound = wave.open(infilename, "r")
newsound = wave.open(outfilename, "w")
params = sound.getparams()
newsound.setnchannels(params.nchannels)
newsound.setsampwidth(params.sampwidth)
newsound.setframerate(params.framerate)

sampleRate = 8000.0 # hertz

n = sound.getnframes()
for i in range(n):
    frame = sound.readframes(1)
    newsound.writeframesraw(frame)
    newsound.writeframesraw(frame)

newsound.close()