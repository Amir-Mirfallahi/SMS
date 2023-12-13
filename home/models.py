from django.db import models


class Honor(models.Model):
    image = models.ImageField(upload_to='images/profiles')
    name = models.CharField(max_length=158)
    description = models.TextField(max_length=2048)

    class Meta:
        verbose_name = 'دستاورد علمی پژوهشی'
        verbose_name_plural = 'دستاورد های علمی پژوهشی'

    def __str__(self):
        return self.name
