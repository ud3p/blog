from django.shortcuts import render, render_to_response
from django.template import RequestContext
from posts.models import Post



def index(request):
	return render(request, 'index.html', {'posts': Post.objects.all()})

