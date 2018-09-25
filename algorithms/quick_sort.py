def quick_sort(list_elements, ponteiro_inicio, ponteiro_fim):
    inicio = ponteiro_inicio
    fim = ponteiro_fim-1
    pivo = int((ponteiro_inicio+ponteiro_fim)/2)

    while inicio <= fim:
        while list_elements[inicio] < list_elements[pivo]:
            inicio += 1

        while list_elements[fim] > list_elements[pivo]:
            fim -= 1

        if inicio <= fim:
            temporario = list_elements[inicio]
            list_elements[inicio] = list_elements[fim]
            list_elements[fim] = temporario
            # print('Trocou {} por {}'.format(list_elements[inicio], list_elements[fim]))
            inicio+=1
            fim-=1

        # print('Ponteiro pro inicio -> {}'.format(inicio))
        # print('Ponteiro pro fim -> {}'.format(fim))

    # Trabalha na sublista da esquerda
    if fim > ponteiro_inicio:
        quick_sort(list_elements, ponteiro_inicio, fim+1)

    # Trabalha na sublista da direita
    if inicio < ponteiro_fim:
        quick_sort(list_elements, inicio, ponteiro_fim)

def print_list(list_elements):
    print(list_elements)
