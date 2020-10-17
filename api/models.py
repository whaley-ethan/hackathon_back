from django.db import models

# Create your models here.

# Main organization model
class organization(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fax = models.CharField(max_length=200, default="")
    phone = models.IntegerField()
    operation_hours = models.CharField(max_length=200)

    services = models.ManyToManyField(service, related_name="organizations")
    eligibilities = models.ManyToManyField(eligibility, related_name="organizations")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Specific contact person info
class contact(models.Model):
    org = models.OneToOneField(organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Address of organization
class address(models.Model):
    org = models.OneToOneField(organization, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()

    class Meta:
        ordering = ['street']

    def __str__(self):
        return self.street

# Services available
class service(models.Model):
    name = models.CharField(max_length=200) # specific name of service_type, like 'education'
    service_type = models.CharField(max_length=200) # categories, medical, alternative, etc

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Eligibility requirements
class eligibility(models.Model):
    name = models.CharField(max_length=200) # military status, service eras, etc
    value = models.CharField(max_length=200) # specific value of service_type like 'veteran' or 'WWII'

    class Meta:
        ordering = ['value']

    def __str__(self):
        return self.value

# Financial Info
class financial_info(models.Model):
    org = models.OneToOneField(organization, on_delete=models.CASCADE)
    limit = models.CharField(max_length=200)
    turnaround = models.CharField(max_length=200)

# IJF participation info
class ijf(models.Model):
    org = models.OneToOneField(organization, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=200) # Name of IJF community
    participant_location = models.CharField(max_length=200) # Location of IJF community
    requestinfo = models.CharField(max_length=200) # Yes or No to requesting more info about IJF