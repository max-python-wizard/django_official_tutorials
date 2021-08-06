from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [

    # ex: /polls/
    # path('', TemplateView.as_view(template_name='views/main.html')),
    path('', views.index, name='index'),

    # ex: /polls/5/ - here were picking up a parameter, we say it should be int
    # we call views.detail passing HttpRequest and question_id
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]