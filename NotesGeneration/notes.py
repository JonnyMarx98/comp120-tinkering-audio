import wave, struct, math, cmath, random


class Note:

    def __init__(self, frequency, samplerate, samplelength, bitdepth, volume):
        self.frequency = frequency
        self.note = wave.open('sound.wav', 'w')
        self.note.setparams((2, 2, bitdepth, samplelength, 'NONE', 'not compressed'))

        for i in range(0, samplelength):
            value = math.sin(2.0 * math.pi * frequency * (i / samplerate)) * (volume * bitdepth)
            packed_value = struct.pack('h', value)
            self.note.writeframes(packed_value)
            self.note.writeframes(packed_value)

        self.note.close()