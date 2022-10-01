from django.shortcuts import render, redirect, get_object_or_404
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


def edit_record_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    form = RecordForm(instance=record)
    if request.method == 'GET':
        return render(request, 'edit_record.html', context ={'form': form})
    form = RecordForm(request.POST)
    if form.is_valid():
        Record.objects.update(**form.cleaned_data)
        return redirect('index_view')
