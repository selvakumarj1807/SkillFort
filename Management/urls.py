from django.urls import path
from .views import adminSFhome, enquiry_Detail

app_name = 'Management'

urlpatterns = [
    # Template-based Views (for HTML forms)
    path('', adminSFhome, name='adminSFhome'),
    path('enquiryDetails/', enquiry_Detail, name='enquiry_Detail'),

]
