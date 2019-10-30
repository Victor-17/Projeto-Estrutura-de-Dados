class No:
    def __init__(self,dado=None,proximo=None):
        self._dado=dado
        self._proximo=proximo
    def get_dado(self):
        return self._dado
    def set_dado(self,novoDado):
        self._dado=novoDado
    def get_proximo(self):
        return self._proximo
    def set_proximo(self,outro):
        self._proximo=outro
    def __str__(self):
        return "{}".format(self._dado)
class Pilha:
    def __init__(self,head=None):
        self._head=head
    def isEmpty(self):
        if self._head == None:
            return True
        else:
            return False
    def push(self,item):
        p=self._head
        q=No(item)
        q.set_proximo(p)
        q=self._head
    def remove(self):
        p=self._head
        q=self._head
        q.set_proximo(self._head)
        p.set_proximo(None)
    def size(self):
        topo=self._head
        cont=0
        while(topo.get_proximo()!=None):
            cont+=1
            topo=topo.get_proximo()
        return cont