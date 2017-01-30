from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import django.contrib.auth
from django.contrib.auth.decorators import login_required



@login_required
def get_profile(request):
	return render(request, 'userreg/profile.html')

