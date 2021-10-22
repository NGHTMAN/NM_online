from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create_form', views.create_form, name='create_form'),
    path('create', views.create, name='create'),
    path('success_saved', views.success_saved, name='success_saved'),
    path('<int:pk>/update/', views.QuestionsUpdateView.as_view(), name='question_update'),
    path('create_choice', views.ChoiceCreateView.as_view(), name='choice_create'),
    path('<int:pk>/choice_update/', views.ChoiceUpdateView.as_view(), name='choice_update'),
    path('<int:choice_id>/delete_choice', views.ChoiceDeleteView.as_view(), name='delete_choice'),
]
