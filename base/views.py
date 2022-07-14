from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Refueling


class CustomLoginView(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('refs')


class RegisterPage(FormView):
  template_name = 'base/register.html'
  form_class = UserCreationForm
  redirect_authenticated_user = True
  success_url = reverse_lazy('refs')

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      login(self.request, user)
    return super(RegisterPage, self).form_valid(form)

  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('refs')
    return super(RegisterPage, self).get(self.request)


class RefList(LoginRequiredMixin, ListView):
  model = Refueling
  context_object_name = 'refuelings'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['refuelings'] = context['refuelings'].filter(user=self.request.user)
    
    search_input = self.request.GET.get('searching') or ''
    if search_input:
      context['refuelings'] = context['refuelings'].filter(
        title__icontains=search_input)

    context['search_input'] = search_input

    return context


class RefDetail(LoginRequiredMixin, DetailView):
  model = Refueling
  context_object_name = 'refueling'
  template_name = 'base/ref.html'


class RefCreate(LoginRequiredMixin, CreateView):
  model = Refueling
  fields = ['title', 'price_per_liter', 'amount', 'location']
  success_url = reverse_lazy('refs')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(RefCreate, self).form_valid(form)


class RefUpdate(LoginRequiredMixin, UpdateView):
  model = Refueling
  fields = ['title', 'price_per_liter', 'amount', 'location']
  success_url = reverse_lazy('refs')

  
class RefDelete(LoginRequiredMixin, DeleteView):
  model = Refueling
  context_object_name = 'refueling'
  success_url = reverse_lazy('refs')

