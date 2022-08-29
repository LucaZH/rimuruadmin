from django.shortcuts import render
from rest_framework import generics
from .models import CentreMedical,Pharmacie,Utilisateur,Conseil
from .serializers import CentreMedicalapiSerializer,UtilisateurapiSerializer,PharmacieapiSerializer,ConseilapiSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = Utilisateur.objects.all()
        serializer = UtilisateurapiSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UtilisateurapiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def user_detail(request, pk):
    try:
        user = Utilisateur.objects.get(pk=pk)
    except Utilisateur.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UtilisateurapiSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UtilisateurapiSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def centremedical_list(request):
    if request.method == 'GET':
        centremedicals = CentreMedical.objects.all()
        serializer = CentreMedicalapiSerializer(centremedicals, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CentreMedicalapiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def centremedical_detail(request, pk):
    try:
        cm = CentreMedical.objects.get(pk=pk)
    except CentreMedical.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CentreMedicalapiSerializer(cm)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CentreMedicalapiSerializer(cm, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cm.delete()
        return HttpResponse(status=204)

@csrf_exempt
def pharmacie_list(request):
    if request.method == 'GET':
        pharmacies = Pharmacie.objects.all()
        serializer = PharmacieapiSerializer(pharmacies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PharmacieapiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def pharmacie_detail(request, pk):
    try:
        pharmacie = Pharmacie.objects.get(pk=pk)
    except Pharmacie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PharmacieapiSerializer(pharmacie)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PharmacieapiSerializer(pharmacie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pharmacie.delete()
        return HttpResponse(status=204)


@csrf_exempt
def conseil_list(request):
    if request.method == 'GET':
        conseils = Conseil.objects.all()
        serializer = ConseilapiSerializer(conseils, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ConseilapiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def conseil_detail(request, pk):
    try:
        conseil = Conseil.objects.get(pk=pk)
    except Conseil.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ConseilapiSerializer(conseil)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ConseilapiSerializer(conseil, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        conseil.delete()
        return HttpResponse(status=204)