#estrutura de repeticão for para listas 
#lista: estrutura de dados composta (armazena vários valores)

#cria uma lista de nome
nomes =  ['Pietro', 'Ryan', 'Maria', 'Gabriela', 'Sophia']

#Imprime toda a lista (conjunto)
print(nomes)

#imprime um nome individualmente (Maria)
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])

#imprime todos os nomes utilizando for - range
for i in range(5):
    print(nomes[1])

# outra opção para interar(percorer de 1 em 1 ) sobre as listas
for nome in nomes:
    print(nome)