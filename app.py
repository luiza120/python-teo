import os

def mostra_titulo():
      print(""" 
            𝓔𝓼𝓽𝓾́𝓭𝓲𝓸 𝓕𝓸𝓽𝓸́𝓰𝓻𝓪𝓯𝓲𝓬𝓸 𝓛𝓩 
            """);

def mostra_escolhas():
      print('1. Cadastrar Fotógrafos')
      print('2. Listar Clientes')
      print('3. Ativar Agenda')
      print('4. Sair')

def escolhe_opcao():

      def finalizar_programa():
            os.system('cls')
            print('finalizando o programa\n')

      def opcao_invalida():
            print('Esse carácter não é permitido\n')
            input('Aperte qualquer tecla para voltar')
            main()

      try:
            opcao_escolhida = int(input("Escolha uma opção: "))

            if opcao_escolhida == 1:
                  print('Você escolheu Cadastrar Fotógrafos')
            elif opcao_escolhida == 2:
                  print('Você escolheu Listar Clientes')
            elif opcao_escolhida == 3:
                  print('Você escolheu Ativar Agenda')
            elif opcao_escolhida == 4:
                  finalizar_programa()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main ():
      mostra_titulo()
      mostra_escolhas()
      escolhe_opcao()

if __name__ == '__main__':
            main()







