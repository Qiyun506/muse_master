from chord_global import *
from chord_type import *

# 设置MuseScore路径
environment.set('musicxmlPath', "D:/fun_purpose/music_master/muse/bin/MuseScore3.exe")

# 和弦序列
chord_sequence = ["C", "G", "Am", "F"]

# 创建Score（乐谱）
score = stream.Score()

# 创建左手和右手部分
right_hand = stream.Part()
left_hand = stream.Part()

# 设置左右手的谱号
right_hand.append(clef.TrebleClef())  # 右手高音谱号
left_hand.append(clef.BassClef())    # 左手低音谱号

# 添加时间签名
time_signature = meter.TimeSignature("4/4")
right_hand.append(time_signature)
left_hand.append(time_signature)

# 节奏类型函数
def generate_arpeggio(chord_notes, duration=4.0):
    """生成分解和弦"""
    return [note.Note(p, quarterLength=duration / len(chord_notes)) for p in chord_notes]

def generate_chord_sustained(chord_notes, duration=4.0):
    """生成和弦铺底"""
    return chord.Chord(chord_notes, quarterLength=duration)

# 为左右手生成伴奏
for chord_symbol in tqdm(chord_sequence, desc="Generating Accompaniment", unit="chord"):
    # Parse root and type
    if len(chord_symbol) > 1 and chord_symbol[-1].isalpha():
        root = chord_symbol[:-1]  # E.g., "A" in "Am"
        chord_type = chord_symbol[-1]  # E.g., "m" in "Am"
    else:
        root = chord_symbol  # Standalone root, e.g., "C"
        chord_type = ""  # Default to major

    # Generate chord notes
    chord_notes = [n.nameWithOctave for n in generate_chord(root + "4", chord_type)]

    # 右手：分解和弦
    arpeggio = generate_arpeggiated_variation(chord_notes, duration=4.0)
    for n in arpeggio:
        right_hand.append(n)

    # 左手：和弦的根音
    root_note = note.Note(chord_notes[0], quarterLength=4.0)  # 左手弹根音
    left_hand.append(root_note)

# 将左右手部分添加到总谱
score.append(right_hand)
score.append(left_hand)

# 保存和显示乐谱
save_score(score, output_file="left_right_hands.xml")
