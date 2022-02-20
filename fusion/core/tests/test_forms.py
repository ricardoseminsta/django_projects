from django.test import TestCase

from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.assunto = 'um assunto qualquer'
        self.mensagem = 'uma mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }
        self.form = ContatoForm(data=self.dados) # isso é igaul a ContatoForm(request.POST)

    def test_send_email(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEquals(res1, res2)
