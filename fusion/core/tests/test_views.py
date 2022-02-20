from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha Mensagem'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)


class CadastroViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'funcionalidade': 'Felicity Jones',
            'descricao': 'uma descrição qualquer',
            'icone': 'Mobile',
            'lado': 'Direita',
            }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'funcionalidade': 'Felicity Jones',
            'descricao': 'felicity@gmail.com',
                }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
