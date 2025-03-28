import sys
import os
import platform
import time
from colorama import Style,Fore
#from  construtor.gerador import __CONSTRUTOR_DE_PAYLOAD__



class Megador:
    def __init__(self):
        self.iniciar_loop = True
        self.TIPO_DO_SISTEMA_OPERACIONAL = platform.system()
        self.LISTA_DE_BIBLIOTECAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA = {
            'Linux':{
                'os':'pip3 install os', 
                'colorama':'pip3 install colorama',
                'time':'pip3 install time',
                'platform':'pip3 install platform',
                'pybluez':'pip3 install platform'
                },
            'Windows':{
                'os':'pip install os', 
                'colorama':'pip install colorama',
                'time':'pip install time',
                'platform':'pip install platform'
                }
            }
        self.Lista_De_comandos = {
            'Linux':{
                'clear':lambda: os.system("clear")
                },
            'Windows':{
                'clear':lambda: os.system("cls")
                }
            }
        
    def limpar_terminal(self):
        comando = self.Lista_De_comandos[self.TIPO_DO_SISTEMA_OPERACIONAL]
        comando['clear']()

    def CARREGAR_LOGO_MEGADOR(self):
        self.limpar_terminal()
        import logo
        print(self.texto(logo.logo1, Fore.CYAN))

    def texto(self, texto, cor):
        return f'{Style.BRIGHT}{cor}{texto}{Fore.RESET}'
    
    def P00_VERIFICAR_AS_BIBLIOTECAS_NECESSARIAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA(self):
        for biblioteca in self.LISTA_DE_BIBLIOTECAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA[self.TIPO_DO_SISTEMA_OPERACIONAL].keys():
            try:
                __import__(biblioteca)
            except ImportError:
                coletar_pip = self.LISTA_DE_BIBLIOTECAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA[self.TIPO_DO_SISTEMA_OPERACIONAL]
                comando_pip = coletar_pip[biblioteca]
                if biblioteca:
                    resposta_usuario = input(f"Biblioteca {biblioteca} pendente, deseja instalar agora ? (S ou N): ")
                    match resposta_usuario.lower():
                        case 's':
                            os.system(f'{comando_pip}')
                        case 'n':
                            self.iniciar_loop = False
                        case '':
                            self.iniciar_loop = False
                
                else:
                    pass

    
    def P01_SISTEMA_DE_REPETICAO_DO_MEGADOR(self):
        self.CARREGAR_LOGO_MEGADOR()
        while self.iniciar_loop == True:
            comando = input(self.texto('\n|Megador> ', cor=Fore.RED))

    
    def INICIAR_MEGADOR(self):
        self.P00_VERIFICAR_AS_BIBLIOTECAS_NECESSARIAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA()
        self.P01_SISTEMA_DE_REPETICAO_DO_MEGADOR()


if __name__=="__main__":
    mdr = Megador()
    mdr.INICIAR_MEGADOR()