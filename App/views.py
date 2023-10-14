from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Brain.GooglePalm import text_to_info
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# @method_decorator(login_required(login_url='admin/'), name='dispatch')

class IndexPage(View):
    def get(self, request):
        data = {}
        return render(request, 'Pages/index.html', data)

@csrf_exempt
def getAnswer(request):
    print(request.method)
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        answer = text_to_info(prompt)
        print(answer)
        return JsonResponse({'answer': answer})
    else:
        prompt = request.GET.get('prompt')
        print(prompt)
        answer = text_to_info(prompt)
        print(answer)
        return JsonResponse({'answer': answer})
        return JsonResponse({'error': 'Request is not valid'})




