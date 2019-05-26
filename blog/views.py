from django.shortcuts import render
from . models import Blog
from django.http import HttpResponse
# Create your views here.
def blog(request):
    context={
    'blog':Blog.objects.all()[:5],
    }

    return render(request,'blog-right.html',context)


def blog_details(request,blogid):
    context={}
    try:
        context.update({'blog':Blog.objects.get(id=blogid)})
        return render(request,'blog_details.html',context)
    except:
        return render(request,'404.html')
