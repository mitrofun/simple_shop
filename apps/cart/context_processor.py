from .cart import Cart


def cart(request):
    session = request.session
    return {'cart': Cart(session)}
