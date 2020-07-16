from django.urls import path
from .views import IndexTemplateView

app_name = 'todo'

urlpatterns = [
    path('', IndexTemplateView.as_view()),
]