import os
from gtts import gTTS
import subprocess
import platform


# Step 1: Setup Text to Speech models

# gTTS function (unchanged)
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    play_audio(output_filepath)


    

# Universal audio playback function
def play_audio(filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', filepath])
        elif os_name == "Windows":  # Windows
            # Use a more reliable method for Windows
            subprocess.run(['ffplay', '-nodisp', '-autoexit', filepath], 
                          stdout=subprocess.DEVNULL, 
                          stderr=subprocess.DEVNULL)
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Test the functions
if __name__ == "__main__":
    input_text = "Hi this is Ai with Hassan, autoplay testing!"
    
    # Test gTTS
    print("Testing gTTS...")
    text_to_speech_with_gtts(input_text, "gtts_testing.mp3")
    
   
