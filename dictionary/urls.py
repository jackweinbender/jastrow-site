from django.urls import path
from dictionary.views import IndexView,PageView

urlpatterns = [
    path('', IndexView.as_view()),
    path('page/<int:pk>', PageView.as_view()),
]