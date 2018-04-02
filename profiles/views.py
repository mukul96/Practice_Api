from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from profiles.models import Users
from profiles.serializers import UsersSerializer,GenderSerializer
# Create your views here.
@csrf_exempt
def users_list(request):
    if request.method=='GET':
        users=Users.objects.all();
        serializer=UsersSerializer(users,many=True);
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def specific_user(request,username):

     check=Users.objects.get(name=username);
     print(check);
     serializer = UsersSerializer(check);
     return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_gender(request,username):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

