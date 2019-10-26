class Dado:
    def __init__(self,musica,cantor,genero):
        self._musica = musica
        self._cantor = cantor 
        self._genero = genero
    def __str__(self):
        return f'Musica: {self._musica}\nCantor: {self._cantor}\nGênero: {self._genero}'
  

