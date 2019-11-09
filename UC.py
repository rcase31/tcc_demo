from reconhecimento_audio import *
from reconhecimento_video import *
from reproducao_audio import *

class Estado:
    ESPERA = 0
    LEITURA = 1
    AGUARDA_OBJETO = 2
    ORIENTACAO = 3
    atual = None

    def __init__(self):
        self.atual = self.ESPERA

    def incrementa(self):
        self.atual += 1

    def volta_inicio(self):
        self.__init__()

    def aguarda_fala(self, palavra, limite: int=-1):
        contador = 0
        while not aguarda_audio(palavra):
            contador += 1
            if limite == contador:
                break
        self.incrementa()


if __name__ == '__main__':
    estado = Estado()

    player = PlayerAudio()
    with player:
        player.play(AUDIO.BOM_DIA)
    estado.aguarda_fala('testando')
    with player:
        player.play(AUDIO.BOM_DIA)












