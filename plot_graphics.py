import matplotlib.pyplot as plt
import numpy as np

def plota_grafico(list_avl, list_rb, list_heap, list_quick, list_selection, list_bubble, list_insertion, list_radix, list_shell, list_bucket, list_merge):
    plt.title('Gráfico de desempenho')
    plt.ylabel('Tempo')
    plt.xlabel('Iteração')
    plt.plot(list_avl, color='black')
    plt.plot(list_rb, color='green')
    plt.plot(list_heap, color='orange')
    plt.plot(list_selection, color='red')
    plt.plot(list_bubble, color='grey')
    plt.plot(list_insertion, color='purple')
    plt.plot(list_radix, color='pink')
    plt.plot(list_shell, color='yellow')
    plt.plot(list_bucket, color='brown')
    plt.plot(list_merge, color='silver')
    plt.plot(list_quick, color='blue')

    plt.show()
