from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete modo como vai ser deletado, entrar em doc django
    name = models.CharField(max_length=50)

    def __str__(self):  # metodo de como é mostrado na tela
        return self.name #+ " de: " + str(self.owner)

class Item(models.Model):
    name = models.CharField(max_length=50)
    item = models.ForeignKey(List, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):  # metodo de como é mostrado na tela
        return self.name
