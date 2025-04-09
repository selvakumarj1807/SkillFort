from django.http import JsonResponse
from django.shortcuts import render

from Enquiry.models import StudentEnquiry

# Create your views here.
# Homepage View
def adminSFhome(request):
    return render(request, 'ManagementIndex.html')

# Enquiry Form View
def enquiry_Detail(request):
    enquiries = list(StudentEnquiry.objects.all().order_by('-created_at').values())  # Order by created_at descending
    enquiry_count = StudentEnquiry.objects.count()

    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({"count": enquiry_count, "enquiries": enquiries}, safe=False)

    return render(request, 'EnquiryDetails.html', {'enquiries': enquiries})


