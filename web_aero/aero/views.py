from django.shortcuts import render, redirect, get_object_or_404

from . forms import BlogForm

from . models import Blog


def revamp(request):
    return render(request,'aero/revamp.html');

def index(request):
    return render(request,'aero/index.html');

def gallery(request):
    return render(request,'aero/gallery.html');

def events(request):
	return render(request,'aero/events.html');

def addblogs(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        blog = form.save()
        return redirect('blogs')
    else:
        form = BlogForm()
        blogs = Blog.objects.all()
    return render(request, 'aero/blogs/base.html', {'form': form , 'blogs': blogs})

def gblog(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'aero/blogs/blog.html', {'blog': blog})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'aero/blogs/allblogs.html', {'blogs':blogs})
