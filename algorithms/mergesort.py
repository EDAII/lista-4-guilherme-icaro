def merge_sort(list_elements):
    if(len(list_elements) > 1):
        meio = int(len(list_elements)/2)

        lista_esquerda = list_elements[:meio]
        lista_direita = list_elements[meio:]

        merge_sort(lista_esquerda)
        merge_sort(lista_direita)

        i, j, k = [0, 0, 0]

        while(i < len(lista_esquerda) and j < len(lista_direita)):
            if(lista_esquerda[i] < lista_direita[j]):
                list_elements[k] = lista_esquerda[i]
                i += 1
            else:
                list_elements[k] = lista_direita[j]
                j += 1

            k += 1

        while(i < len(lista_esquerda)):
            list_elements[k] = lista_esquerda[i]
            k += 1
            i += 1

        while(j < len(lista_direita)):
            list_elements[k] = lista_direita[j]
            j += 1
            k += 1

def print_list(list_elements):
    print(list_elements)
