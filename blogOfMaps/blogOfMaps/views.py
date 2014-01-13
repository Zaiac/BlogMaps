from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse


def main_page(request):
    t = get_template('main.html')
    html = t.render(RequestContext(request, {}))
    return HttpResponse(html)