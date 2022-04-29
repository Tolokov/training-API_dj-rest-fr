from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=500)
    restaurant_uniq_id = models.IntegerField(unique=True)
    borough = models.CharField(max_length=300)
    cuisine = models.CharField(max_length=300)
    building = models.CharField(max_length=15)
    street = models.CharField(max_length=500)
    zipcode = models.IntegerField(null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f'"{self.name}" - {self.restaurant_uniq_id} - {self.borough}'

    @property
    def count_reviews(self):
        return Grade.objects.filter(fk_grade=self.pk).count()

    @property
    def max_score(self):
        if bool(Grade.objects.filter(fk_grade=self.pk)):
            return int(Grade.objects.filter(fk_grade=self.pk).aggregate(models.Avg('score'))['score__avg'])
        else:
            return f'-'


class Grade(models.Model):
    fk_grade = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    grade = models.CharField(max_length=2)
    score = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.fk_grade.name} {self.score} {self.grade}'



