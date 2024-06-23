from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from funfun.models import Item


# Create your views here.
class FundingListView(ListView):
    model = Item

class FundingCreateView(CreateView):
    model = Item
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('funfun:item_list')

class FundingUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('funfun:item_list')

class FundingDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('funfun:item_list')
