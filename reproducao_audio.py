from pygame import mixer  # Load the popular external library


class AUDIO:
    _caminho_falas = 'falas\\'
    BOM_DIA = _caminho_falas + 'bom dia.mp3'


class PlayerAudio:

    def __enter__(self):
        mixer.init()

    def __exit__(self, exc_type, exc_val, exc_tb):
        mixer.stop()

    def play(self, caminho: str):
        mixer.music.load(caminho)
        mixer.music.play()