


from django.db import models

# Create your models here.
class Division (models.Model):
    name=models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)
    url=models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name




class District (models.Model):
    name = models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)
    division= models.ForeignKey(Division,on_delete=models.CASCADE)
    lat=models.CharField(max_length=500, null=True)
    lon=models.CharField(max_length=500, null=True)
    url=models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Category (models.Model):
    name = models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chodokotha (models.Model):

    title= models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    district= models.ForeignKey(District,on_delete=models.CASCADE)


    def __str__(self):
        return self.title


