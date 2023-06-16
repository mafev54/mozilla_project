from django.views import generic

from ..models.languaje import Languaje

class LanguajeListView(generic.ListView):
    model = Languaje
    context_object_name = 'languaje_list'
    template_name = 'catalog/languaje/languaje_list.html'
    
class LanguajeDetailView(generic.DetailView):
    model = Languaje
    context_object_name ='languaje_detail'
    template_name = 'catalog/languaje/languaje_detail.html'
    
class LanguajeCreateView(generic.CreateView):
    model = Languaje
    fields = [
        'name',
    ]
    template_name = 'catalog/languaje/languaje_form.html'