from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet, InitiatePayment, VerifyPayment
from django.urls import path


def trigger_error(request):
    division_by_zero = 1 / 0


router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')


urlpatterns = router.urls + [
    path('payments/initiate/<int:booking_id>/', InitiatePayment.as_view(), name='initiate-payment'),
    path('payments/verify/<str:tx_ref>/', VerifyPayment.as_view()),
    path('sentry-debug/', trigger_error),
]
