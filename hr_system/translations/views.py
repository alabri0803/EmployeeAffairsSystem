from django.http import JsonResponse
from .utils import translate_text

def translate_api(request):
    text = request.GET.get('text')
    result = translate_text(text)
    return JsonResponse({'text': result})