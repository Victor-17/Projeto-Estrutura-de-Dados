class Fila:
    def __init__(self, head=None):
        self._head = head
    def isEmpty(self):
        return self._head == None
    def remove(self):
        p = self._head
        self._head = self._head.get_proximo()
        return p.get_dado()
    def add (self, no):
        p = self._head
        while(p.get_proximo != None):
            p = p.get_proximo()
        p.set_proximo(no)
        return p
    def size(self):
        p = self._head
        cont = 0
        while(p.get_proximo() != None):
            cont += 1
            p = p.get_proximo()
        cont += 1
        return f'O tamanho da fila é de {cont} itens..'