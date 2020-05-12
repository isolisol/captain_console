from order.models import Cart, ContactInformation


def build_context(user):
    cart, created = Cart.objects.get_or_create(user_id=user.id, complete=False)
    cart_items = cart.productincart_set.all()
    total_price = calculateTotalPrice(cart_items)
    return {'cart_items': cart_items, 'total_price': total_price}


def calculateTotalPrice(cart_items):
    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity
    return total_price
