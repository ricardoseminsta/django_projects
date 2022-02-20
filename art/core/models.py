from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Obra(Base):
    image = StdImageField('Imagem', upload_to='obras', variations={'thumb': (124, 124)})
    nome = models.CharField('Nome da Obra', max_length=100)
    data = models.DateField('Data da Obra')
