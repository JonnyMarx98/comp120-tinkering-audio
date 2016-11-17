from notes import *

def filepath(note):
    return str('Notes/' + str(note) + '_Note.wav')

# this will generate all the notes so only needs to run the first time
# for item in cMajor:
#     Note(item, sampleRate, sampleLength, bitDepth, volume)

# plays through cMajor
for item in cMajor:
    name, frequency = item
    winsound.PlaySound(filepath(name), winsound.SND_FILENAME)
