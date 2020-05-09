import hashlib

class Czar():
    def __init__(self,mensagem,numero_casas):
        self.mensagem = mensagem
        self.alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        self.numero_casas = numero_casas
    def cript(self):
        self.m = ''
        for i in self.mensagem:
            if i.isalpha():
                i_index = self.alfabeto.index(i)
                self.m += self.alfabeto[(i_index + self.numero_casas) %len(self.alfabeto)]#+ para adicionar o numero de casas e - para remover
            else:
                self.m += i
    def sha1hash(self):
        self.hsh = hashlib.sha1()
        self.hsh.update(self.m.encode('utf-8'))
        self.hash_digested = self.hsh.hexdigest()
        print('Texto criptografado em {}: {}\nResumo Criptográfico: {}'.format(self.numero_casas,self.m,self.hash_digested))
