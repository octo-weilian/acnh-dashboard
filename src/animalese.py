from src import *
import string
from pydub import AudioSegment
import base64


def text_to_animalese(text,file,speed_up=2.3):
    text = text.lower()
    sound = AudioSegment.empty()
    digraphs = ["ch", "sh", "ph", "th", "wh"]

    for i in range(len(text)):
        char = None

        if i < len(text)-1 and text[i] != ' ':
            if  (text[i] + text[i+1]) in digraphs:
                char = text[i] + text[i+1]
            elif text[i] in string.ascii_lowercase:
                char = text[i]
            else:
                char = "bebebese"
            
            fname = Path(f"./src/animalese/sound_files/{char}.wav")
            if fname.exists():
                sound += AudioSegment.from_file(fname,format='wav')
            else:
                raise OSError(f"{fname} does not exists.")
            
    new_frame_rate = sound.frame_rate*speed_up
    sound = sound._spawn(sound.raw_data, overrides={"frame_rate":new_frame_rate })
    sound.set_frame_rate(new_frame_rate)
    sound.export(file, format="wav")

    return str(Path(file).absolute())

def play_sound(wav_file):
    with open('animalese_sound.wav','rb') as f:
        b64 = base64.b64encode(f.read()).decode()
        md = f'<audio autoplay="true"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        return st.markdown(md,unsafe_allow_html=True)


