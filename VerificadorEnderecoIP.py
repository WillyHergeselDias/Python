#Script simples que verifica se um endereco IP passado pelo usuario é valido ou nao, ainda está sendo trabalhado (WIP)

import re
#Variável que recebe o IP que o usuário inserir
IpAdress = input("Insira o endereco de IP: ")
#Utilizando split() para separar os octatos do endereco pelos pontos
AdressOctets = IpAdress.split(".")

#Definindo um padrao com range de 1 a 3 para cada octato para verificar se o IP inserido pelos usuario segue o formato correto
IpAdressPattern = r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"

#Verificando se cada octato nao ultrapassa o limite (0 até 255)
for Octet in AdressOctets:
    if int(Octet) < 0 or int(Octet) > 255:
        print("Excedencia do valor limite (0 a 255).")
        exit()
#Verificando se o endereco insirido pelo usuario segue o formato definido anteriormente e imprimindo se o IP é valido ou invalido
if(re.fullmatch(IpAdressPattern, IpAdress)):
    print(f'O endereco de IP {IpAdress} é valido!')
else:
    print(f"O endereco de IP {IpAdress} é invalido...")
