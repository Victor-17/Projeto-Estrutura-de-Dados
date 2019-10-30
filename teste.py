class Dado:
    def __init__(self,musica,cantor,genero):
        self._musica = musica
        self._cantor = cantor 
        self._genero = genero
    def __str__(self):
        return f'Musica: {self._musica}\nCantor: {self._cantor}\nGênero: {self._genero}'
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
        while(p.get_proximo() != None):
            p = p.get_proximo()
        p.set_proximo(no)
        return p.get_proximo()
    def size(self):
        p = self._head
        cont = 0
        while(p.get_proximo() != None):
            cont += 1
            p = p.get_proximo()
        cont += 1
        return f'O tamanho da fila é de {cont}  itens..'
    def printall(self):
          p = self._head
          print(p,"\n")
          while(p.get_proximo() != None):
              p = p.get_proximo()
              print(p,"\n")
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
    def printall(self):
        p = self._head
        print(p,"\n")
        while(p.get_proximo()!= None):
            p = p.get_proximo()
            print(p,"\n")
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



dado = Dado('JGDGS','Jsifu','Trush')
no = No(dado)
fila = Fila(no)
print(fila.printall())
dado2 = Dado('Boom','Matuê','Rap')
no2 = No(dado2)
