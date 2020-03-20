from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic import  UpdateView, CreateView

# Create your views here.
class UpdateUserView(UpdateView):
	model = Profile
	fields = ['firstname','lastname','Designation','Age','Sex']

class CreateUserView(CreateView):
	model = Profile
	fields = ['firstname','lastname','Designation','Age','Sex']

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username	=	form.cleaned_data.get('username')
			messages.success(request, f'Account {username} is created successfully!')
			return redirect('login')

	else:
		form = UserCreationForm()
	return render(request, 'useracc/register.html', {'form': form})

def userview(request):
	context = {
		'accounts': User.objects.all()
	}
	return render(request, 'useracc/userview.html',context)


	

	

	
