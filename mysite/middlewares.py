from django.utils.deprecation import MiddlewareMixin

class MyTest(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Headers'] = "Content-Type, Authorization, Accept, X-Requested-With"
        response['Access-Control-Allow-Methods'] = "GET, POST, OPTIONS, PUT, DELETE"
        return response