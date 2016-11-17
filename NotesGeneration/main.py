import wave, struct, math, cmath, random, notes


sampleLength = 44100*2
frequency = 261.6
sampleRate = float(44100)
volume = 1
bitDepth = 32767

noteParams = [frequency, sampleRate, sampleLength, bitDepth, volume]

middleC = notes.Note(noteParams[0], noteParams[1], noteParams[2], noteParams[3], noteParams[4])
