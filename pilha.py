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
        dado=Dado(item)
        q=No(dado)
        q.set_proximo(p)
        q=self._head
    def remove(self):
        p=self._head
        topo=self._head
        topo.set_proximo(self._head)
        p.set_proximo(None)
    def size(self):
        topo=self._head
        cont=0
        while(topo.get_proximo()!=None):
            cont+=1
            topo=topo.get_proximo()
        return cont