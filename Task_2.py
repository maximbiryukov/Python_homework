# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter
from operator import itemgetter

class Huffnode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def node_factory(a, b): # возвращает кустик из 3 элементов
    output = Huffnode(a[1]+b[1])
    if type(a[0]) == str:
        output.left = Huffnode(a[0])
    else:
        output.left = a[0]
    if type(b[0]) == str:
        output.right = Huffnode(b[0])
    else:
        output.right = b[0]
    return output

def node_placer(content_list, node): # вставляет ноду и сортирует content_list
    content_list.insert(0,(node, node.value))
    content_list.sort(key=itemgetter(1))

def tree_grower(content_list): # строит дерево
    branch_1 = []
    branch_2 = []
    while len(content_list) > 1:
        branch_1 = content_list[0]
        branch_2 = content_list[1]
        content_list.remove(content_list[0])
        content_list.remove(content_list[0])
        node_placer(content_list, node_factory(branch_1, branch_2))

def coder(node, code='', output = {}): # возвращает словарь с кодами всех элементов
    if node.left == None and node.right == None and type(node.value) == str:
        output[node.value] = code
    else:
        coder(node.left, code + "0");
        coder(node.right, code + "1");
    return output

def huffifier(string): # печатает словарь с кодами элементов и код строки string
    char_dict = Counter(S)
    content_list = sorted(char_dict.items(), key=lambda k: k[1])

    print('Исходная строка:')
    print(S)
    print('')

    tree_grower(content_list)

    code_dict = coder(content_list[0][0])
    print("Таблица кодов:")
    print(code_dict)
    print('')

    output = ''
    for char in S:
        output += code_dict[char]
        output += ' '

    print("Закодированная строка:")
    print(output)

S = "beep boop beer!"

huffifier(S)