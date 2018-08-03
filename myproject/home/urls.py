from django.conf.urls import url
from home.views import HomeView
from . import views
from django.contrib.auth.decorators import login_required


#from home import views


urlpatterns=[
  url(r'^$',HomeView.as_view(),name='home'),

  #url(r'^comment/', (CommentView.as_view()),name='comment'),

  url(r'^(?P<pk>\d+)/comment/$',login_required(views.add_comment_to_post),name='comment'),

]
