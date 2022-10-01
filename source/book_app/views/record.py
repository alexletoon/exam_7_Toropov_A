from django.shortcuts import render, redirect
from book_app.models import Record
from forms import RecordForm


def add_record_view(request):
    form = RecordForm()
    if request.method == 'GET':
        return render(request, 'add_record.html', context={
            'form': form
        })
    form = RecordForm(request.POST)
    if not form.is_valid():
        return render (request, 'add_record.html', context={
            'form': form
        })
    record = Record.objects.create(**form.cleaned_data)
    return redirect('index_view')

