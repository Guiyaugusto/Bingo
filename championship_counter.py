numero_de_times =  int(input("Digite o numero de times participantes: "))
numero_de_partidas = numero_de_times*(numero_de_times-1)
print("Digite os resultados de cada partida assim como o exemplo: \nPonte Preta 3 x Guarani 1 \nObs: Os times devem se enfrentar dentro e fora de casa! ")
dic_times = {}
vencedor = []

for i in range (numero_de_partidas): 
	saldo_gols= 0
	gols_pro = 0
	linha_entrada = input()
	dados_partida = linha_entrada.split()
	if dados_partida[0] not in dic_times: #adiciona os times na lista_times
		dic_times[dados_partida[0]] = [0,0,0,0]
	if dados_partida[3] not in dic_times:
		dic_times[dados_partida[3]] = [0,0,0,0]
	
	if int(dados_partida[1])>int(dados_partida[4]):
		dic_times[dados_partida[0]][0] +=3 #soma 3 pontos a cada vitoria
		dic_times[dados_partida[0]][1] +=1 #soma 1 ao numero de vitorias
		saldo_gols = int(dados_partida[1])-int(dados_partida[4])#soma e subtrai o saldo de gols
		dic_times[dados_partida[0]][2] += saldo_gols
		dic_times[dados_partida[3]][2] -= saldo_gols
		
	elif int(dados_partida[1])<int(dados_partida[4]):
		dic_times[dados_partida[3]][0] +=3
		dic_times[dados_partida[3]][1] +=1
		saldo_gols = int(dados_partida[4])-int(dados_partida[1])
		dic_times[dados_partida[3]][2] += saldo_gols
		dic_times[dados_partida[0]][2] -= saldo_gols
	else:
		dic_times[dados_partida[0]][0] += 1 
		dic_times[dados_partida[3]][0] += 1 
		#nao e necessario ter calculo do saldo de gols
	dic_times[dados_partida[0]][3] += int(dados_partida[1])
	dic_times[dados_partida[3]][3] += int(dados_partida[4])	
	

for t in sorted(dic_times):
	print(t, dic_times[t][0], dic_times[t][1], dic_times[t][2], dic_times[t][3])
	valor = int(dic_times[t][0])*1000 + int(dic_times[t][1])*100 + int(dic_times[t][2])*10 + int(dic_times[t][3])*1
	vencedor.append(valor)
posicao=int(vencedor.index(max(vencedor)))
ordem_times = sorted(dic_times)
print("Vencedor:", ordem_times[posicao])

