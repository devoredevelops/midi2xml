import pytest
import xml.etree.ElementTree as ET
from main import write_measure_attributes


@pytest.mark.parametrize(
    "current_measure, key_accidentals, time_signature, clef_type, expected",
    [
        # Positive cases
        (
            1,
            0,
            ET.Element("time_signature", numerator="4", denominator="4"),
            "treble",
            ET.Element(
                "attributes",
                ET.Element("divisions", text="24"),
                ET.Element("key", ET.Element("fifths", text="0")),
                ET.Element(
                    "time",
                    ET.Element("beats", text="4"),
                    ET.Element("beat-type", text="4"),
                ),
                ET.Element(
                    "clef", ET.Element("sign", text="G"), ET.Element("line", text="2")
                ),
            ),
        ),
        (
            2,
            -2,
            ET.Element("time_signature", numerator="3", denominator="8"),
            "bass",
            ET.Element(
                "attributes",
                ET.Element("divisions", text="24"),
                ET.Element("key", ET.Element("fifths", text="-2")),
                ET.Element(
                    "time",
                    ET.Element("beats", text="3"),
                    ET.Element("beat-type", text="8"),
                ),
                ET.Element(
                    "clef", ET.Element("sign", text="F"), ET.Element("line", text="4")
                ),
            ),
        ),
        # Negative cases
        (
            3,
            1,
            ET.Element("time_signature", numerator="5", denominator="4"),
            "invalid",
            None,
        ),
        (
            4,
            3,
            ET.Element("time_signature", numerator="2", denominator="2"),
            "treble",
            None,
        ),
    ],
)
def test_write_measure_attributes(
    current_measure, key_accidentals, time_signature, clef_type, expected
):
    # Arrange

    # Act
    result = write_measure_attributes(
        current_measure, key_accidentals, time_signature, clef_type
    )

    # Assert
    assert ET.tostring(result) == ET.tostring(expected)
