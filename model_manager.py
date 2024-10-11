from django.db.models import models



class Skillmanager(models.Manager):

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted = False)
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default = False)

    objects = Skillmanager()
    new_manager = models.Manager()
