
#lista de nomes 
nomes = ['Giovana', 'mateus', 'Goão', 'emilly', 'julia', 'vitória']

for indice, nome in enumerate(nomes):
        print(f'estou no {indice} que possui o nome {nome}')
        if nome == 'Goão':
                nomes[indice] = 'joão'
                break
        
print(nomes)