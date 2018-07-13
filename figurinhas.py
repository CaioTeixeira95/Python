"""Album de figurinhas da copa."""
from random import randint


class Album:
    u"""Classe que é o album da copa."""

    def __init__(self):
        u"""Cria-se a lista de figurinhas no album."""
        self.figurinhas = []
        self.repetidas = []

    def verificaAlbum(self, fig, r=''):
        u"""Essa função verifica se a figurinha já existe no album."""
        if r == 'repetidas':
            return self.repetidas.count(fig) == 0
        return self.figurinhas.count(fig) == 0
        # Se for igula a 0 não tem no album/repetidas (True)

    def qtdFigurinhas(self):
        u"""Essa função verifica se o album está completo."""
        if len(self.repetidas) < 782:
            return True
        else:
            print("Você completou o seu album. Parabéns!")
            self.parar()
            return False

    def abrirPacote(self):
        u"""Essa função gera 5 figurinhas aleatórias."""
        if self.qtdFigurinhas():
            fig = 0
            a = 0
            r = 0
            for x in range(0, 5):
                fig = randint(1, 782)
                if self.verificaAlbum(fig):
                    self.figurinhas.append(str(fig))
                    self.figurinhas = sorted(self.figurinhas, key=int)
                    a += 1
                else:
                    self.repetidas.append(str(fig))
                    self.repetidas = sorted(self.repetidas, key=int)
                    r += 1

            if a > 0:
                print("Foram adicionadas {} figurinhas no seu album. Parabéns!".format(a)) # NOQA

            if r > 0:
                print("{} figurinhas são repetidas. Tente trocá-las!".format(r)) # NOQA
        self.parar()

    def colarAvulsa(self, fig):
        u"""Essa função cola uma figurinha avulsa."""
        if self.qtdFigurinhas():
            if self.verificaAlbum(fig) is True:
                self.figurinhas.append(str(fig))
                self.figurinhas = sorted(self.figurinhas, key=int)
                print("Figurinha colada no album com sucesso. Parabéns!")
            else:
                self.repetidas.append(fig)
                self.repetidas = sorted(self.repetidas, key=int)
                print("Figurinha colocada na pilha de repetidas. Tente trocá-la!") # NOQA
        self.parar()

    def troca(self, figT, figR):
        u"""Essa função troca uma figurinha."""
        if self.qtdFigurinhas():
            if self.verificaAlbum(figT) is True and self.verificaAlbum(figR) is False: # NOQA
                self.figurinhas.append(str(figT))  # Adicionando figurinha ao album # NOQA
                self.repetidas.remove(str(figR))  # Removendo figurinha das repetidas # NOQA
                self.figurinhas = sorted(self.figurinhas, key=int)
                self.repetidas = sorted(self.repetidas, key=int)
                print("Troca realizada com sucesso.")
            elif self.verificaAlbum(figR, 1) is True:
                print("Figurinha não encontrada na pilha de repetidas.")
            elif self.verificaAlbum(figT) is False:
                print("Você já possui essa figurinha da troca no seu album.")
        self.parar()

    def imprimir(self, rel):
        u"""If rel == 0 ? imprime album : imprime repetidas."""
        if len(self.figurinhas) == 0 or (len(self.repetidas) == 0 and rel != 0): # NOQA
            print("Não há figurinhas para serem mostradas.")
        else:
            if rel == 0:
                print("Album: " + ', '.join(self.figurinhas))
            else:
                print("Repetidas:" + ', '.join(self.repetidas))
        self.parar()

    def imprimirFaltantes(self):
        u"""Essa função imprime as figurinhas que faltam."""
        i = []
        for x in range(1, 782):
            if self.verificaAlbum(x) is True:
                i.append(str(x))
        print(', '.join(i))
        self.parar()

    def parar(self):
        u"""Essa função serve para parar ao chamar uma função."""
        input("\nAperte ENTER para continuar...\n")


album = Album()
c = True
while(c): # NOQA

    print("\n\n*** Album da Copa do Mundo da Russia de 2018 ***\n")
    print("1 - Novo pacote de figurinha")
    print("2 - Colar figurinha avulsa")
    print("3 - Trocar figurinha")
    print("4 - Mostrar Album")
    print("5 - Figurinhas repetidas")
    print("6 - Figurinhas que faltam")
    print("7 - Buscar figurinha no album")
    print("8 - Buscar figurinha nas repetidas")
    print("9 - Sair\n")

    print("10 - Salvar progresso")
    print("11 - Carregar progresso\n")

    try:
        op = int(input("Digite o opção desejada: "))
    except Exception as e:
        print("Digite uma opção válida!")
        op = 0
        album.parar()

    if op == 1:
        album.abrirPacote()

    elif op == 2:
        fig = input("Digite a figurinha que deseja colar: ")
        album.colarAvulsa(fig)

    elif op == 3:
        figT = input("Digite a figurinha que você está recebendo: ")
        figR = input("Digite a figurinha que você está dando na troca: ")
        album.troca(figT, figR)

    elif op == 4:
        album.imprimir(0)

    elif op == 5:
        album.imprimir(1)

    elif op == 6:
        album.imprimirFaltantes()

    elif op == 7:
        fig = input("Digite a figurinha que deseja buscar no album: ")
        if album.verificaAlbum(fig) is False:
            print("Figurinha encontrada no album.")
        else:
            print("Figurinha não encontrada.")

        album.parar()

    elif op == 8:
        fig = input("Digite a figurinha que deseja buscar nas repetidas: ")
        if album.verificaAlbum(fig, 'repetidas') is False:
            print("Figurinha encontrada nas repetidas.")
        else:
            print("Figurinha não encontrada")

        album.parar()

    elif op == 9:
        c = False

    elif op == 10:
        tamA = len(album.figurinhas)
        tamR = len(album.repetidas)
        if tamA > 0:
            arquivo = open('album.txt', 'w')
            for x in range(0, tamA):
                arquivo.write(album.figurinhas[x] + '\n')
            arquivo.close()
            if tamR > 0:
                arquivo = open('repetidas.txt', 'w')
                for x in range(0, tamR):
                    arquivo.write(album.repetidas[x] + '\n')
                arquivo.close()
            print("Progresso salvo com sucesso.")

        else:
            print("Não há progresso para ser salvo.")

        album.parar()

    elif op == 11:
        try:
            arquivo = open('album.txt', 'r')
            for linha in arquivo:
                linha = linha.replace('\n', '')
                album.figurinhas.append(linha)
            album.figurinhas = sorted(album.figurinhas, key=int)
            arquivo.close()
            print("Album carregado com sucesso!")
        except Exception as e:
            print("Arquivos de progresso não encontrados.")

        try:
            arquivo = open('repetidas.txt', 'r')
            for linha in arquivo:
                linha = linha.replace('\n', '')
                album.repetidas.append(linha)
            album.repetidas = sorted(album.repetidas, key=int)
            arquivo.close()
            print("Figurinhas repetidas carregadas com sucesso!")
        except Exception as e:
            print("Não há figurinhas repetidas para serem carregadas.")

        album.parar()

    elif op > 11 and op != 0:
        print("Valor inválido!")
        album.parar()
