# waveform.py
#
# 실습08 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#
# Plot waveform
#
# Usage:
#
# python waveform.py sound.wav waveform.png
#
import sys
import wave
import matplotlib.pyplot

sound = wave.open("sori.wav", "r")

amps = []
for i in range(sound.getnframes()):
    b = sound.readframes(1)
    amp = int.from_bytes(b, byteorder='little', signed=True)
    amps.append(amp)


# 가로축은 프레임의 번호, 세로축은 프레임의 정수값

matplotlib.pyplot.plot(amps)
matplotlib.pyplot.show()