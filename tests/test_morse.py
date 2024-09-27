import pytest
from unittest.mock import patch
from source.main import text_to_morse, morse_to_text, play_morse_code
# from morse_code import text_to_morse, morse_to_text, play_morse_code

def test_text_to_morse():
    assert text_to_morse("Hello World") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
    assert text_to_morse("SOS") == "... --- ..."
    assert text_to_morse("123") == ".---- ..--- ...--"
    assert text_to_morse("Unknown!") == "..- -. -.- -. --- .-- -.-- --- ..- -.--."

def test_morse_to_text():
    assert morse_to_text(".... . .-.. .-.. ---   .-- --- .-. .-.. -..") == "Hello World"
    assert morse_to_text("... --- ...") == "SOS"
    assert morse_to_text(".---- ..--- ...--") == "123"
    assert morse_to_text("..- -. -.- -. --- .-- -.-- --- ..- -.--.") == "Unknown"

def test_morse_to_text_with_unknown_characters():
    assert morse_to_text("... --- ... @") == "SOS "
    assert morse_to_text("... --- ... ???") == "SOS "

@patch('pygame.mixer.Sound')  # Mock pygame Sound
def test_play_morse_code(mock_sound):
    play_morse_code("... --- ...")
    assert mock_sound.call_count == 5  # 3 dots, 2 spaces between letters
    # Each dot and dash sound should be called
    assert mock_sound.return_value.play.call_count == 3  # Three dot sounds for 'SOS'

@pytest.mark.parametrize("morse_input,expected_output", [
    (".... . .-.. .-.. ---", "Hello"),
    ("... --- ...", "SOS"),
    ("-.. .- ... ....", "DASH"),
])
def test_morse_code_conversion(morse_input, expected_output):
    decoded = morse_to_text(morse_input)
    assert decoded == expected_output