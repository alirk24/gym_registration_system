from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Member, MembershipPlan

class MemberAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('name', 'LastName', 'registration_date_jalali', 'remaining_days')
    readonly_fields = ('registration_date',)  # Optional: Make this read-only
    fields = ('name', 'LastName', 'phone', 'gender', 'date_of_birth', 'registration_date', 'MembershipPlan')  # Fields to display/edit

admin.site.register(Member, MemberAdmin)
admin.site.register(MembershipPlan)