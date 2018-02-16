from django.urls import path
from dictionary.views import IndexView,PageView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('p/<int:pk>', PageView.as_view(), name='page'),
]