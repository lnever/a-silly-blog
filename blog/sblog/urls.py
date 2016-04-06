from django.conf.urls import *
 
urlpatterns = patterns(('sblog.views'),
    url(r'^bloglist/$', 'blog_list', name='blog_list'),
    url(r"^$",'home' , name ='home'),
    url(r'^blog/(?P<_id>\d+)/$', 'blog_show', name='blog_show'),
    url(r'^add/$', 'blog_add', name='blog_add'),
    url(r'^del/(?P<_id>\w+)/$', 'blog_del', name='blog_del'),
    url(r'^edit/(?P<_id>\w+)/$', 'blog_edit', name='blog_edit'),
    # name属性是给这个url起个别名，可以在模版中引用而不用担心urls文件中url的修改 引用方式为{% url bloglist %}
)
