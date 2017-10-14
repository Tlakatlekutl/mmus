from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

import json


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
        return JsonResponse({})
    else:
        return JsonResponse({'status': 'error', 'message': 'Incorrect password or login'},
                            status=403)


@login_required
def logout_user(request):
    logout(request)
    return JsonResponse({})