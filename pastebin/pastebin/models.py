# LEANGUAGE_CHOICES = (
#     ('python',  'PYTHON'),
#     ('Javascript', 'JAVASCRIPT'),
# )
from django.db import models

class Post (models.Model):

    title = models.CharField(max_length=200)
    # linguagem = models.ChoiceField(choices=LEANGUAGE_CHOICES, default='python')
    linguagem = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title
