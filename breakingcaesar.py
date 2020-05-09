#! python3
import operator
class Breaking():
    def __init__(self, mensagem):
        self.mensagem = mensagem.lower()
        self.alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    def frequency(self):
        self.m=''
        string_decod = ''
        lista_string_decod = []
        self.dicionario = {}
        for k in range(1,26):
            for i in self.mensagem:
                self.m = ''
                if i.isalpha():
                    i_index = self.alfabeto.index(i)
                    self.m += self.alfabeto[(i_index + k) %len(self.alfabeto)]#+ para adicionar o numero de casas e - para remover
                else:
                    self.m += i
                string_decod+=self.m
            lista_string_decod.append(string_decod)
            string_decod = ''
        for i in lista_string_decod:
            counting = i.count('a')  + i.count('e') + i.count('i') + i.count('o') + i.count('u')
            counting = int(counting)
            self.dicionario[i] = counting
        return max(self.dicionario.items(), key=operator.itemgetter(1))[0]
