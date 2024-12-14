from django import forms
from .models import Member
from django import forms
from django import forms
from jalali_date.widgets import AdminJalaliDateWidget
from .models import Member

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'LastName', 'phone', 'gender', 'date_of_birth', 'registration_date', 'MembershipPlan']
        widgets = {
            'date_of_birth': AdminJalaliDateWidget(attrs={
                'class': 'form-control jalali_date-input',
                'placeholder': 'تاریخ تولد به صورت ۱۴۰۳/۰۹/۲۴'
            }),
            'registration_date': AdminJalaliDateWidget(attrs={
                'class': 'form-control jalali_date-input',
                'placeholder': 'تاریخ ثبت‌نام به صورت ۱۴۰۳/۰۹/۲۴'
            }),
        }
        labels = {
            'name': 'نام',
            'LastName': 'نام خانوادگی',
            'phone': 'تلفن',
            'gender': 'جنسیت',
            'date_of_birth': 'تاریخ تولد',
            'registration_date': 'تاریخ ثبت‌نام',
            'MembershipPlan': 'پلن عضویت',
        }


class MemberEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'LastName', 'phone', 'gender', 'date_of_birth', 'registration_date', 'MembershipPlan']
        widgets = {
            'date_of_birth': AdminJalaliDateWidget(attrs={
                'class': 'form-control jalali_date-input',
                'placeholder': 'تاریخ تولد به صورت ۱۴۰۳/۰۹/۲۴'
            }),
            'registration_date': AdminJalaliDateWidget(attrs={
                'class': 'form-control jalali_date-input',
                'placeholder': 'تاریخ ثبت‌نام به صورت ۱۴۰۳/۰۹/۲۴'
            }),
        }
        labels = {
            'name': 'نام',
            'LastName': 'نام خانوادگی',
            'phone': 'تلفن',
            'gender': 'جنسیت',
            'date_of_birth': 'تاریخ تولد',
            'registration_date': 'تاریخ ثبت‌نام',
            'MembershipPlan': 'پلن عضویت',
        }