from django.shortcuts import render
#from django.http import HttpResponse
from .models import Pet

# Create your views here.
def index(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }
    return render(request, 'pets/index.html', context)

def about(request):
    return render(request, 'pets/about.html')

def our_pets(request):
    from .models import Pet, Category
    pets = Pet.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'pets': pets,
        'categories': categories
    }
    return render(request, 'pets/ourpets.html', context)