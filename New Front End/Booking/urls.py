from django.urls import path
from Booking import views

urlpatterns = [
    
    # students
    path('guestroom', views.guestroom, name='guestroom'),
    path('guestroom_pb', views.guestroom_pb, name='guestroom_pb'),
    # hall manager
    path('pending', views.pending, name='pending'),
    path('aprooved', views.bookings_aprooved, name='bookings_aprooved'),


    # path('return_request_initiate', views.return_request_initiate, name='return_request_initiate')
]