from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from accounts.models import SiteUser
from accounts.forms import SiteUserSignupForm

# Create your views here.
def index(request):
  return render(request, 'accounts/index.html')

class SiteUserListView(ListView):
  model = SiteUser

class SiteUserDetailView(DetailView):
  model = SiteUser
  success_url = reverse_lazy("siteuser-index")

class SiteUserCreateView(CreateView):
  model = SiteUser
  form_class = SiteUserSignupForm
  success_url = reverse_lazy("index")

  """
  Creer la ListView => SiteUserListView avec
  la template_name 'siteuser_list'
  pour 
  la success_url : reverse_lazy('siteuser_list')"""

