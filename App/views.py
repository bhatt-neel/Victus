from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Brain.GooglePalm import text_to_info
# @method_decorator(login_required(login_url='admin/'), name='dispatch')
class IndexPage(View):
    def get(self, request):
        data = {}
        return render(request, 'Pages/index.html', data)


@api_view(['POST'])
def getAnswer(request, format=None):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        answer = text_to_info(prompt)
        return Response({'answer': answer}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)

