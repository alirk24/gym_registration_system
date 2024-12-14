from django.db import models
from django.utils.timezone import now
# Create your models here.
from django.db import models
from datetime import timedelta

class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_months = models.PositiveIntegerField()

    def __str__(self):
        return self.name
class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'مرد'),
        ('F', 'زن'),
    ]

    name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    registration_date = models.DateTimeField(default=now)  # Make it editable
    MembershipPlan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def remaining_days(self):
        expiry_date = self.registration_date + timedelta(days=self.MembershipPlan.duration_in_months * 30)
        remaining_time = expiry_date - now()
        return max(remaining_time.days, 0)

    def registration_date_jalali(self):
        from jalali_date import date2jalali
        return date2jalali(self.registration_date).strftime('%Y/%m/%d')
    def extend_membership(self, days=30):
        self.registration_date += timedelta(days=days)
        self.save()