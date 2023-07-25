a=input("Digite algo: ")
print("O tipo primitivo deste valor é ",type(a)) # semopre irá apontar para str,pois não teve o tipo primitivo informado.
print("Só tem espaços? " ,a.isspace()) # se possui espaços o que foi digitado pelo usuário.
print("É um numero? ",a.isnumeric()) # é um numero?
print("É alfabetico? ",a.isalpha()) # está em ordem alfabética?
print("É alfanumérico? ",a.isalnum()) # é alfanumérico?
print("Está em maiusculas? " , a.isupper()) #está em maiusculas?
print(("Está em minusculas? ",a.islower())) # está em minuscula?



