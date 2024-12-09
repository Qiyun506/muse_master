
from chord_global import *
# 节奏类型函数
def generate_arpeggio(chord_notes, duration=1.0):
    """生成分解和弦"""
    return [note.Note(p, quarterLength=duration / len(chord_notes)) for p in chord_notes]

def generate_chord_sustained(chord_notes, duration=1.0):
    """生成和弦铺底"""
    return chord.Chord(chord_notes, quarterLength=duration)

def generate_staccato(chord_notes, duration=1.0):
    """生成跳音伴奏"""
    return [note.Note(p, quarterLength=duration / len(chord_notes) * 0.5) for p in chord_notes]

def generate_arpeggiated_variation(chord_notes, duration=1.0):
    """生成CGEG样式的分解和弦"""
    # 按顺序生成 CGEG
    pattern = [chord_notes[0], chord_notes[2], chord_notes[1], chord_notes[2]]  # C, G, E, G
    return [note.Note(p, quarterLength=duration / len(pattern)) for p in pattern]

# save scred
def save_score(score, output_file="output.xml"):
    """Save the score as a MusicXML file and display it using MuseScore."""
    try:
        score.write('musicxml', fp=output_file)
        print(f"MusicXML file saved as '{output_file}'")

        # Display the score with MuseScore
        score.show()  # Opens in MuseScore or configured viewer
    except Exception as e:
        print(f"Error displaying the score: {e}")


# Function to generate a chord dynamically
def generate_chord(root, chord_type):
    """Generate a chord based on root and chord type."""
    if chord_type not in chord_mappings:
        raise ValueError(f"Chord type '{chord_type}' not found in chord mappings.")
    intervals = chord_mappings[chord_type]
    return [note.Note(root).transpose(i) for i in intervals]