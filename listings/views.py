from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Property, User, Booking
from .serializers import PropertySerializer, UserSerializer,  BookingSerializer
from .tasks import send_booking_confirmation_email
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListingViewset(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Pass the user to the serializer
        serializer.save(host=self.request.user)


class BookingViewset(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()

        # Send email asynchronously
        booking_details = f"Booking ID: {booking.booking_id}, Date: {booking.start_date} - {booking.end_date}, Total price: {booking.total_price}"
        send_booking_confirmation_email.delay(
            booking.user_id.email, booking_details)
        # return Response({"sucess": "Booking created and details sent to your email"}, status.HTTP_201_CREATED)
