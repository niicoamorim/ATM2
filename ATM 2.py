contas = []
saldo = []
vlrdep = int()
vlrsaque = int()
vl = int()
vlp = int()
pos = int()
tentlogin = int(3)
ver = str('S')
verifconta = str()
voltarsaque = str('S')


print('=' * 30)
print('{:^30}'.format('NICOLAS BANK'))
print('=' * 30)


respcliente = str(input('Você já é nosso cliente do banco? S / N.'))

if respcliente == 'N':
    desejocad = str(input('Deseja cadastrar uma conta? S/N'))

    if desejocad == 'S':
       while desejocad == 'S':

         numconta = str(input('Digite o número da conta a ser cadastrada.'))

         if numconta in contas:
            print( 'Parece que você já tem uma conta.' )
            ver = str(input('deseja entra?'))
            if ver == 'S':
              desejocad = 'N'
              respcliente = 'S'

         else:
            contas.append(numconta)
            saldo.append(0)
            print(contas,saldo)
            desejocad = str( input( 'Desja cadastrar outra conta?' ) )
            if desejocad == 'N':
                    desejoent = str(input('Deseja entrar no sistema do banco?'))
                    if desejoent == 'S':
                        desejocad = 'N'
                        respcliente = 'S'
            else:
                desejocad = 'S'

    if desejocad == 'N':
           print('NICOLAS BANK lhe deseja sucesso.')


if respcliente == 'S':
        while verifconta not in contas or tentlogin == 0:
         verifconta = str( input( 'Digita sua conta. Você ainda possui {} dentativas'.format( tentlogin ) ) )
         print( 'Login efetuado com sucesso.' )
         while verifconta in contas and voltarsaque == 'S':

          print('Qual peração vc deseja  realizar?')
          operacao = int(input('Digite 1 para saldo, 2 para depósito, 3 para saque, 4 para transferencia ou 5 para sair:'))

          if operacao == 1:
           pos = contas.index(verifconta)
           print('Seu saldo é {}'.format( saldo[pos]))


          if operacao == 2:
              vlrdep = bool(input('Digite o valor a ser depositado:'))
              pos = contas.index(verifconta)
              print(pos)
              vl = saldo[pos]
              vlp = saldo[pos]+vlrdep
              print(vlp)
              saldo.insert(pos, vl+vlrdep)
              print('Seu saldo atual é : R$',saldo[pos])

          while operacao == 3:
            print('Você optou para opção de saque')
            vlrsaque = int(input('Quanto vc deseja sacar?'))
            pos = contas.index(verifconta)
            if vlrsaque <= 0:
                print('Valor de saque impossível.')
                voltarsaque = str(input('Deseja tentar novamente?'))
                if voltarsaque == 'S':
                 operacao = 3
                else:
                 break


            if vlrsaque > saldo[pos]:
                 print('Saldo insuficiente. Deseja tentar novamente?')

            if vlrsaque <= saldo[pos]:
                saldo[pos] = saldo[pos] - vlrsaque

                opnovosaque = str(input('Deseja realizar um novo saque? S/N.'))
                if opnovosaque == 'S':
                     operacao = 3
                else:
                  voltarsaque = 'S'
                  break


          if operacao == 4:
              contatransf = int(input('Digite a conta para transferir:'))
              vlrdep = int(input('Digite o valor a ser transferido:'))
              pos = contas.index(verifconta)
              pos2 = contas.index(contatransf)
              s1 = saldo[pos]
              s2 = saldo[pos2]
              if s1 < vlrdep:
                  print('Transferencia impossível:')
              else:
               for c in range(0, len(contas)):
                  if contatransf == c:
                   p1 = pos
                   p2 = pos2
                   saldo.insert(s1, s1-vlrdep)
                   saldo.insert(s2, s2+vlrdep)



         else:
             tentlogin -= 1
             if tentlogin == 0:
                 print('Erro ao logar. Tente novamente em 30 minutos.')
                 verifconta = ''
                 break



