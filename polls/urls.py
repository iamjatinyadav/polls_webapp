from django.urls import path
from polls import views

app_name="polls"
urlpatterns = [
    path('', views.index, name="home"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.result, name="result"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]
