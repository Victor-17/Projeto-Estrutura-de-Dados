#class no
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
    def add(self,no):
        p=get_dado()
        while(p.get_proximo()==None):
            p.get_proximo()=no
            no.get_proximo()=None
    def __str__(self):
        return "{}".format(self._dado)
    