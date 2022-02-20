from django.views.generic import ListView
from .models import Obra
from django.shortcuts import get_object_or_404, render


class IndexView(ListView):
    model = Obra
    template_name = 'index.html'
    queryset = Obra.objects.all()
    context_object_name = 'obra'


def obra(request, id):
    # prod = Produto.objects.get(id=pk)
    arte = get_object_or_404(Obra, id=id)
    context = {
        'arte':  arte
    }
    return render(request, 'obra.html', context)