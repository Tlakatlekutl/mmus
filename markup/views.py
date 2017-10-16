from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import FileFieldForm
from .models import Category, Image, Solution, Tag
import csv
import zipfile, io, os
from django.http import HttpResponse
from django.conf import settings

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
    category_by_name = get_object_or_404(Category, name=category)    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="output.csv"'

    category_images = Image.objects.filter(category=category_by_name)

    writer = csv.writer(response)
    writer.writerow(['Filename', 'X1', 'Y1', 'X2', 'Y2', 'Class'])

    for i in category_images:
        for c in Solution.objects.filter(img=i):
            writer.writerow([c.img.img.name, c.x1, c.y1, c.x2, c.y2, c.tag.name])    
        
    return response

def markup(request, category, image):
    category_by_name = get_object_or_404(Category, name=category)
    category_tags = Tag.objects.filter(category=category_by_name)
    image_file = get_object_or_404(Image, pk=image)
    return render(request, 'markup.html',{'image': image_file,'tags':category_tags, 'c': category_by_name.name, 'id':image})


def next(request, category, image):
    category_by_name = get_object_or_404(Category, name=category)
    next_image = Image.objects.filter(id__gt=image, category=category_by_name).order_by('id').first()#filter(category=category_by_name, pk=image)
    if next_image:
        return redirect("markup", category=category, image=next_image.id)
    else:
        return redirect("images", category=category)



def download(request, category):
    category_by_name = get_object_or_404(Category, name=category)    
    stream = io.BytesIO()
    temp_zip_file = zipfile.ZipFile(stream, 'w')


    for image in Image.objects.filter(category=category_by_name):
        temp_zip_file.write(os.path.join(settings.MEDIA_ROOT, image.img.name), arcname=image.filename())
    temp_zip_file.close()

    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="temp.zip"'
    archive = stream.getvalue()
    stream.close()
    response.write(archive)
    return response 


def toggle(request, category, image):
    category_by_name = get_object_or_404(Category, name=category)
    image_file = get_object_or_404(Image, pk=image)
    image_file.ready = not image_file.ready
    image_file.save()
    return redirect("images", category=category)
