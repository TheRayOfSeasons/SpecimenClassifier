from django.db import models

from specimen.models import (
    Specimen
) 


class EpiphyticOrganism(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
