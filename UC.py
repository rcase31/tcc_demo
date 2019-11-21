from reconhecimento_audio import *
from reconhecimento_video import *
from reproducao_audio import *
from enum import Enum

class Estado(Enum):
    ESPERA = 0
    LEITURA = 1
    AGUARDA_OBJETO = 2
    ORIENTACAO = 3
    OBJETO_ENCONTRADO = 4
    # _valor = None
    # def __init__(self):
    #     self.valor = Estado.EST_ESPERA
    #
    # def incrementa(self):
    #     self.valor += 1
    #
    # def volta_inicio(self):
    #     self.__init__()
    #

class Assistente:

    atual = None
    olhos = None

    def __init__(self):
        self.estado = Estado.ESPERA
        self.player = PlayerAudio()
        self.olhos = ReconhecedorObjetos()
        self.coordenadas_mao = None
        self.coordenadas_objetos = None
        #TODO: trabalhar nisso aqui
        self.objeto_em_mira = ObjetoAvistado()

    def procura_objetos(self):
        with self.olhos:
            self.coordenadas_mao, self.coordenadas_objetos = self.olhos.procurar_c_insistencia(30)

    def reproduz_fala(self, audio: str):
        self.player.play(audio)

    def avanca_estado(self):
        self.estado += 1

    def volta_para_estado_inicial(self):
        self.estado = Estado.ESPERA

    def direciona(self, objeto_em_mira: str):
        #TODO: fazer essa parte
        self.objeto_em_mira = objeto_em_mira

    def retorna_objetos_vistos(self) -> list:
        #TODO: retornar os objetos vistos em forma de lista de strings
        return []

    def aguarda_fala(self, palavras, limite: int=-1) -> str:
        contador = 0
        palavra_escutada = None
        while palavra_escutada is None:
            palavra_escutada = aguarda_audio(palavras)
            contador += 1
            if limite == contador:
                return None
        return palavra_escutada

    def encontrou_objetos(self) -> bool:
        if self.coordenadas_mao is None:
            return False
        if len(self.coordenadas_objetos) == 0:
            return False
        return True

    def fala_objetos_vistos(self):
        #TODO: fazer com a fala de fato
        if self.encontrou_objetos():
            print("Encontrei %3d objetos" % len(self.coordenadas_objetos))
        else:
            print("Nao encontrei objetos")


if __name__ == '__main__':
    HOT_WORD = "Maiara"

    mayara = Assistente()


    #TODO: para debug
    mayara.estado = Estado.LEITURA

    """ Primeiro estado onde a Assistente Virtual (AV) espera ser chamado pela "hot word". Quando acionado, 
    dira "bom dia"
    """
    if mayara.estado == Estado.ESPERA:
        if mayara.aguarda_fala(HOT_WORD) == HOT_WORD:
            mayara.reproduz_fala(Audio.BOM_DIA)
            mayara.avanca_estado()
    """ AV faz a leitura dos objetos a sua frente, e diz quais objetos ela viu."
    """
    if mayara.estado == Estado.LEITURA:
        mayara.procura_objetos()
        if mayara.encontrou_objetos():
            mayara.fala_objetos_vistos()
            mayara.avanca_estado()
    """ AV aguarda usuario dizer qual objeto esta procurando.
    """
    if mayara.estado == Estado.AGUARDA_OBJETO:
        objetos_vistos = mayara.retorna_objetos_vistos()
        objeto_em_mira = None
        while objeto_em_mira is None:
            mayara.reproduz_fala(Audio.QUAL_DESEJA)
            objeto_em_mira = mayara.aguarda_fala(objetos_vistos)
        mayara.avanca_estado()
    """ AV vai orientar a mao do usuario a sobrepor o objeto buscado.
    """
    if mayara.estado == Estado.ORIENTACAO:
        while not mayara.direciona(objeto_em_mira):
            pass
        mayara.avanca_estado()
    """ AV diz a mensagem de sucesso quando o objeto eh encontrado
    """
    if mayara.estado == Estado.OBJETO_ENCONTRADO:
        mayara.reproduz_fala(Audio.OBJETO_ENCONTRADO)
        mayara.volta_para_estado_inicial()
















