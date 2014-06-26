from django.shortcuts import render


from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from books.models import Book

# Create your views here.

def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('page.html',
        {
        'values': values
        },
        RequestContext(request)
    )

def display_request_info(request):
    METAs = request.META.items()
    METAs.sort()
    POSTs = request.POST.values()
    GETs = request.GET.keys()
    return render_to_response('full_request_info.html',
        {
        'METAs': METAs,
        'POSTs': POSTs,
        'GETs': GETs
        },
        RequestContext(request)
    )


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not request.GET['q']:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html',
                {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html',
            {'error': error})