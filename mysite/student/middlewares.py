#  coding=utf-8
"""
Created:2019-09-20 11:01
@Author:Jacob Yang
function description: 
"""
import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):

	def process_request(self, request):
		self.__start_time = time.time()
		return

	def process_view(self, request, func, *args, **kwargs):
		if request.path != reverse('index'):
			return None
		start = time.time()
		response = func(request)
		cost_time = time.time() - start
		print('process view spend :{:.2f}s'.format(cost_time))
		return response

	def process_exception(self, request, response):
		pass

	def process_template_response(self, request, response):
		return response

	def process_response(self, request, response):
		cost_time = time.time() - self.__start_time
		print('request to response spend :{:.2f}s'.format(cost_time))
		return response
