'''
    CLASSE QUE IMPLEMENTA UM MENU COM QUANTOS ITEMS QUISER 
    DATA - 15/04/2021
    AUTOR - MARCELO ANTONIO NUNES DA SILVA
    EMAIL -   marcelo197519@gmail.com
    WHASTSAPP - (11)977634435 
'''
import keyboard
import winsound 
import os

class MenuSelect():
    index_aux = 0
    
    '''
    up - escolha uma tecla para selecionar os itens para cima
    down - escolha uma tecla para selecionar os itens para baixo
    sair - escolha uma tecla para, parar a leitura do teclado( sair do loop)
    args - items do menu separados por virgula ex -> 'item1','item2','item3'... assim por diante
    '''
    def __init__(self,up , down,sair,*args):
        self.__tecla1 = down
        self.__tecla2 = up
        self.__tecla3 = sair
        self.__lista  = str(args).replace("'",'').replace('(','').replace(')','')
        self.__index = 0
        self.__l1 = 0

    def beep(self):
        winsound.Beep(1100, 90)
    
    def listar_menus(self): # deve ser chamado no inicio apos instanciar a classe usando o objeto instanciado ex ->  menu.listar_menus
        os.system('cls')
        self.__l1 = str(self.__lista).split(',')
        for i in range(len(self.__l1)):
            if i == self.__index:
                print('\033[31m{:>0}\033[32m{:>6}\033[0m'.format('-> ',self.__l1[i]))
            if i != self.__index:
                ajust = 10-len(self.__l1[i])
                self.__l1[i]+=(' '* ajust)
                print('{:>10}'.format(self.__l1[i]))
                self.__index = self.__index
                
    
    def index(self): # retorna index atual ex -> index = menu.index()
        return MenuSelect.index_aux


    def down(self):
        os.system('cls')
        if self.__index != 0:
            self.__index -=1
            MenuSelect.index_aux = self.__index
        self.listar_menus()
        self.beep()


    def up(self):
        os.system('cls')
        if self.__index != len(self.__l1)-1:
            self.__index +=1
            MenuSelect.index_aux = self.__index
        self.listar_menus()
        self.beep()


    def espera(self): # é obrigatorio chamar ex -> menu.espera()
        keyboard.add_hotkey(self.__tecla1,self.up)
        keyboard.add_hotkey(self.__tecla2,self.down)
        try:
            keyboard.wait(self.__tecla3)
            self.beep()
        except:
            pass





