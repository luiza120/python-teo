import os

fotografos = [{'nome':'Luana Jazmin', 'categoria': 'moda', 'ativo':True},
              {'nome':'Taylor Swift', 'categoria': 'social', 'ativo':True},
              {'nome':'Igor Pires', 'categoria': 'retratista', 'ativo':False}]

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

      def exibir_subtitulo(texto):
            os.system('cls')
            print(texto)
            print('')

      def retorna_menu():
            input(' Digite uma tecla para voltar ao menu principal')
            main()


      def cadastra_fotografo():
            exibir_subtitulo('Cadastrar fotografo')

            nome_fotografo = input('Digite o nome do(a) fotógrafo que deseja cadastrar:')
            categoria_fotografo = input(f'Digite a categoria que o {nome_fotografo} vai atuar:')
            dados_df = {'nome': nome_fotografo, 'categoria': categoria_fotografo, 'ativo': True}
            fotografos.append(dados_df)
            print(f'O fotógrafo {nome_fotografo} foi cadastrado com sucesso\n')

            retorna_menu()

      def listar_clientes():
            exibir_subtitulo('Lista de clientes cadastrados')

            for fotografo in fotografos:
                  nome_fotografo = fotografo['nome']
                  categoria_fotografo = fotografo['categoria']
                  ativo = fotografo['ativo']
                  print(f' - {nome_fotografo} | {categoria_fotografo} | {ativo}')
            retorna_menu()

      def finalizar_programa():
            os.system('cls')
            print('Finalizando o programa\n')

      def opcao_invalida():
            print('Esse carácter não é permitido\n')
            input('Aperte qualquer tecla para voltar')
            main()

      try:
            opcao_escolhida = int(input("Escolha uma opção: "))

            if opcao_escolhida == 1:
                  cadastra_fotografo()
            elif opcao_escolhida == 2:
                  listar_clientes()
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







