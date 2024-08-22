# musicbox.py
#
# 실습08 컴퓨터의 개념 및 실습 수업용 파일입니다.
# 언어학과 2021-12659 박유나에 의해 작성되었습니다.
#
# Usage :
#
# python musicbox.py merry-go-round.txt merry-go-round.wav
#
import sys
import wave
import math, struct
import random

inputfilename = sys.argv[1]
outfilename = sys.argv[2]
music = wave.open(outfilename, "w")
file = open(inputfilename)
firstline = file.readline()


sampleRate = 8000
music.setframerate(sampleRate)
music.setnchannels(1)
music.setsampwidth(2)


# http://pages.mtu.edu/~suits/notefreqs.html
# http://newt.phys.unsw.edu.au/jw/notes.html
# https://en.wikipedia.org/wiki/Musical_note
# http://blog.acipo.com/wave-generation-in-python/
# http://meettechniek.info/additional/additive-synthesis.html

notenum = {'do4' : 60, 'do5' : 72, 'dos5' : 73, 're5' : 74, 'res5' : 75, 'mi4' : 64, 
    'mi5' : 76, 'fa5' : 77, 'fas5' : 78, 'sol5' : 79 , 'ra4' : 69, 'ra5' : 81, 'si4' : 71 , 'si5' : 83 }

def tone(freq, amp, dur):
    sampleRate = 8000.0

    framerate = 8000
    sampwidth = 2
    maxVolume = 2**(sampwidth*8 - 1) - 1

    volume = int(amp * maxVolume)
    n = int(dur * framerate)

    packed = bytearray(b'')
    for i in range(n) :
        t = i / sampleRate
        y = int(volume * math.sin(2*math.pi * freq * t))
        packed.extend(struct.pack('<h', int(y)))
    return packed

def midi2freq(midi):
    freq = 440*2**((midi-69)/12)
    return freq

def bak2dur(bak):
    if bak == '4':
        return 0.5
    elif bak == '8':
        return 0.25
    elif bak == '4.':
        return 0.75
    elif bak == '2':
        return 1
    elif bak == '2.':
        return 2

for line in file:
    notes = line.split()
    for word in notes:
        if word[2] == 's':
            note = word[0:4]
            if len(word) == 7:
                bakja = word[5:7]
            else:
                bakja = word[5]

        elif word[2] == 'l':
            note = word[0:4]
            if len(word) == 7:
                bakja = word[5:7]
            else:
                bakja = word[5]

        else:
            note = word[0:3]
            if len(word) == 6:
                bakja = word[4:6]
            else:
                bakja = word[4]
        midi = notenum[note]
        freq = midi2freq(midi)
        amp = 0.5
        dur = bak2dur(bakja)
        packed = tone(freq, amp, dur)

music.writeframesraw(packed)
music.close()