import pygame
import time
from morse_dict import MORSE_CODE_DICT, reverse_morse_code_dict

# Load audio files for dot and dash
dot_sound = pygame.mixer.Sound('dot.wav')  # Replace with your dot sound file path
dash_sound = pygame.mixer.Sound('dash.wav')  # Replace with your dash sound file path

def play_morse_code(morse_code):
    print(morse_code)
    for symbol in morse_code:
        print(symbol)
        if symbol == '.':
            dot_sound.play()
            time.sleep(0.2)  # Short pause after dot
        elif symbol == '-':
            dash_sound.play()
            time.sleep(0.6)  # Longer pause after dash
        elif symbol == ' ':
            time.sleep(0.4)  # Pause for space between letters
        else:
            continue  # Ignore any unknown symbols

    # Wait for any sound currently playing to finish before exiting
    pygame.time.delay(1000)

# Example usage:
def text_to_morse(text):
    morse_message = []
    for char in text.upper():
        # print(char)
        if char in MORSE_CODE_DICT:
            # print(MORSE_CODE_DICT[char])
            morse_message.append(MORSE_CODE_DICT[char])
        else:
            morse_message.append(' ')  # Space for unknown characters
    return ' '.join(morse_message)

def capitalize_first_word(text):
    # Split the text into sentences using regex
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    # Capitalize the first word of each sentence
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    # Join the sentences back into a single string
    return ' '.join(capitalized_sentences)

def morse_to_text(morse_code):
    # Split the Morse code by spaces (words are separated by three spaces)
    words = morse_code.split('   ')
    decoded_message = []

    for word in words:
        letters = word.split()  # Split the word into letters
        decoded_word = ''.join(reverse_morse_code_dict.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)

    upper_message = ' '.join(decoded_message)
    return capitalize_first_word(upper_message)