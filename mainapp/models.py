from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=512, verbose_name="Name")
    short_name = models.CharField(max_length=256, verbose_name="Shortname")
    post_address = models.TextField(blank=True, null=True, verbose_name="Address")
    bank_account = models.TextField(blank=True, null=True, verbose_name="Account")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()


class Developments(models.Model):
    cod = models.CharField(max_length=128, verbose_name="Cod")
    name = models.CharField(max_length=256, verbose_name="Name")
    parent = models.CharField(max_length=128, blank=True, null=True)
    levels = models.CharField(max_length=128, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()


class Worker(models.Model):
    firstname = models.CharField(max_length=256, verbose_name="Firstname")
    lastname = models.CharField(max_length=256, verbose_name="Lastname")
    post_address = models.TextField(blank=True, null=True, verbose_name="Address")
    bank_account = models.TextField(blank=True, null=True, verbose_name="Account")
    development = models.ForeignKey(Developments, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.firstname}"

    def delete(self, *args):
        self.deleted = True
        self.save()
