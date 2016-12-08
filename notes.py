import wave
import struct
import math
import random
from noteFrequencies import *


sampleLength = 44100/16
sampleRate = float(44100)
volume = 1
bitDepth = 32767
notePrefix = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']
fSharpMinor = ['FS', 'GS', 'A', 'B', 'CS', 'D', 'E']
CMajor = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def note_gen():
    prefix_choice = random.randint(0, len(notePrefix)-1)
    suffix_choice = random.randint(0, 1)

    return notePrefix[prefix_choice] + str(4)

sound_params = (2, 2, sampleRate, sampleLength*random.randint(2, 5), 'NONE', 'Not compressed')
sound_params2 = (2, 2, sampleRate, sampleLength*random.randint(2, 5), 'NONE', 'Not compressed')

noise_out = wave.open('melody1.wav', 'w')
noise_out2 = wave.open('melody2.wav', 'w')
cool_noise_out = wave.open('CoolPlaneSound.wav', 'w')

noise_out.setparams(sound_params)
noise_out2.setparams(sound_params2)
cool_noise_out.setparams(sound_params)

values = []
values2 = []
cool_values = []


def save_sound(noise):
    noise.close()


def random_note(identifier, noise):
    note_choice = note_gen()
    for i in range(0, sound_params[3]):
        value = math.sin(2.0 * math.pi * notes[note_choice] * (i / sound_params[2])) * (volume * bitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, sound_params[0]):
            identifier.append(packaged_value)
    value_str = ''.join(identifier)
    noise.writeframes(value_str)


def cool_plane_sound():
    loop_count = 0
    melody1 = enumerate(values)
    for index, val in melody1:
        if loop_count < 1000:
            loop_count += 1
            unpacked_values = struct.unpack('h', val)
            unpacked_ints = reduce(lambda rst, d: rst * 10 + d, unpacked_values)
            packaged_value = struct.pack('h', unpacked_ints)
            for j in xrange(0, sound_params[0]):
                cool_values.append(packaged_value)
            value_str = ''.join(cool_values)
            cool_noise_out.writeframes(value_str)


def echo(list):
    """Echo function that is not used as it wasn't working"""
    count = 0
    echo_list = []
    for i in list:
        count += 1
        if count < 10000:
            echo_value = i
        else:
            echo_value = i + (list[count - 10000] * 0.4)
        echo_list.append(echo_value)
    return new_list


class Note:
    def __init__(self, (name, frequency), sampleRate, samplelength, bitdepth, identifyer):
        self.note = wave.open('Notes/' + str(name) + '_' + identifyer + '.wav', 'w')
        self.note.setparams((2, 2, bitdepth, samplelength, 'NONE', 'not compressed'))
        volume = 0
        length = samplelength

        for i in range(0, samplelength):
            half = (samplelength + 1)/2
            if i < half and volume < 0.9:
                volume = float(i*2)/samplelength
            elif i > half and volume > 0.1:
                volume = samplelength/float(i*2)
            value = math.sin(2.0 * math.pi * frequency * (i / sampleRate)) * (volume * bitdepth)
            packed_value = struct.pack('h', value)
            self.note.writeframes(packed_value)
            self.note.writeframes(packed_value)

        self.note.close()



