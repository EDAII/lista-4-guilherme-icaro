from algorithms.avltree import AvlTree, Node
from algorithms.rbtree import Tree, rb_insert, Node
from algorithms.heap_sort import heapsort
from algorithms.quick_sort import quick_sort
from algorithms.selection_sort import selection_sort
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.radix_sort import radix_sort
from algorithms.shell_sort import shell_sort
from algorithms.bucket_sort import bucket_sort
from algorithms.mergesort import merge_sort
from plot_graphics import plota_grafico
import time
import random

def main():
    print("Bem vindo ao programa de análise de algoritmos, nele, será feito um comparativo entre:")
    print("1. Algoritmos de ordenação O(n²)")
    print("2. Algoritmos de ordenação O(n*log(n))")
    print("3. Algoritmos de complexidade O(log(n)) - Ordenação com Árvores AVL e RB")

    print("Qual opção você deseja?")
    print("(1) - Analisar todos os algoritmos de ordenação")
    print("(2) - Analisar os algoritmos de árvore AVL com verificações e árvore Rubro-Negra")
    option = int(input("Digite uma das opções anteriores: "))

    if option == 1:
        print("Nele, será analisado 10 listas diferentes contendo 5.000 elementos.")
        print("Aguarde um momento que está sendo feito a análise...")

        list_avl = []
        list_rb = []
        list_heap = []
        list_quick = []
        list_selection = []
        list_bubble = []
        list_insertion = []
        list_radix = []
        list_shell = []
        list_bucket = []
        list_merge = []

        for i in range(0, 10):

            list = build_random_list(5000)

            list_avl.append(calcula_avl(list))
            list_rb.append(calcula_rb(list))
            list_heap.append(calcula_heap_sort(list))
            list_quick.append(calcula_quick_sort(list))
            list_selection.append(calcula_selection_sort(list))
            list_bubble.append(calcula_bubble_sort(list))
            list_insertion.append(calcula_insertion_sort(list))
            list_radix.append(calcula_radix_sort(list))
            list_shell.append(calcula_shell_sort(list))
            list_bucket.append(calcula_bucket_sort(list))
            list_merge.append(calcula_merge_sort(list))

        plota_grafico(list_avl, list_rb, list_heap, list_quick, list_selection, list_bubble, list_insertion, list_radix, list_shell, list_bucket, list_merge)

    elif option == 2:

        print("Nesta opção, será analisado de forma comparativa em uma lista de 100.000 elementos.")
        print("Por favor, aguarde o término...")

        list = build_random_list(100000)

        list_avl = list
        list_rb = list

        print("O tempo para ordenar uma lista com árvore avl foi de: {} segundos.".format(calcula_avl(list_avl)))
        print("O tempo para ordenar uma lista com árvore rubro-negra foi de: {} segundos.".format(calcula_rb(list_rb)))
    else:
        print("Opção inválida!")

def build_random_list(value):
    return random.sample(range(1000**2), value)

def calcula_avl(list):

    tempo = 0

    tree = AvlTree()

    for i in list:
        inicio = time.time()
        tree.insert(i)
        fim = time.time()
        tempo += (fim-inicio)

    return tempo

def calcula_rb(list):

    tempo = 0

    tree = Tree()

    for i in list:
        node = Node(i)
        inicio = time.time()
        rb_insert(tree, node)
        fim = time.time()
        tempo += (fim-inicio)

    return tempo

def calcula_heap_sort(list):
    inicio = time.time()

    heapsort(list)

    fim = time.time()

    return fim-inicio

def calcula_quick_sort(list):
    inicio = time.time()

    quick_sort(list, 0, len(list))

    fim = time.time()

    return fim-inicio

def calcula_selection_sort(list):
    inicio = time.time()

    selection_sort(list)

    fim = time.time()

    return fim-inicio

def calcula_bubble_sort(list):
    inicio = time.time()

    bubble_sort(list)

    fim = time.time()

    return fim-inicio

def calcula_insertion_sort(list):
    inicio = time.time()

    insertion_sort(list)

    fim = time.time()

    return fim-inicio

def calcula_radix_sort(list):
    inicio = time.time()

    radix_sort(list)

    fim = time.time()

    return fim-inicio

def calcula_shell_sort(list):
    inicio = time.time()

    shell_sort(list)

    fim = time.time()

    return fim-inicio

def calcula_bucket_sort(list):
    inicio = time.time()

    bucket_sort(list)

    fim = time.time()

    return fim-inicio

def calcula_merge_sort(list):
    inicio = time.time()

    merge_sort(list)

    fim = time.time()

    return fim-inicio

main()
