from .views import (
    checkout,
    my_orders,
    all_orders,
    update_order_status,
    create_payment,
)

urlpatterns = [
    path("checkout/", checkout),
    path("payment/", create_payment),
    path("my-orders/", my_orders),
    path("all-orders/", all_orders),
    path("update/<int:id>/", update_order_status),
]