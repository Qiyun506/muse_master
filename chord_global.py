# Import necessary modules
from chord_mapping import *  # Ensure this file defines the chord_mappings dictionary
from music21 import environment, stream, chord, note, meter,clef
from tqdm import tqdm

# Set up MuseScore path
environment.set('musicxmlPath', "D:/fun_purpose/music_master/muse/bin/MuseScore3.exe")
print("MuseScore Path:", environment.get('musicxmlPath'))