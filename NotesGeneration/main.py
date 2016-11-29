from notes import *
import winsound, pygame

# function to play note (takes string for note name)
def play(note, identifyer):
    winsound.PlaySound(str('Notes/' + str(note) + '_' + identifyer + '.wav'), winsound.SND_FILENAME)

# this will generate all the notes so only needs to run the first time

# Note(RandomNote, sampleRate, sampleLength, bitDepth, volume)
#
# play(RandomNote)
melody = []
chorus = []
# set this to procedurally generate rhythm
# total bar length = 2, split up randomly taking 1/2, 1/4, 1/8, 1/16, 1/32 and append to list
# make sure it doesn't go over minus
# randomBeat = random.randint(2, 4, 8, 16, 32)
# print 1/randomBeat
notelength = [4, 2, 4, 4, 2, 2, 16, 16, 8, 4, 4, 8, 4, 2, 4, 4, 4, 8, 8]

for i in xrange(len(notelength)):
    samplelength = 44100/(notelength[i])
    noteChoice = notegen()
    noteInput = (noteChoice, notes[noteChoice])
    print noteInput
    Note(noteInput, sampleRate, samplelength, bitDepth, volume, ('melody' + str(i)))
    melody.append(noteChoice)

for i in xrange(8):
    samplelength = 44100 / 16
    noteChoice = notegen()
    noteInput = (noteChoice, notes[noteChoice])
    print noteInput
    Note(noteInput, sampleRate, samplelength, bitDepth, volume, 'chorus')
    chorus.append(noteChoice)

while True:

    for i in xrange(2):
        print 'melody'
        j = 0
        for pitch in melody:
            play(pitch, ('melody' + str(j)))
            j += 1
        j = 0

    for i in xrange(2):
        for times in xrange(3):
            print 'chorus'
            for pitch in chorus:
                print times
                for i in xrange(times):
                    play(pitch, 'chorus')