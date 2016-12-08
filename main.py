from notes import *
from noteFrequencies import *
import winsound
import wave
import struct
import sys
import pygame
import random
from pygame.locals import *


pygame.init()


def play(note, identifier):

    winsound.PlaySound(str('Notes/' + str(note) + '_' + identifier + '.wav'), winsound.SND_FILENAME)

# initialising the arrays to save the notes to
melody = []
chorus = []


def generate_song(melody_list, chorus_list):

    note_marker = 0

    for i in xrange(2):
        for i in xrange(8):
            note_marker += 1
            sample_length = 44100 / (i + 1)
            note_choice = notegen()
            note_input = (note_choice, notes[note_choice])
            print note_input
            Note(note_input, sampleRate, sample_length, bitDepth, ('melody' + str(note_marker)))
            melody_list.append(note_choice)

    for i in xrange(8):
        sample_length = 44100 / 16
        note_choice = notegen()
        note_input = (note_choice, notes[note_choice])
        print note_input
        Note(note_input, sampleRate, sample_length, bitDepth, 'chorus')
        chorus_list.append(note_choice)

    return melody, chorus


# defining key presses
def g_key():

    generate_song(melody, chorus)
    print 'press space to play once'
    print 'press i to play infinitely'


def c_key():

    random_note(values, noise_out)
    cool_plane_sound()
    print 'CoolPlaneSound.wav saved'
    winsound.PlaySound('CoolPlaneSound.wav', winsound.SND_FILENAME)


def one_key():
    print "added random notes to melody1.wav"
    random_note(values, noise_out)


def two_key():

    print "added random notes to melody2.wav"
    random_note(values2, noise_out2)


def return_key():

    print 'melodys saved'
    save_sound(noise_out)
    save_sound(noise_out2)


def i_key():
    for i in xrange(4):
        print 'melody'
        j = 0
        for pitch in melody:
            j += 1
            play(pitch, ('melody' + str(j)))
        j = 0

    for i in xrange(3):
        for times in xrange(3):
            print 'chorus'
            for pitch in chorus:
                print times
                for n in xrange(times):
                    play(pitch, 'chorus')


def space_key():
    for song in xrange(1):
        for i in xrange(4):
            print 'melody'
            j = 0
            for pitch in melody:
                j += 1
                play(pitch, ('melody' + str(j)))
            j = 0

        for i in xrange(3):
            for times in xrange(3):
                print 'chorus'
                for pitch in chorus:
                    print times
                    for i in xrange(times):
                        play(pitch, 'chorus')
        print 'press space to play song'
        print 'press i to play song infinitely'
        print 'press 1 to write random note to melody1.wav'
        print 'press 2 to write random note to melody2.wav'
        print 'press enter to save melody1.wav'
        print 'press keypad enter to save melody2.wav'

print 'press g to generate song'
print 'press c to play Cool Plane Sound'
print 'press 1 to write random note to melody1.wav'
print 'press 2 to write random note to melody2.wav'
print 'press enter to save melodies'

Width = 300
Height = 200
window = pygame.display.set_mode((Width, Height), 0, 32)
pygame.display.set_caption('Press keys in this window')

controls = {'g': g_key,
            'c': c_key,
            '1': one_key,
            '2': two_key,
            'return': return_key,
            'i': i_key,
            'space': space_key}

while True:

    key = pygame.key.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            key_type = pygame.key.name(event.key)

            if key_type in controls:
                controls[key_type]()


