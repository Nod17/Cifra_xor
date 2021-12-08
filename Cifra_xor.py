import os

tam = 0
cont = 0
#solicitação de informações ao usuário
nome_arq = input("Digite o nome do arquivo e sua extensão: \n")
palavra = input("\nDigite a palavra cifra: \n")

tam = len(palavra)

try:
  #Leitura do arquivo
  arquivo = open(nome_arq, 'r')

  novo_nome = nome_arq.split('.')[0]+'.enc'
  resultado = open(novo_nome, 'w')
  dado = arquivo.read(1)

  while True:
   
    if dado == '':
      break
    
    if cont == tam:
      cont = 0
    
    xor = ord(dado) ^ ord(palavra[cont])
    contador =  cont + 1
   #Escreve o arquivo cifrado 
    resultado.write(chr(xor))
    dado = arquivo.read(1)
 
  arquivo.close()
  resultado.close()
#Remove o arquivo antigo
  os.remove(nome_arq)
except:
  print('Não foi possível abrir esse arquivo.')
