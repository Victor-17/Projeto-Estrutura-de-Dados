class Lista:
    def __init__(self,dado=None,proximo=None):
        self._dado=dado
        self._proximo=proximo
    def add(self,no,pos):
        p=self._dado
        q=self._dado
        no=No(no)
        while(p.get_proximo()!=pos):
            p=p.get_proximo()
            q=p.get_proximo()
        no.set_proximo(q)
        p.set_proximo(no)
        return no
    def remove(self,pos):
        p=self._dado
        q=self._dado
        while(p.get_proximo()!=pos):
            p=p.get_proximo()
            q=pos
        p.set_proximo(q.get_proximo())
    def isEmpty(self):
        if(self._dado==None):
            return True
        else:
            return False
    def size(self):
        p=self._dado
        cont=0
        while(p.get_proximo()!=None):
            cont+=1
            p-p.get_proximo()
        cont+=1
        return f'O tamanho da fila é de {cont} itens..'

