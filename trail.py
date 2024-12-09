

from chord_global import *
from chord_type import *

# Generate and print a minor chord
root = "C4"
chord_type = "m"
minor_chord = generate_chord(root, chord_type)
print("Generated Minor Chord:", [n.nameWithOctave for n in minor_chord])


# Define a fixed chord sequence for the score
chord_sequence = [
    chord.Chord(minor_chord),  # C Minor Chord (Dynamically generated)
    chord.Chord(["G3", "B3", "D4"]),  # G Major Chord
    chord.Chord(["A3", "C4", "E4"]),  # A Minor Chord
    chord.Chord(["F3", "A3", "C4"]),  # F Major Chord
]

# Create a music stream and set the time signature to 4/4
score = stream.Stream()
time_signature = meter.TimeSignature("4/4")  # 4/4 time signature
score.append(time_signature)  # Add time signature at the start of the score

# Add chords to the stream
for c in chord_sequence:
    score.append(c)

# Print details of the stream's elements
print("\nChord Sequence in Stream:")
for element in score:
    if isinstance(element, chord.Chord):
        print(f"Chord: {', '.join(p.nameWithOctave for p in element.pitches)}")
    elif isinstance(element, meter.TimeSignature):
        print(f"Time Signature: {element.ratioString}")
    else:
        print(f"Unknown Element: {element}")


save_score(score)


