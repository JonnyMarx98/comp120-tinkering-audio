from notes import *
import winsound


# function to play note (takes string for note name)
def play(note):
    winsound.PlaySound(str('Notes/' + str(note) + '.wav'), winsound.SND_FILENAME)

# this will generate all the notes so only needs to run the first time

Note(item, sampleRate, sampleLength, bitDepth, volume)

for note in song:
    play(note[0])