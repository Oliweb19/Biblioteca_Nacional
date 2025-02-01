from libros import *
from extras import *


def Biblioteca():
    op = 6
    while(op == 6):
        op = menu()
        if(op == 1):
            biblioteca = agg_libro()
            print(biblioteca)

Biblioteca()