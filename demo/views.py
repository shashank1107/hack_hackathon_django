from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@require_http_methods(["GET"])
def home_page_view(request):
    if not request.session.session_key:
        request.session.save()
    return render(request, template_name='demo/index.html')


@api_view(['POST'])
def configure_demo_app(request):
    """
        payload =>
        {"app_name": "Demo App"}
    """
    payload = request.data
    return Response(status=status.HTTP_200_OK,
                    data={'success': True, 'message': f"{payload['app_name']} App successfully configured"})
