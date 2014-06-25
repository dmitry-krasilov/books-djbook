from django.shortcuts import render


from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
