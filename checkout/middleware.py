# coding=utf-8
from .models import CartIten

def cart_iten_middleware(get_response):

    def middleware(request):
        session_key = request.session.session_key
        response = get_response(request)
        if session_key != request.session.session_key:
            CartIten.objects.filter(
                cart_id=session_key).update(
                cart_id=request.session.session_key
                )
        return response
    return middleware