from django.urls import path
from .views import home, enquiry_form, StudentEnquiryAPI, StudentEnquiryDetailAPI

app_name = 'Enquiry'

urlpatterns = [
    # Template-based Views (for HTML forms)
    path('', home, name='home'),
    path('enquiryForm/', enquiry_form, name='enquiry_form'),

    # API Views (Django REST Framework)
    path('api/submit-enquiry/', StudentEnquiryAPI.as_view(), name='submit-enquiry'),  # Fix name here
    path('api/submit-enquiry/<int:pk>/', StudentEnquiryDetailAPI.as_view(), name='enquiry_detail'),
]
