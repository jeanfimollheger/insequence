from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from accounts.models import SiteUser
from accounts.forms import SiteUserSignupForm

# Create your views here.
def index(request):
  return render(request, 'accounts/index.html')

#def signup(request):
#  return render(request, 'accounts/signup.html')

class SiteUserCreateView(CreateView):
  model = SiteUser
  form_class = SiteUserSignupForm
  success_url = reverse_lazy("index")

  """
  Creer la ListView => SiteUserListView avec
  la template_name 'siteuser_list'
  pour 
  la success_url : reverse_lazy('siteuser_list')"""

