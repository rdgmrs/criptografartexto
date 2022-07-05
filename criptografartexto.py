#criptografartexto

##tela sem nada#
# import tkinter

# janela = tkinter.Tk()
# janela.title("NutryNotepad")
# janela.mainloop() 
# ------------------------------
# ------------------------------
# nomedoaquivo = input(str)
# print(nomedoaquivo)

#### de srt pra binario####
# test_str = "GeeksforGeeks"
# print("The original string is : " + str(test_str)) 
# res = ''.join(format(i, 'b') for i in bytearray(test_str, encoding ='utf-8')) 
# print("The string after binary conversion : " + str(res)) 

####de bin pra srt#####
# def BinaryToDecimal(binary):  
         
#     binary1 = binary  
#     decimal, i, n = 0, 0, 0
#     while(binary != 0):  
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)  
#         binary = binary//10
#         i += 1
#     return (decimal)     
# bin_data ='10001111100101110010111010111110011'
   
# print("The binary value is:", bin_data) 
   
# str_data =' '
   
# for i in range(0, len(bin_data), 7): 
      
    
    
#     temp_data = int(bin_data[i:i + 7]) 
       
    
    
#     decimal_data = BinaryToDecimal(temp_data) 
       
    
    
    
    
    
#     str_data = str_data + chr(decimal_data)  
   
# print("The Binary value after string conversion is:",  
#        str_data)




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
