from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^search/$', views.search_page, name='search_page'),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', views.logout_page),
    url(r'^accounts/register/$', views.register_page),
    url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),
]