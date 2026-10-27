from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    description=models.TextField()
    salary=models.IntegerField()
    is_active=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Jobseeker(models.Model):

    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,related_name='job_applicant')
    resume_link=models.URLField(blank=True)
    cover_letter=models.TextField(blank=True)
    applied_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[

            models.UniqueConstraint(
                fields=['job','applicant'],
                name='unique_job_application'
            )
        ]
        