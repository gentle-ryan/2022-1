# whitenoise.py
#
# 실습08 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#
# Usage:
#
# python whitenoise.py amplitude duration whitenoise.wav
#
# eg) python whitenoise.py 0.5 10 whitenoise.wav
#
import sys
import wave
import random
import struct

noise = wave.open("whitenoise.wav", "w")

sampleRate = 8000.0 # hertz
noise.setframerate(sampleRate)
noise.setnchannels(1)
noise.setsampwidth(2)

duration = 5

n = int(duration*sampleRate)
data = bytearray(b'')
for _ in range(n):
    amp = random.randint(-32768, 32767)
    data.extend(struct.pack('<h', amp))

noise.writeframesraw(data)
noise.close()