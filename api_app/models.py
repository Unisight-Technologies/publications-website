from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    clgID = models.BigIntegerField(blank=False,null=False) #doubt
    website = models.URLField(max_length=200,**options)

class Departments(models.Model):
    name = models.CharField(max_length=100)
    deptID = models.BigIntegerField(blank=False,null=False)

class Author(models,model):
    name = model.CharField(max_length=100)
    userID = models.BigIntegerField(blank=False,null=False)
    ORCid = models.UUIDField(
          primary_key = True,
          default = uuid.uuid4,
          editable = False)
    scopusID= models.UUIDField(
          primary_key = True,
          default = uuid.uuid4,
          editable = False)
    bio = models.CharField(max_length=1000)
    affiliation = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    phoneno = models.BigIntegerField(blank=True,null=True)
    weblinks = models.URLField(max_length=200,**options)
    designation = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = 



class Paper(models.Model):
    title = models.CharField(max_length=100)
    DOI = models.UUIDField(
          primary_key = True,
          default = uuid.uuid4,
          editable = False)
    pri_author = models.CharField(max_length=100)
    co_authors
    volume
    issue
    citation = imodels.AutoField(primary_key=True, **options)
    field = models.CharField(max_length=100)
    publication_date = models.TimeField(auto_now=False, auto_now_add=False, **options)
    publish_name = models.CharField(max_length=100)
    abstract = models.CharField(max_length=1000)
    tags =
