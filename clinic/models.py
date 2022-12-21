from django.db import models
from django.core.validators import FileExtensionValidator
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


class HelpU(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    description = models.TextField()





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

class Backtext2stl(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Postsstl(models.Model):
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

class Newsstl(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

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

class StateH(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Backtext2H(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class PostsH(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Posts2H(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class Doctor1H(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class NewsH(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title






#педиатория---------------------------------------------------------------------------------------------------------------
class Pediatrician (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class StateP(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Backtext2P(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class PostsP(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Posts2P(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class Doctor1P(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class NewsP(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title


#ГИНЕКОЛОГИЯ--------------------------------------------------------------------------------------------------------------
class Gynecologist (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class StateG(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Backtext2G(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class PostsG(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Posts2G(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class Doctor1G(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='')
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

class NewsG(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

#ОНАС --------------------------------------------------------------------------------------------------------------------------

class AboutAs (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AboutAsState (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

    def __str__(self):
        return self.title

