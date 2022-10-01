from django.urls import path
from book_app.views.base import index_view
from book_app.views.record import add_record_view, edit_record_view, delete_record_view, deleted_view

urlpatterns = [
    path("", index_view, name='index_view'),
    path('record/new_record/', add_record_view, name='add_record'),
    path('record/edit_record/<int:pk>', edit_record_view, name='edit_record'),
    path('record/delete_record/<int:pk>', delete_record_view, name='confirm_delete'),
    path('record/deleted/<int:pk>', deleted_view, name='deleted')
]