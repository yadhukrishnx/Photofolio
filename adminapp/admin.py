from django.contrib import admin
from . models import UserDetails, ProfessionalExperience, Education,Projects,Services
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
    
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_category', 'client_name', 'project_date')
    search_fields = ('project_category', 'client_name')
    list_filter = ('project_category', 'client_name', 'project_date')
    ordering = ('-project_date',)
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ('title',)