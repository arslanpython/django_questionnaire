from django.contrib import admin
from django.urls import path

from questionnaire import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questionnaire_id>/', views.next_question, name='next_question'),
    path('admin/', admin.site.urls),
]
