from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'

class About(models.Model):
    title = models.CharField(max_length=10)
    sub_title =models.CharField(max_length=500, help_text="Nima haqidaligini yozing")

    def __str__(self) -> str:
       return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

class service(models.Model):
    #icon = models.ImageField(upload_to='service/%Y/%m/%d')
    title = models.CharField(max_length=10)
    sub_title = models.CharField(max_length=20)

    def __str__(self) -> str:
       return self.title

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'


class contact_us(models.Model):
    title = models.CharField(max_length=10)
   # image = models.ImageField('contact_us/%Y/%m/%d')

    def __str__(self) -> str:
       return self.title

    class Meta:
        verbose_name = 'contact_us'
        verbose_name_plural = 'contact_uses'