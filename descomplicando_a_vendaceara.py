

while True:
    #Criando verificador de escolha
    opcoes = (1,2,3)
    git 
    print('Descomplicando a venda')
    print(' Opções: (1)laje (2)tijolo (3)piso/revestimento')

    escolha = int(input('Digite a opção: '))
    
    #Calculo dos tijolos 
    if escolha == 2:
        print(' Tijolos (1) 9x19x19 (2) 11,5x14x24  (3) 14x19x29 ')
        definicao = int(input('Digite: '))

        #tijolo 9x19x19 
        if definicao == 1:
            metragem = float(input('Digite a metragem em [M2]: '))
            quantidade = metragem * 25
            print(f'Total de tijolo 9x19x19 = {quantidade:.2f}pçs (obs: Espessura da massa de 10mm) ')
       
        #tijolo  11,5x14x24
        elif definicao == 2:
            metragem = float(input('Digite a metragem em [M2]: '))
            quantidade = metragem * 27.5
            print(f'Total de tijolo 11,5x14x24 = {quantidade:.2f}pçs (obs: Espessura da massa de 10mm)')
       
        #tijolo 14x19x29
        elif definicao == 3:
            metragem = float(input('Digite a metragem em [M2]: '))
            quantidade = metragem * 17
            print(f'Total de tijolo 14x19x29 = {quantidade:.2f}pçs (obs: Espessura da massa de 10mm)')
    

    #Calculo da laje    
    if escolha == 1:

        print('laje por área total(t) laje por vigas (v) laje por medidas(m)')
        print()
        escolha2 = str(input('selecione a opção: ')).lower().strip()
        
        verificador_opções = 't','v','m'
        if escolha2 not in verificador_opções:
            print('opção invalida')

        


        if escolha2 == 'm':
    
            comprimento = float(input('Digite o comprimento: '))
            largura = float(input('Digite a largura: '))
            vigas = float(input('Tamanho da viga: '))
            total_m2 = comprimento * largura
            total_vigas = (total_m2 / vigas) / 0.42
            placa_eps = (total_m2 / 0.42 ) 
            lajota = (total_m2 * 11)
            print(f'laje= {total_m2}mt2   vigas{vigas}mt  total de vigas= {total_vigas:.2f}un  placa eps= {placa_eps:.2f} ou {lajota:.2f} lajotas ')
        
        elif escolha2 == 'v':

            tamanho_vigas = float(input('Digite o comprimentos das vigas: '))
            quantidade_vigas = int(input('Digite a quantidade de vigas: '))
            metragemQuadrada = (tamanho_vigas * quantidade_vigas) * 0.42
            placa_eps = metragemQuadrada / 0.42
            lajota = metragemQuadrada * 11
           
            quantidadeLaje = metragemQuadrada
            print(f'total laje = {quantidadeLaje:.2f}mt2  total vigas ={quantidade_vigas:.0f}un tamanho das vigas {tamanho_vigas:.2f}mt  placa eps{placa_eps:.2f} ou {lajota:.2f}lajotas ')
        
        elif escolha2== 't':

            lajeTotal = float(input('Digite total da laje: '))
            tamanho_vigas = float(input('Comprimento das vigas: '))
            totalVigas = lajeTotal / tamanho_vigas / 0.42
            placa_eps = lajeTotal / 0.42
            lajota = lajeTotal * 11

            print(f' laje total ={lajeTotal}mt2  Quantidade vigas = {totalVigas:.0f}un  vigas {tamanho_vigas}mt placa eps{placa_eps:.2f} ou {lajota:.2f}lajotas')
        
    
    
    #Calculo piso/revestimento quantidade na caixa
    if escolha == 3:
        largura = float(input('Digite a largura: '))
        comprimento = float(input('Digite o comprimento: '))
        quantidade_caixa = float(input('Digite a quantidade da caixa: '))
        quantidade_peças = quantidade_caixa / comprimento / largura
        print(f'Na caixa vem no total de {quantidade_peças:.2f}pçs')
    
    #Verificando se a escolha existe
    if escolha not in opcoes:
       print('Opção invalida!')
   
    
    #Criando break do loopin
    continuar = str(input('Quer continuar? [s/n]')).lower().strip()
    if continuar == 'n':
        print('Obrigdo por utilizar nossos serviços!')
        break


