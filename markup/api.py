from django.http import JsonResponse
import json

def login(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    return JsonResponse(received_json_data)


def signup(request):
    # received_json_data = json.loads(request.body.decode("utf-8"))
    return JsonResponse({'ok':'hello'})