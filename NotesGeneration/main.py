from notes import *
import winsound


# function to play note (takes string for note name)
def play(note):
    winsound.PlaySound(str('Notes/' + str(note) + '.wav'), winsound.SND_FILENAME)

# this will generate all the notes so only needs to run the first time
for item in notes:
    Note(item, sampleRate, sampleLength, bitDepth, volume)

# plays through cMajor
for item in cMajor:
    play(item[0])

song = [E4, D4, C4, D4, E4, E4, E4]

for note in song:
    play(note[0])