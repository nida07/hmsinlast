from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password1': forms.PasswordInput()
        }
    def clean_password(self):
        password = self.cleaned_data['password']

            # Custom password strength validation
        if len(password) < 8:
            raise forms.ValidationError("Password should be at least 8 characters long.")

        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password should contain at least one uppercase letter.")

        if not any(char.isalnum() for char in password):
            raise forms.ValidationError("Password should contain at least one alphanumeric character.")

        return password

    def clean_username(self):
        username = self.cleaned_data['username']

            # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")

        return username



class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
    # }
    def clean_password(self):
        password = self.cleaned_data['password']

            # Custom password strength validation
        if len(password) < 8:
            raise forms.ValidationError("Password should be at least 8 characters long.")

        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password should contain at least one uppercase letter.")

        if not any(char.isalnum() for char in password):
            raise forms.ValidationError("Password should contain at least one alphanumeric character.")

        return password

    def clean_username(self):
        username = self.cleaned_data['username']

            # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")

        return username

class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','is_active','profile_pic']

#for patient related form

class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
    # }
    def clean_password(self):
        password = self.cleaned_data['password']

            # Custom password strength validation
        if len(password) < 8:
            raise forms.ValidationError("Password should be at least 8 characters long.")

        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password should contain at least one uppercase letter.")

        if not any(char.isalnum() for char in password):
            raise forms.ValidationError("Password should contain at least one alphanumeric character.")

        return password

    def clean_username(self):
        username = self.cleaned_data['username']

            # Check if the username already exists in the database
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")

        return username

class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.filter(is_active=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','is_active','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.filter(is_active=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.filter(is_active=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    appointment_datetime = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}),input_formats=['%Y-%m-%dT%H:%M'],help_text='Format: YYYY-MM-DDTHH:MM (24-hour clock)')
    class Meta:
        model=models.Appointment
        fields=['description','is_active','appointment_datetime']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.filter(is_active=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','is_active']


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
class LeaveForm(forms.Form):
    leave_day = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    partial_leave = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    partial_time_on_leave_start = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    partial_time_on_leave_end = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

# class ForgotPasswordForm(forms.Form):
#     email = forms.EmailField()