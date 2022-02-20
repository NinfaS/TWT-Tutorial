from django.db import models
import numpy as np


# Create your models here.
class DataSet(models.Model):
    name = models.CharField(max_length=200, unique=True)
    num_entries = models.IntegerField()
    x_mu = models.FloatField()
    x_sigma = models.FloatField()

    def save(self, *args, **kwargs):
        super(DataSet, self).save(*args, **kwargs)
        for _ in range(self.num_entries):
            self.datapoint_set.create(x=np.random.normal(self.x_mu, self.x_sigma))

    def __str__(self):
        return self.name


class DataPoint(models.Model):
    todolist = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    x = models.FloatField()

    def __str__(self):
        return str(self.x)
