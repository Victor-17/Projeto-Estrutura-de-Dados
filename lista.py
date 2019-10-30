class Lista:
    def __init__(self,head=None):
        self._head=head
    def add(self,no,valor_anterior):
        p=self._head
        q=self._head
        dado=Dado(no)
        no=No(dado)
        while(p.get_proximo()!=valor_anterior):
            p=p.get_proximo()
            q=p.get_proximo()
        no.set_proximo(q)
        p.set_proximo(no)
        return no
    def remove(self,pos):
        p=self._head
        q=self._head
        while(p.get_proximo()!=pos):
            p=p.get_proximo()
            q=pos
        p.set_proximo(q.get_proximo())
    def isEmpty(self):
        if(self._head==None):
            return True
        else:
            return False
    def size(self):
        p=self._head
        cont=0
        while(p.get_proximo()!=None):
            cont+=1
            p-p.get_proximo()
        cont+=1
        return f'O tamanho da fila é de {cont} itens..'
    def ordenar(self):
        p = self._head
        temp = 0
        cont = 0
        while(p.get_proximo() != None):
            cont += 1
            p = p.get_proximo()
        cont += 1
        print('A lista ordenada é:\n')
        while(temp < cont):
            while(p.get_proximo() != None):
                if(p.get_dado()._musica > p.get_proximo().get_dado()._musica):
                    aux = p.get_dado()._musica
                    p.get_dado()._musica = p.get_proximo().get_dado()._musica
                    p.get_proximo().get_dado()._musica = aux
                    if temp == cont-1:
                        print(p.get_dado()._musica)
                else:
                    if temp == cont-1:
                        print(p.get_dado()._musica)
                    p = p.get_proximo()
        if temp == cont-1:
            print(p.get_dado()._musica)
        p = self._head
        temp +=1
    def print(self):
        p=self._head
        while(p.get_proximo()!=None):
            print(p,"\n")
            p=p.get_proximo()

