from order.models import Cart, ContactInformation, Order
from user.models import Profile


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


def get_next_order_no():
    order = Order.objects.values('order_number').order_by('-order_number').first()
    if order is None:
        return 1000
    else:
        order_no = order['order_number']
        return order_no + 1


def get_recently_viewed(user):
    profile = Profile.objects.get(user=user)
    recently_viewed= profile.recentlyviewed_set.order_by('-date')[1:5]    #product.distinct().order_by('')
    return recently_viewed
