from notes import *

# this will generate all the notes so only needs to run the first time
for item in cMajor:
    Note(item, sampleRate, sampleLength, bitDepth, volume)

# plays through cMajor
for item in cMajor:
    name, frequency = item
    filePath = str('Notes/' + str(name) + '_Note.wav')
    winsound.PlaySound(filePath, winsound.SND_FILENAME)