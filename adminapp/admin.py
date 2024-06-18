from django.contrib import admin
from . models import UserDetails, ProfessionalExperience, Education
# Register your models here.

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'age', 'degree', 'freelance')
    search_fields = ('name', 'email', 'phone', 'city')
    list_filter = ('freelance', 'city')
    ordering = ('name',)
    

@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_year', 'end_year', 'location')
    search_fields = ('title', 'company', 'location')
    list_filter = ('company', 'location')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'location')
    search_fields = ('degree', 'institution', 'location')
    list_filter = ('institution', 'location')