from django.contrib.auth.models import User
from django.db import models

from VRapp.models import Items


class ItemsBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemse = models.ForeignKey(Items, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.added.strftime("%Y.%m.%d %H:%M")}: {self.itemse.name}'

    def to_html(self):
        return f'<i>{self.added.strftime("%Y.%m.%d %H:%M")}</i>: <b>{self.itemse.name}</b>'