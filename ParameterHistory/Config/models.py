from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class Parameter(models.Model):
    user = models.CharField(max_length=30)
    option = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    created_day = models.DateTimeField(default=timezone.now)
    version = models.PositiveIntegerField(default=1)
    deleted_day = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.option} - {self.value} - {self.created_day} - {self.version}'

    def delete(self, using=None, keep_parents=False):
        self.deleted_day = timezone.now()
        self.save()

    def is_active(self):
        return not self.deleted_day


class ParameterHistory(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    option = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    created_day = models.DateTimeField()
    modified_day = models.DateTimeField(auto_now=True)
    deleted_day = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.parameter} - {self.user} - {self.option} - {self.value} - {self.created_day} - {self.modified_day} - {self.deleted_day}'


@receiver(post_save, sender=Parameter)
def create_parameter_history(sender, instance, created, **kwargs):
    ParameterHistory.objects.create(
        parameter=instance,
        user=instance.user,
        option=instance.option,
        value=instance.value,
        created_day=instance.created_day,
        deleted_day=instance.deleted_day,
    )


@receiver(pre_delete, sender=Parameter)
def delete_parameter(sender, instance, **kwargs):
    ParameterHistory.objects.create(
        parameter=instance,
        user=instance.user,
        option=instance.option,
        value=instance.value,
        created_day=instance.created_day,
        deleted_day=timezone.now(),
    )

