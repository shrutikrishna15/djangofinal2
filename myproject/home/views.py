
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect,get_object_or_404
from home.forms import HomeForm,CommentForm
from home.models import Post,Friend,Comment
from django.http import HttpResponse
from django.views.generic import DetailView


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self,request):
        form = HomeForm()
        posts = Post.objects.all()
        #users = User.objects.exclude(id=request.user.id)
        args = {'form':form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('/home')

        args = {'form': form, 'text': text }
        return render (request, self.template_name,args)



def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('home:', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'home/comment.html', {'form': form,'post':post})

class DetailPost(DetailView):
    model = Post
template_name = "home/post.html"