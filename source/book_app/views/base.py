from django.shortcuts import render
from book_app.models import Record
from forms import SearchForm, RecordForm

def index_view(request):
    records = Record.objects.filter(status='ACTIVE').order_by('-created_at').values()
    if request.method == "GET":
        form = SearchForm()
        context = {'records': records, 'form': form}
        return render(request, 'index.html', context=context)
    form = SearchForm(request.POST)
    if not form.is_valid():
        return render(request, 'index.html', context={'records': records, 'form': form})
    records = Record.objects.filter(name=(form.cleaned_data['name'].capitalize()))
    context = {'records': records, 'form': form}
    return render(request, 'index.html', context=context)