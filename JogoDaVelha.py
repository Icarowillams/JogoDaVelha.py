class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'

    def exibir_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * 5)

    def verificar_vitoria(self):
        # Verificar linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return True

        # Verificar colunas
        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != ' ':
                return True

        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if ' ' in linha:
                return False
        return True

    def fazer_movimento(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.jogador_atual
            if self.verificar_vitoria():
                self.exibir_tabuleiro()
                print(f"Jogador {self.jogador_atual} venceu!")
                return True
            elif self.verificar_empate():
                self.exibir_tabuleiro()
                print("Empate!")
                return True
            self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
            return False
        else:
            print("Movimento inválido. Tente novamente.")
            return False

    def jogar(self):
        while True:
            self.exibir_tabuleiro()
            linha = int(input(f"Jogador {self.jogador_atual}, escolha a linha (0-2): "))
            coluna = int(input(f"Jogador {self.jogador_atual}, escolha a coluna (0-2): "))
            if self.fazer_movimento(linha, coluna):
                break

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
