import sys

class PrefixTreeNode:
    def __init__(self):
        self.children = dict()
        self.end_node = False


class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    #  Сложность по памяти - O(len(word)), т.к потенциально для каждого символа может создаваться новое звено
    #
    #  Сложность по времени - O(len(word)), т.к происходит полный проход по слову
    def add(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTreeNode()
            node = node.children[c]
        
        node.end_node = True

    #  Сложность по памяти - O(1)
    #
    #  Сложность по времени - O(len(word)), т.к происходит полный проход по слову
    def contain(self, word, node=None):
        if node is None:
            node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
      
        return node.end_node

    #  Сложность по памяти O(len(word)), т.к. нужно сформировать несколько новых строк (C) длины 
    #  len(word), а (O(C*len(word)) = O(len(word)))
    #
    #  Сложность по времени O(len(word)), т.к. после одной из операций нужно проверить есть ли 
    #  измененный остаток в дереве (всего операций: С = 3 * [кол-во детей] + 1), где С - константа
    def get_available_words_(self, node, word, pos, words, check):
        l_word = word[:pos]
        r_word = word[pos + 1:]
        ch = word[pos] if pos < len(word) else ''

        word_remove = f'{l_word}{r_word}'
        if word_remove not in check:
            if self.contain(r_word, node):
                words.append(word_remove)
            check.add(word_remove)
        
        for child in node.children:
            word_replcace = f'{l_word}{child}{r_word}'
            if word_replcace not in check:
                if self.contain(f'{child}{r_word}', node):
                    words.append(word_replcace)
                check.add(word_replcace)
            
            word_insert = f'{l_word}{child}{ch}{r_word}'
            if word_insert not in check:
                if self.contain(f'{child}{ch}{r_word}', node):
                    words.append(word_insert)
                check.add(word_insert)
            
            if pos + 1 < len(word) and child == r_word[0]:
                word_swap = f'{l_word}{child}{ch}{r_word[1:]}'
                if word_swap not in check:
                    if self.contain(f'{child}{ch}{r_word[1:]}', node):
                        words.append(word_swap)
                    check.add(word_swap)

    #  Cложность по памяти O(len(word) ^ 3)
    #  На каждый символ создаём С слов длины len(word),
    #  1-й символ: С1 * len(word), 2-й символ: С2 * len(word), ..., N-й: Cn * len(word)
    #  Сумма (Сi*len(word)), i = 1..len(word) <= Сумма(С) * len(word), i = 1..len(word) =
    #  = C * len(word)^2 => всего С * len(word)^3
    #  C - максимальное число детей у вершины
    #  
    #  Сложность по времени O(len(word) ^ 3)
    #  Нужно пройти по слову (len(word))
    #  для каждого символа произвести одну из 4-х операций:
    #       удаление O(1)
    #       вставка/замена/удаление: O(C) = O(1) (С максимальное число детей у вершины)
    #  и проверить есть ли оно в дереве: O(len(word)) в среднем
    #  O(len(word) * [Сумма(С), i = 1..len(word)] * len(word)) = O(len(word) ^ 3) 
    def get_available_words(self, word):
        words = list()
        check = set()
        node = self.root

        for i in range(len(word) + 1):
            self.get_available_words_(node, word, i, words, check)
            if i != len(word) and word[i] in node.children:
                node = node.children[word[i]]
            else:
                break
        
        return sorted(words)

def main():
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    n = int(input())

    tree = PrefixTree()

    for i in range(n):
        word = input().lower()
        tree.add(word)

    was_printed = False

    for word in sys.stdin:
        word = word.strip('\n')

        if not word:
            continue

        if was_printed:
            print('')
        else:
            was_printed = True

        if tree.contain(word.lower()):
            print('{0} - ok'.format(word), end = '')
        else:
            words = tree.get_available_words(word.lower())

            if words:
                print('{0} -> {1}'.format(word, ', '.join(words)), end = '')
            else:
                print('{0} -?'.format(word), end = '')
    print()

main()
