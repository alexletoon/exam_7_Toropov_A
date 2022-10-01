from django.urls import path
from book_app.views.base import index_view
from book_app.views.record import add_record_view

urlpatterns = [
    path("", index_view, name='index_view'),
    path('record/new_record/', add_record_view, name='add_record')
]