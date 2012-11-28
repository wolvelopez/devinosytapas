# Create your views here.
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	#solo mostramos los ultimos 3 posts
	lista_posts = Posts.objects.all().order_by('-id')[:3]
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))
