from django.urls import path
from .views import BookView, WriterView
#from .views import book_detail_view


app_name = "books"


urlpatterns = [
    #path('books/', BookView.as_view()),
    # path('books/<int:pk>', book_detail_view)
    path('books/<int:pk>', BookView.as_view()),
    path('writers/<int:pk>', WriterView.as_view())
]
