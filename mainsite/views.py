from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect


# Create your views here.
def homepage(request):
    # posts = Post.objects.all()
    # post_list=list()
    # for count,post in enumerate(posts):
    #     post_list.append('No.{}:'.format(str(count))+str(post)+'<br>')
    # return HttpResponse(post_list)

    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')