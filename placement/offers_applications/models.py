from django.db import models

# Create your models here.

class Recruiter(models.Model):
	uid=models.CharField(max_length=15)
	name=models.CharField(max_length=100)
	url=models.URLField()

	
class Offer(models.Model):
	recruiter=models.ForeignKey(Recruiter)
	description=models.TextField()
	minimum_cgpa=models.FloatField()
	major_ph=models.BooleanField(default=0)
	major_ch=models.BooleanField(default=0)
	major_es=models.BooleanField(default=0)
	major_bi=models.BooleanField(default=0)
	major_ma=models.BooleanField(default=0)
	deadline=models.DateField()

class Application(models.Model):
	offer=models.ForeignKey(Offer)
	applicant_uid=models.CharField(max_length=20) #college id
	interview_offer=models.BooleanField()
