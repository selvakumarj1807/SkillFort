# forms.py
from django import forms
from .models import StudentEnquiry  # Replace with the actual model name if different
from django.core.exceptions import ValidationError

class StudentEnquiryForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Month DD, YYYY',
        'id': 'flatpickr-human-friendly'
    }))
    
    duration = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'YYYY-MM-DD to YYYY-MM-DD',
        'id': 'flatpickr-range'
    }))

    class Meta:
        model = StudentEnquiry
        fields = [
            "name", "dob", "mobile", "email", "education", "passout_year",
            "course", "placement", "currently_working", "profession", "company",
            "designation", "duration", "pf", "uan", "form16", "address",
            "pan_aadhar", "refer_by", "referer_mobile"
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'passout_year': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select select'}),
            'placement': forms.RadioSelect(),
            'currently_working': forms.RadioSelect(),
            'profession': forms.RadioSelect(),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'uan': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_aadhar': forms.TextInput(attrs={'class': 'form-control'}),
            'refer_by': forms.TextInput(attrs={'class': 'form-control'}),
            'referer_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'pf': forms.RadioSelect(),
            'form16': forms.RadioSelect(),
        }

    def clean_duration(self):
        duration = self.cleaned_data.get("duration")
        import re
        if not re.match(r"^\d{4}-\d{2}-\d{2}\s+to\s+\d{4}-\d{2}-\d{2}$", duration):
            raise ValidationError("Enter duration in 'YYYY-MM-DD to YYYY-MM-DD' format")
        return duration
