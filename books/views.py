from django.shortcuts import render


from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
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
