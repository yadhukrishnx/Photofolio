from django import forms
from .models import UserDetails, ProfessionalExperience, Education


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = [
            'name', 'email', 'phone', 'birthday', 'website', 'city', 'age', 
            'degree', 'freelance', 'picture', 'heading1', 'heading2', 'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name detail'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email detail'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone detail'}),
            'birthday': forms.DateInput(attrs={'placeholder': 'Enter birthday detail'}),
            'website': forms.URLInput(attrs={'placeholder': 'Enter website detail'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city detail'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age detail'}),
            'degree': forms.TextInput(attrs={'placeholder': 'Enter degree detail'}),
            'freelance': forms.Select(attrs={'placeholder': 'Enter freelance detail'}),
            'picture': forms.ClearableFileInput(attrs={'placeholder': 'Upload profile picture'}),
            'heading1': forms.TextInput(attrs={'placeholder': 'Enter heading1 detail'}),
            'heading2': forms.TextInput(attrs={'placeholder': 'Enter heading2 detail'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description detail'}),
        }
        

class ProfessionalExperienceForm(forms.ModelForm):
    class Meta:
        model = ProfessionalExperience
        fields = ['title', 'start_year', 'end_year', 'company', 'location', 'description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'start_year', 'end_year', 'institution', 'location', 'description']