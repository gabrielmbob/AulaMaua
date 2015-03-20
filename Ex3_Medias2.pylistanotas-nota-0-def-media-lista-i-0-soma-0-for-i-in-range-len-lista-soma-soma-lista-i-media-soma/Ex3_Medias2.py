listanotas=[]
nota = 0

def media(lista):
    i = 0
    soma = 0
    for i in range (len(lista)):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media
    

while (nota >= 0):
    nota = int(raw_input('Digite a nota: '))
    listanotas.append(nota)
print ('A media e: {0}'.format (media(listanotas[:-1])))
