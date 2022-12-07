from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Index (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Backtext (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Backtext2 (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Posts(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Posts2(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Doctor1(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class News1(models.Model):
    title = models.CharField(max_length=100)
    datetime = models.TextField()
    description = models.TextField()
    add = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class News2(models.Model):
    title = models.CharField(max_length=100)
    datetime = models.TextField()
    description = models.TextField()
    add = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class News3(models.Model):
    title = models.CharField(max_length=100)
    datetime = models.TextField()
    description = models.TextField()
    add = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Kontact(models.Model):
    title = models.CharField(max_length=100)
    adress = models.TextField()
    phonenumber = models.TextField()
    mainphone = models.TextField()
    email = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Back2(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Help(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.TextField()

class Bodrost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

#СТОМАТОЛОГИЯ------------------------------------------------------------------------------------------------
class Dentist (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class State(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class PostsSTL(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Posts2STL(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class Doctor1STL(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title


#ХИРУРГИЯ------------------------------------------------------------------------------------------------------
class Surgeon (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Pediatrician (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Gynecologist (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
