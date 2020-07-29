idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]

print(type(idades))

print(len(idades))

print(idades[0])

print(idades)

print(idades[1])
print(idades[2])
print(idades[3])

idades.append(15)

print(idades)

print(idades[4])

for idade in idades:
    print(idade)

idades.remove(30)

print(idades)

idades.append(15)

print(idades)

idades.remove(15)

print(idades)

idades.append(27)
idades.remove(27)
print(idades)

a = 28 in idades
print(a)
b = 15 in idades
print(b)

if 15 in idades:
    idades.remove(15)

print(idades)

if 28 in idades:
    idades.remove(28)

print(idades)

idades.append(19)
print(idades)

idades.insert(0, 20)
print(idades)

idades = [20, 39, 18]
print(idades)

idades.append([27, 19])

print(idades)

for elemento in idades:
    print("Recebi o elemento", elemento)

idades = [20, 39, 18]
idades.extend([27, 19])
print(idades)

for idade in idades:
    print(idade + 1)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)

idades_no_ano_que_vem = [idade+1 for idade in idades]
print(idades_no_ano_que_vem)

maior_21 = [idade for idade in idades if idade > 21]
print(maior_21)


def proximo_ano(idade):
    return idade + 1


[proximo_ano(idade) for idade in idades if idade > 21]


def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    lista.append(13)


idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)
print(idades)


def faz_processamento_de_visualizacao(lista=[]):
    print(len(lista))
    print(lista)
    lista.append(13)


faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()

faz_processamento_de_visualizacao()


'''Método com lista vazia como parâmetro padrão fará 
com que, a cada alteração, um novo objeto seja armazenado 
na memória, sem reset do parâmetro em uma nova referência
do método.'''


def faz_processamento_de_visualizacao(lista=list()):
    print(len(lista))
    print(lista)
    lista.append(13)


faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()


def faz_processamento_de_visualizacao(lista=None):
    if lista is None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()