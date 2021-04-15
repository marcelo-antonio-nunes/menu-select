from menu_select import *

'''
Pequeno exemplo de utilização da classe, essas teclas escolhi so para exemplificar mas
vc pode escolher as que melhor atender, são tres teclas - direcional pra cima que escolhi 
por up mas poderia ser qualquer outra -1 2 A B... a que melhor atender e isso vale para - down
e sair que escolhi (enter)
'''

menu1 = MenuSelect('up','down','enter','Cadastrar','Editar','Listar','Voltar','Deletar','sair')
menu1.listar_menus()
menu1.espera()
index = menu1.index()

'''
Essa parte do programa so funcionara apos apertar o enter assim sairar 
do loop de espera de entrada do teclado, daqui pra baixo vc pode tratar 
seu programa como bem achar necessario!
'''
print(index)













