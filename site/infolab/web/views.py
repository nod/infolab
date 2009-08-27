from django.shortcuts import render_to_response

from basic.blog.models import Post

def index(request):
    return render_to_response('web/index.html', {'posts':Post.objects.all()})
