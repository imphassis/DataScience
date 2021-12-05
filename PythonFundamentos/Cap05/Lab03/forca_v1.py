# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import re

# Board (tabuleiro)
from board import board


# Classe
class Hangman:
    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.correctLetters = []
        self.wrongLetters = []
        self.result = False
        self.hidden = list("_" * len(word))

    # Método para adivinhar a letra

    def guess(self):
        print(board[len(self.wrongLetters)])
        print(f"Letras erradas: {''.join(self.wrongLetters)}")
        print(f"Letras corretas: {''.join(self.correctLetters)}")
        print(f"\nPalavra: {''.join(self.hidden)}\n")
        letter = input("Digite a Letra: ")
        x = re.search(letter, self.word, re.IGNORECASE)
        self.correctLetters.append(letter) if x else self.wrongLetters.append(letter)
        self.hide_word()

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if "".join(self.hidden) == self.word:
            print(f"\nPalavra: {''.join(self.hidden)}\n")
            self.result = True
            return self.result
        
        # if len(self.wrongLetters) == len(board):
        #     print(f"\nPalavra: {''.join(self.hidden)}\n")
        #     self.result = False
        #     return self.result
            

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return self.result == True

    # Método para não mostrar a letra no board
    def hide_word(self):
        for i, char in enumerate(self.word):
            if char in self.word and char in self.correctLetters:
                self.hidden[i] = char
        return self.hangman_over()

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        while len(self.wrongLetters) < len(board) - 1 and self.result == False:
            print("LENGTH", len(self.wrongLetters), len(board))
            self.guess()
        print(board[len(self.wrongLetters)])
       


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print("\nParabéns! Você venceu!!")
    else:
        print("\nGame over! Você perdeu.")
        print("A palavra era " + game.word)

    print("\nFoi bom jogar com você! Agora vá estudar!\n")


# Executa o programa
if __name__ == "__main__":
    main()

