# librerias
import os

# imprime la tabla del juego
def print_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# agrega una marca al tablero en la posicion pos
def add_mark(mark, values, pos):
    values[pos] = mark
    return values

# main loop del juego
def main():

    # estado inicial del juego
    values = ["_","_","_","_","_","_","_","_","_"]
    print_board(values)

    # un jugados por iteracion.
    for i in range(9):
        
        print("ingrese un simbolo:")
        mark = input()
        print("ingrese la posicion:")
        pos = int(input())
        values = add_mark(mark, values, pos)
        print("")
        clear = lambda: os.system('cls')
        clear()
        print_board(values)


main()