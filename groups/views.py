from django.http import HttpResponse

def main_page(request):
    html = "<html><body>Nothing to see yet</body></html>"
    return HttpResponse(html)
