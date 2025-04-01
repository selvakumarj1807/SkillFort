from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentEnquiry
from .serializers import StudentEnquirySerializer


# Homepage View
def home(request):
    return render(request, 'EnquiryIndex.html')

# Enquiry Form View
def enquiry_form(request):
    return render(request, 'EnquiryForm.html')


# Student Enquiry API (List & Create)
class StudentEnquiryAPI(APIView):
    def get(self, request):
        """Fetch all student enquiries"""
        enquiries = StudentEnquiry.objects.all()
        serializer = StudentEnquirySerializer(enquiries, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new student enquiry"""
        email = request.data.get('email')
        mobile = request.data.get('mobile')

        # Check for existing email or mobile
        if StudentEnquiry.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email already exists!", "status": "error"}, status=400)

        if StudentEnquiry.objects.filter(mobile=mobile).exists():
            return JsonResponse({"message": "Mobile number already exists!", "status": "error"}, status=400)

        serializer = StudentEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"message": "Student Enquiry Submitted Successfully!", "status": "success", "data": serializer.data},
                status=201
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Student Enquiry Detail API (Retrieve, Update, Delete)
class StudentEnquiryDetailAPI(APIView):
    def get(self, request, pk):
        """Fetch a single student enquiry"""
        enquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(enquiry)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Update a student enquiry"""
        enquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(enquiry, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student Enquiry Updated Successfully!", "status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a student enquiry"""
        enquiry = get_object_or_404(StudentEnquiry, pk=pk)
        enquiry.delete()
        return Response({"message": "Student Enquiry Deleted Successfully!", "status": "success"}, status=status.HTTP_204_NO_CONTENT)
