import random

forca = ['cabide', 'roupas', 'aviao', 'homem', 'pessoa']
a = random.randint(0, 4)

forca = forca[a]
texto_forca = '_' * len(forca)

acertou = False

tentativa = 0

print(f'Palavra: {texto_forca}')

while acertou is False:  # Enquanto o utilizador não acertou a palavra
    tentativa += 1  # Número de tentativas tem o incremento em 1
    
    letra = input("\nDigite uma letra ou a palavra, se deseja sair, digite 'sair': ")  # Variável letra recebe a letra, ou palavra informada pelo utilizador
    if len(letra) > 1 and letra == forca:  # Se o tamanho do vetor letra for maior que 1, e a palavra informada igualar a sorteada
        print(f'\nVocê acertou a palavra, era {forca}!')
        print(f'Você acertou com {tentativa} tentativa(s)!')
        acertou = True
        break

    while len(letra) > 1:  # Se o tamanho da letra for maior que 1
        tentativa += 1
        if letra == 'sair':  # Se a palavra digitada for 'sair' encerra o programa.
            acertou = True
            break

        print('\nVocê errou a palavra, tente novamente')
        letra = input("Digite uma letra ou a palavra, se deseja sair, digite 'sair': ")

    if not letra == 'sair':  # Se a letra digitada não for 'sair'
        print(f'\nLetra digitada: {letra}')
        if letra not in forca:  # Se a letra não estiver na palavra sorteada
            print(f"A letra {letra} não está na palavra.")

        for i in range(len(forca)):
            if forca[i] == letra:  # Se a letra estiver no índice da forca
                # Será adicionado os espaços em brancos até o índice, adiciona a letra, e completa após a letra com os espaços em branco
                texto_forca = texto_forca[:i] + letra + texto_forca[i+1:]  
                print(texto_forca)

        if texto_forca == forca:  # Se todas as letras do forem acertadas sem a palavra inteira for digitada
            print(f'Você acertou a palavra, era {forca}!')
            print(f'Você acertou com {tentativa} tentativa(s)!')
            acertou = True
            
