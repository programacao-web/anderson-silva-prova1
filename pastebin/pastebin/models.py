# LEANGUAGE_CHOICES = (
#     ('python',  'PYTHON'),
#     ('Javascript', 'JAVASCRIPT'),
# )
from django.db import models

class Paste (models.Model):

    paste_title = models.CharField(max_length=50)
    paste_language = models.CharField(max_length=50)
    paste_data = models.CharField(max_length=300)

    def __str__(self):
        return self.paste_title
