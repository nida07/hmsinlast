from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):

    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.TextField()
    mobile = models.CharField(max_length=10, null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')

    is_active=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):

    id = models.AutoField(primary_key=True)
    user_id=models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    
    is_active=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)

    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor=models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="doctor_appointments")

    appointment_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=500, null=True, blank=True)
    
    is_active=models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)



class PatientDischargeDetails(models.Model):

    id = models.AutoField(primary_key=True)
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="appointment_discharge")

    admit_date=models.DateTimeField(null=False)
    release_date=models.DateTimeField(null=True, blank=True)

    room_charge=models.PositiveIntegerField(null=False)
    medicine_Cost=models.PositiveIntegerField(null=False)
    doctor_fee=models.PositiveIntegerField(null=False)
    other_charge=models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def get_total_amount(self):
        total = 0
        total += int(self.room_charge) if self.room_charge else 0
        total += int(self.medicine_Cost) if self.medicine_Cost else 0
        total += int(self.doctor_fee) if self.doctor_fee else 0
        total += int(self.other_charge) if self.other_charge else 0
        return total
    

class DoctorLeave(models.Model):

    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor_leave")

    leave_day = models.DateField()
    partial_leave = models.BooleanField(default=False)
    partial_time_on_leave_start = models.TimeField(blank=True, null=True)
    partial_time_on_leave_end = models.TimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.doctor.user.first_name} is leave on {self.leave_day}'


class Holidays(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=100)
    is_public = models.BooleanField(default=False)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title}: {self.date}"


# time scheduling
class DoctorSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    is_working = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.time} ({'Working' if self.is_working else 'Not Working'})"
