from menu_select import *



menu1 = MenuSelect('up','down','enter','Cadastrar','Editar','Listar','Voltar','Deletar','sair','cafe')
menu1.listar_menus()

op = menu1.index()

menu1.espera()



print(op)












