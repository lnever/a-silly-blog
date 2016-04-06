from django.shortcuts import render,render_to_response
from sblog.models import Blog
from django.http import Http404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from sblog.models import Author
from sblog.forms import BlogForm
# Create your views here.

def blog_del(request, _id):
    try:
        blog = Blog.objects.get(id=_id)
    except Exception:
    	return render(request, "base.html")
    if blog:
        blog.delete()
        return HttpResponseRedirect("/sblog/bloglist/")
    blogs = Blog.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})

def blog_edit(request, _id):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['caption']
            author = Author.objects.get(id=1)
            content = cd['content']
            blog = Blog.objects.get(id=_id)
            blog.caption = title
            blog.content = content
            blog.save()
            return HttpResponseRedirect('/sblog/blog/%s' % _id)
    else:
        try:
            blog = Blog.objects.get(id=_id)
        except Exception:
            return render(request, "base.html")
        form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
        return render_to_response('blog_add.html',{'blog': blog, 'form': form, 'id': _id},context_instance=RequestContext(request))

def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['caption']
            author = Author.objects.get(id=1)
            content = cd['content']
            blog = Blog(caption=title, author=author, content=content)
            blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/sblog/blog/%s' % id)
    else:
        form = BlogForm()
    return render_to_response('blog_add.html',{'form': form}, context_instance=RequestContext(request))

def home(request):
    return render(request, "home.html")

def blog_list(request):
    blogs =list( Blog.objects.all())
    return render_to_response("blog_list.html", {"blogs": blogs})

def blog_show(request, _id):
    try:
        blog = Blog.objects.get(id=_id)
    except Blog.DoesNotExist:
        return render(request, "base.html")
    return render_to_response("blog_show.html", {"blog": blog})
        
