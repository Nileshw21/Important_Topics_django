
class Students2(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    ulpoad_file = models.FileField(upload_to="files/")
