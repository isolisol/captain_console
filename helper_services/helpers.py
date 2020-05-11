from order.models import Cart


def build_context(user):
    cart_items = Cart.objects.get(user_id=user.id, complete=False).productincart_set.all()
    total_price = calculateTotalPrice(cart_items)
    return {'cart_items': cart_items, 'total_price': total_price}


def calculateTotalPrice(cart_items):
    total_price = 0
    item_prices = cart_items.values('product__price')
    for price in item_prices:
        total_price += price['product__price']
    return total_price