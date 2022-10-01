from django.shortcuts import render, get_object_or_404
from book_app.models import Record

def index_view(request):
    records = Record.objects.filter(status='ACTIVE').order_by('-created_at').values()
    context = {'records': records}
    return render(request, 'index.html', context=context)