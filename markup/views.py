from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import FileFieldForm
from .models import Category, Image

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html',{'categories': categories})


def images(request, category):
    category_by_name = get_object_or_404(Category, name=category)
    images_in_category = Image.objects.filter(category=category_by_name)
    return render(request, 'images.html',{'category': category, 'images': images_in_category})

    
def upload(request, category):
    category_by_name = get_object_or_404(Category, name=category)
    if request.method == 'POST' and request.user.is_authenticated:
        form = FileFieldForm(request.POST, request.FILES)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                obj, created = Image.objects.get_or_create(
                    category = category_by_name,
                    img = f
                )
                if created:
                    obj.save()
                
            return redirect("images", category=category)
    else:
        form = FileFieldForm()

    return render(request, 'upload.html',{'category': category, 'form': form})

def result(request, category):
    pass

def markup(request, category, image):
    pass