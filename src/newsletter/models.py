from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField(max_length=254,blank=False)
	full_name = models.CharField(max_length=50, blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3 __str__
		return self.email