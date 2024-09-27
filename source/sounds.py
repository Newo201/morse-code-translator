from pydub import AudioSegment
from pydub.generators import Sine

# Function to create dot and dash sounds
def create_morse_code_sounds(dot_duration=100, dash_duration=300, volume=-10):
    # Create a dot sound (short beep)
    dot = Sine(1000).to_audio_segment(duration=dot_duration).apply_gain(volume)
    
    # Create a dash sound (long beep)
    dash = Sine(1000).to_audio_segment(duration=dash_duration).apply_gain(volume)
    
    return dot, dash

# Save sounds to files
def save_sounds(dot, dash):
    dot.export("dot.wav", format="wav")
    dash.export("dash.wav", format="wav")

if __name__ == "__main__":
    dot, dash = create_morse_code_sounds()
    save_sounds(dot, dash)
    print("Dot and dash sounds have been created as 'dot.wav' and 'dash.wav'.")