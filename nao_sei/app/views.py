from django.shortcuts import render

# Create your views here.
a= "Esse é m teste em python"
def home(request):
	return render(request,'home.html',{})