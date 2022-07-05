#criptografartexto

##tela sem nada#
# import tkinter

# janela = tkinter.Tk()
# janela.title("NutryNotepad")
# janela.mainloop()
# ------------------------------
# ------------------------------
nomedoaquivo = input(str)
print(nomedoaquivo)

test_str = 'ONIBUS'
print('a palavra é : '+str(test_str))
res = ''.join(format(ord(i), 'b')for i in test_str)
print('convertido para binário : '+ str(res))

# nomedoaquivo = ('utf-8' b'nomedoarquivo'.encode)
# arqbinnome = input(int)
# print(arqbinnome)
#cria um arquivo txt e escreve nele uma vez
# def novotxt(): 
#     with open(nomedoaquivo, 'w+') as file: #escreve/cria o txt
#         file.write(input(str))#poe um cursor pra escrever um texto
#         file.seek(0) #depois de escrever o 'w+' para após o ultimo carácter escrito entao seek0 volta o cursor para o inicio
#         print(file.read()) #lê apartir de onde o cursor esteja
#novotxt()
#---------------------
#escrever mais sem sobrescever
# def addtotxt():
#     with open(nomedoaquivo, 'a+') as file: #escreve mais texto adicionando ao tetxto já existente
#         file.write(input(str))#poe um cursor pra escrever um texto
#         file.seek(0) #depois de escrever o 'a+' para após o ultimo carácter escrito entao seek0 volta o cursor para o inicio
#         print(file.read()) #lê apartir de onde o cursor esteja
#addtotxt()
# ###
# def bintxt(): 
#     with open(nomedoaquivo,'wb') as file: #escreve/cria o txt
#         file.write(input(bin))#poe um cursor pra escrever um texto
#         file.seek(0) #depois de escrever o 'w+' para após o ultimo carácter escrito entao seek0 volta o cursor para o inicio
#         print(file.read()) #lê apartir de onde o cursor esteja
# bintxt()
##lê o txt printa
# file = open(nomedoarquivo,'r')
# print(file.read())

##somente cria o arquivo
# file = open(nomedoarqivo,'x')
