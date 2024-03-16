import music21
from music21 import harmony


def chord_progression_to_xml(progression):
    # Create a music21 stream to hold the chords
    stream = music21.stream.Stream()

    # Iterate through each chord in the progression
    for chord_str in progression:
        # Create a music21 Chord object from the chord string
        chord = harmony.ChordSymbol(chord_str)

        # Get the MIDI pitches for the chord
        midi_pitches = [p.midi for p in chord.pitches]

        # Create a music21 Chord object with the MIDI pitches
        midi_chord = music21.chord.Chord(midi_pitches)

        # Set the duration of the chord to a quarter note
        midi_chord.duration.quarterLength = 1

        # Append the chord to the stream
        stream.append(midi_chord)

    # Write the stream to MusicXML format
    xml = music21.musicxml.m21ToXml.GeneralObjectExporter().parse(stream)

    return xml


# Example usage
progression = ["Cmaj7", "Am7", "Dm7", "G7"]
xml_output = chord_progression_to_xml(progression)
print(xml_output)
