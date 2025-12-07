from . import models, forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        return queryset


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brand_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.add_brand'
    form_class = forms.BrandForm


class BrandDetailView(LoginRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brand_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.change_brand'


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_confirm_delete.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.delete_brand'