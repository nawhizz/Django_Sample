from django.db import models

# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=10)
	introduction = models.TextField()
	area = models.CharField(max_length=15)
	party_number = models.IntegerField(default=0)

	def __str__(self):
		return self.name	#object를 출력하면 name이 보입니다.


class Poll(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	area = models.CharField(max_length = 15)


class Choice(models.Model):
	poll = models.ForeignKey(Poll)	#Poll 모델의 id를 이용
	candidate = models.ForeignKey(Candidate)
	votes = models.IntegerField(default = 0)
