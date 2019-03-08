from django.shortcuts import render
from django.http import HttpResponse
from .forms import TagForm

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def select(request):
    return render(request, 'index/select.html')

def index(request):
	name = "test"
	current_day = "test"
	form = TagForm(request.POST or None)
	if request.method == "POST":
		print (request.POST)
		new_form = form.save()

	return render(request, 'index/index.html', locals())