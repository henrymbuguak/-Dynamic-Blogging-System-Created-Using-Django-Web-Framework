from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from django.template import Context, RequestContext
from django.template.loader import get_template
from django.utils import timezone

from django.contrib.auth.models import User
from klab.models import Post
from klab.forms import *

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:5]
    template = get_template('klab/post_list.html')
    variables = Context({'user':request.user})
    output = template.render(variables)
    return render(request, 'klab/post_list.html', {'posts': posts},{'output':output})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'klab/post_detail.html', {'post': post})

def search_page(request):
    form = SearchForm()
    posts = []
    show_results = False
    if request.GET.has_key('query'):
        show_results = True
        query = request.GET['query'].strip()
        if query:
            form = SearchForm({'query': query})
            posts = \
                Post.objects.filter(text__icontains=query)[:10]
    variables = RequestContext(request, {'form': form,
        'posts' : posts,
        'show_results': show_results,
        
    })
    return render(request, 'klab/search.html',{'form':form})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render(request, 'registration/register_page.html', {'form': form})