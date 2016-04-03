from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profile(models.Model):
	user=models.ForeignKey(User)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	phone_pattern = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+91'. Up to 10 digits")
	phone=models.CharField(validators=[phone_pattern],max_length=30)


	def __unicode__(self):
		return '%s %s'%(self.first_name,self.last_name)

	

		


class InternCategory(models.Model):
	name=models.CharField(max_length=100)
	company_name=models.CharField(max_length=100)
	def __unicode__(self):
		return self.name


class Internship(models.Model):
	interncategory=models.ForeignKey(InternCategory,null=True)
	location=models.CharField(max_length=50)
	stipend=models.IntegerField()
	duration=models.CharField(max_length=20)
	start_date=models.DateField()
	end_date=models.DateField()
	posted_on=models.DateField(null=True)
	desciption=models.TextField()
	image=models.ImageField(upload_to="ritu",null=True)
	aval=models.IntegerField(null=True)
	intern_detail=models.TextField(null=True)
	eligiblity=models.TextField(null=True)


	def __unicode__(self):
		return self.location

	@models.permalink
	def get_absolute_url(self):
		return ('single_detail', (), { 'intern_id': self.id})


class InternshipFill(models.Model):
	internshhip=models.ForeignKey(Internship,null=True)
	starting_date=models.DateField()
	expected_stipend=models.IntegerField()
	months_commit=models.CharField(max_length=10)
	assessment=models.TextField()

	def __unicode__(self):
		return self.assessment
	


    	

    	
