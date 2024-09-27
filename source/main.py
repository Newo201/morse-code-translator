import pygame
from morse_functions import text_to_morse, play_morse_code, morse_to_text

# Initialize Pygame mixer
pygame.mixer.init()


if __name__ == "__main":
    # Example conversion
    example_text = "Hello, World"
    morse_output = text_to_morse(example_text)
    play_morse_code(morse_output)
    # Clean up the mixer
    pygame.mixer.quit()
