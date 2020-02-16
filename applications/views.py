from django.http import HttpResponse
from django.template import loader

def top_page(request):
	template = loader.get_template("applications/top_page.html")
	return HttpResponse(template.render({}, request))