class Pilha:
    def __init__(self,head=None):
        self._head=head
    def isEmpty(self):
        if self._head == None:
            return True
        else:
            return False
    def push(self,item):
        p = item
        p.set_proximo(self._head)
        self._head=p
    def remove(self):
        p = self._head
        self._head = p.get_proximo()
    def size(self):
        topo=self._head
        cont=0
        while(topo.get_proximo()!=None):
            cont+=1
            topo=topo.get_proximo()
        cont+=1
        return cont
    def printall(self):
        p = self._head
        print(p,"\n")
        while(p.get_proximo()!= None):
            p = p.get_proximo()
            print(p,"\n")