from uuid import uuid4
from django.db import models

# Create your models here.

class Wombat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text="Unique ID of this Wombat record")
    name = models.CharField(max_length=32)

    class Meta:  # customize the model
        db_table = 'wombats'  # optional
        verbose_name = 'wombat'
        verbose_name_plural = 'wombats'

    def __str__(self):  # how the model is displayed
        return self.name  # edit as needed
