from django.shortcuts import render, render_to_response
from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from .models import *
# Create your views here.

def main(request):
    return render_to_response('index.html',{})

def medicamentos(request):
<<<<<<< HEAD
    return render_to_response('medicamentos.html',{})

def formula(request):
    return render_to_response('formula.html',{})
=======
    medicamentos=medicamento.objects.all()
    return render_to_response('medicamentos.html',locals())

def formula(request):
    return render_to_response('formula.html',{})

def farmacia(request):
    farmacia=farmacia.object.all()
>>>>>>> 104b1ee00d80dbad3b77df7cdfca9639f4d51813
