from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .forms import CadastroModelForm, ContatoForm
from .models import Funcionario, Servico, Funcionalidade
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        context['funcionalidades'] = Funcionalidade.objects.all()
        context['lang'] = lang
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, _('E-mail enviado com sucesso'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar E-mail'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class TabelaView(TemplateView):
    template_name = 'tabela.html'

    def get_context_data(self, **kwargs):

        context = super(TabelaView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('id').all()
        return context


class FuncionarioView(TemplateView):
    template_name = 'funcionario.html'

    def get_context_data(self, **kwargs):
        context = super(FuncionarioView, self).get_context_data(**kwargs)
        context['func'] = Funcionario.objects.all()
        return context


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Funcionario, id=pk)
    context = {
        'func':  prod
    }
    return render(request, 'funcionario.html', context)


class CadastroView(FormView):

    template_name = 'cadastro.html'
    form_class = CadastroModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, _('Funcionalidade cadastrada com sucesso'))
        form.save()
        return super(CadastroView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('erro de cadastro'))
        return super(CadastroView, self).form_invalid(form, *args, **kwargs)

