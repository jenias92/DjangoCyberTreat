from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer


@login_required
def customers_list(request):
    context = {
        'customers': Customer.objects.all()
    }
    return render(request, 'customers/home.html', context)


class CustomersListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/home.html'
    context_object_name = 'customers'


class CustomersDetailView(LoginRequiredMixin, DetailView):
    model = Customer


class CustomersCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['last_name', 'first_name', 'email', 'address', 'birthday', 'phone']

    def get_form(self):
        from django.forms.widgets import SelectDateWidget
        form = super(CustomersCreateView, self).get_form()
        form.fields['birthday'].widget = SelectDateWidget()
        return form


class CustomersUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['last_name', 'first_name', 'email', 'address', 'birthday', 'phone']

    def get_form(self):
        from django.forms.widgets import SelectDateWidget
        form = super(CustomersUpdateView, self).get_form()
        form.fields['birthday'].widget = SelectDateWidget()
        return form
