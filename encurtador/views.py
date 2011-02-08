import random

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers

from encurtador.models import Link
from encurtador.models import Logger

def index(request):
    return render_to_response('index.html',)

def post_link(request):
    if request.method == 'POST':
    	link = Link.objects.filter(longUrl=request.POST['post_data'])
	if len(link) <> 0:
	    retorno = serializers.serialize("json",  link)
	    return HttpResponse(retorno, mimetype="application/json")
        else:
	    mykey = random.choice('abcdefghijlmnopqrstuvxz')
	    while(True):
		if (len(Link.objects.filter(key=mykey)) <> 0):
		    mykey = random.choice('abcdefghijlmnopqrstuvxz')
		else:
		    break
	    newlink = Link()
	    newlink.key = mykey
	    newlink.longUrl = request.POST['post_data']
	    newlink.save()
	    print('depois do save')
	    retorno = serializers.serialize("json", newlink)
	    print('depois')
	    return HttpResponse(retorno, mimetype="application/json")

