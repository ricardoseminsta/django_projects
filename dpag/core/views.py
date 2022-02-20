from django.views.generic import ListView

from .models import Produto


class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    paginate_by = 3
    ordering = 'id'