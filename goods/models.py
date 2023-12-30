from enum import unique
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'