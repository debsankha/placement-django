from django.db import models

# Create your models here.

class Recruiter(models.Model):
	uid=models.CharField(max_length=15)
	name=models.CharField(max_length=100)
	url=models.URLField()

	
class Offer(models.Model):
	recruiter=models.ForeignKey(Recruiter)
	minimum_cgpa=models.FloatField()
	major_ph=models.BooleanField()
	major_ch=models.BooleanField()
	major_es=models.BooleanField()
	major_bi=models.BooleanField()
	major_ma=models.BooleanField()
	deadline=models.DateField()

class Application(models.Model):
	offer=models.ForeignKey(Offer)
	applicant_uid=models.CharField(max_length=20) #college id
	interview_offer=models.BooleanField()
