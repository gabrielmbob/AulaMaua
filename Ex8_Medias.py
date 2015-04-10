listanotas=[]
nota = 0
maior = 0

def media(lista):
    i = 0
    soma = 0
    for i in range (len(lista)):
        soma = soma + lista[i]
    if (len(lista)>0):
        media = soma/len(lista)
    else:
        print 'Voce nao digitou uma nota'
        media = 0
    return media
    

    
while (nota >= 0):
    while True:
        try:
            nota = int(raw_input('Digite a nota: '))
            if (maior < nota):
                maior = nota
            break
        except:
            print 'Voce nao digitou um numero valido'
    listanotas.append(nota)
print ('A media e: {0}'.format (media(listanotas[:-1])))
print ('A maior nota e: {0}'.format (maior))
