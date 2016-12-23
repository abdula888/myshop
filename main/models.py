from django.db import models

class ProductMatEgo(models.Model):
	title = models.CharField("NaiMelBly",max_length=100)
	description = models.TextField("opisalssanie",max_length=3000)
	price = models.IntegerField("То что твое мое")
	def __str__(self):
		return self.description

	class Meta:
		verbose_name = "PATIMEYKERA"
		verbose_name_plural = "CS:Сын за отца сосал хуйца"