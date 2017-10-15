from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Category, Image, Solution, Tag
from django.core.serializers import serialize
from django.http import HttpResponse
import json, csv


@csrf_exempt
@require_POST
def signup(request):
    user_data = json.loads(request.body.decode("utf-8"))
    try:
        user = User.objects.create_user(
            user_data['displayName'],
            user_data['email'],
            user_data['password'],            
        )
        user.save()
        return JsonResponse({'displayName': user.username})
    except:
        return JsonResponse({'error': 'Signup error'}, status=403)


@csrf_exempt
@require_POST
def login_user(request):
    login_data = json.loads(request.body.decode("utf-8"))
    username = login_data['email']
    password = login_data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        category_user = Category.objects.filter(author=user).first() or None
        tag_list = Tag.objects.filter(category=category_user) if category_user else None
        return JsonResponse({
                                'displayName': user.username,
                                'email': user.email,
                                'markup':{
                                    'category': category_user.name if category_user else  None,
                                    'classes': [t.name for t in tag_list] if tag_list else [],
                                }
                            })
    else:
        return JsonResponse({'status': 'error', 'message': 'Incorrect password or login'},
                            status=403)


@login_required
def logout_user(request):
    logout(request)
    return JsonResponse({})


@csrf_exempt
@require_POST
def category(request):
    category_payload = json.loads(request.body.decode("utf-8"))
    category_name = category_payload['category']
    # try:
    tags_list = category_payload['classes']
    ctg, _ = Category.objects.get_or_create(
                    name = category_name,
                    author = request.user
                )
    for tg_name in tags_list:
        temp_tag, created = Tag.objects.get_or_create(name=tg_name)
        if created: temp_tag.save()
        ctg.tags.add(temp_tag)

    ctg.save()
    return JsonResponse({})
    # except:
        # return JsonResponse({'status': 'error', 'message': 'Error creating category with tags'},
                            # status=403)



@csrf_exempt
@require_POST
def upload(request):
    category = request.POST['category']
    category_by_name = Category.objects.filter(name=category).first()
    files = request.FILES.getlist('fileToUpload')
    for f in files:
        obj, created = Image.objects.get_or_create(
            category = category_by_name,
            img = f
        )
        if created:
            obj.save()
        
    return JsonResponse({})


@csrf_exempt
@require_POST
def result(request):
    category_payload = json.loads(request.body.decode("utf-8"))
    category = category_payload['category']
    category_by_name = Category.objects.filter(name=category).first() 
    if category_by_name is None:
        return JsonResponse({'error': 'File creating error, category not founf'}, status=404)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="output.csv"'

    category_images = Image.objects.filter(category=category_by_name)

    writer = csv.writer(response)
    writer.writerow(['Filename', 'X1', 'Y1', 'X2', 'Y2', 'Class'])

    for i in category_images:
        for c in Solution.objects.filter(img=i):
            writer.writerow([c.img.img.name, c.x1, c.y1, c.x2, c.y2, c.tag.name])    
        
    return response


@csrf_exempt
@require_POST
def image(request):
    category_payload = json.loads(request.body.decode("utf-8"))
    category = category_payload['category']
    category_by_name = Category.objects.filter(name=category).first()
    image = Image.objects.filter(category=category_by_name, ready=False).first() or Image.objects.filter(category=category_by_name).last()
    if image is None:
        return JsonResponse({'error': 'Images not found'}, status=404)
    return JsonResponse({'url': request.build_absolute_uri(image.img.url), 'id': image.id})
