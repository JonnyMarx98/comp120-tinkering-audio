import wave, struct, math, random
from noteFrequencies import *

sampleLength = 44100/16
sampleRate = float(44100)
volume = 1
bitDepth = 32767

notePrefix = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']
fSharpMinor = ['FS', 'GS', 'A', 'B', 'CS', 'D', 'E']
CMajor = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def notegen():
    prefixChoice = random.randint(0, 11)
    suffixChoice = random.randint(0, 1)

    return notePrefix[prefixChoice] + str(4)

# denotes which notes are loaded and saved
#notes = [C4, CS4, D4, DS4, E4, F4, FS4, G4, GS4, A4, AS4, B4, C5]

# defining scales
 #cMajor = [C4, D4, E4, F4, G4, A4, B4, C5]

class Note:

    def __init__(self, (name, frequency), samplerate, samplelength, bitdepth, volume, identifyer):
        self.frequency = frequency
        self.note = wave.open('Notes/' + str(name) + '_' + identifyer + '.wav', 'w')
        self.note.setparams((2, 2, bitdepth, samplelength, 'NONE', 'not compressed'))

        for i in range(0, samplelength):
            value = math.sin(2.0 * math.pi * frequency * (i / samplerate)) * (volume * bitdepth)
            packed_value = struct.pack('h', value)
            self.note.writeframes(packed_value)
            self.note.writeframes(packed_value)

        self.note.close()