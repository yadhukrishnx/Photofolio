from django.db import models

# Create your models here.

class UserDetails(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        phone = models.CharField(max_length=15)
        birthday = models.DateField()
        website = models.URLField()
        city = models.CharField(max_length=100)
        age = models.IntegerField()
        degree = models.CharField(max_length=100)
        freelance = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Not Available', 'Not Available')])
        picture = models.ImageField(upload_to='profile_picture')
        heading1 = models.CharField(max_length=70)
        heading2 = models.CharField(max_length=150)
        description = models.CharField(max_length=500)
        def __str__(self):
            return self.email
        

class ProfessionalExperience(models.Model):
    title = models.CharField(max_length=200)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=200)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.degree


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    project_picture = models.ImageField(upload_to='project_pictures')
    project_category = models.CharField(max_length=200)
    project_description = models.TextField()
    client_name = models.CharField(max_length=200)
    client_note = models.CharField(max_length=200)
    project_date = models.DateField()

    def __str__(self):
        return f'{self.project_category} - {self.project_date}'
    
class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    