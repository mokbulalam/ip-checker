from django.http import HttpResponse
from django.shortcuts import render
import ipaddress

def home(request):

	ip = get_client_ip(request)

	ip_version = ipaddress.ip_address(ip)._version

	if ip_version==4:
		return render(request, "errorpage.html")
	elif ip_version==6:
		return render(request, "catpage.html")
	else:
		return render(request, "homepage.html")

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(",")[0]
	else:
		ip = request.META.get("REMOTE_ADDR")
	return ip


