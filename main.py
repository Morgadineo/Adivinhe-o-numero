from random import randint # Biblioteca Python para gerar valores aleatórios

numero_maximo = int(input('Ola! Escolha o número maximo a ser escolhido: ')) # Input, transformado em número inteiro, para limitar o número máximo que pode ser escolhido

numero_escolhido = randint(1, numero_maximo) # O número secreto que deve ser encontrado
tentativas = 0 # Variável das tentativas

print('De seu primeiro chute!')
chute = 0 # Variável de suporte

while chute != numero_escolhido: # Looping do jogo
	chute = int(input()) # Input do chute
	if chute > numero_escolhido: # Se o chute for maior que o numero_escolhido faça:
		print('Muito alto!\n------------------')
		tentativas += 1 # +1 tentiva
	elif chute < numero_escolhido: # E se o chute for menor que o numero_escolhido faça:
		print('Muito baixo!\n-----------------')
		tentativas += 1 # +1 tentativa
	elif chute == numero_escolhido: # E se o chute for igual ao numero escolhido faça:
		print(f'Você acertou com {tentativas} tentativas! O número era {numero_escolhido}') # Printa a mensagem final!
