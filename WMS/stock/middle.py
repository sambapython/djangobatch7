from stock.models import Tracker
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
class TrackerMiddleWare:
	def __init__(self, view_fun):
		self.view=view_fun

	def __call__(self, request):
		#return HttpResponse("Hello, How are you.")
		# write a code want to execute before request
		meta_data = request.META
		hostname = meta_data.get("COMPUTERNAME","localhost1")
		url = meta_data.get("PATH_INFO")
		track=Tracker(hostname=hostname,
					request_url=url
			)
		user_id = request.session.get('_auth_user_id')
		if user_id:
			track.user=User.objects.get(pk=user_id)
		resp= self.view(request)
		track.response_statu_code=resp.status_code
		track.save()
		if url not in ["/media/","/favicon.ico"] and \
			resp.status_code==404:
			return render(request,"stock/404.html")
		# write a code to execute before sending response
		return resp
