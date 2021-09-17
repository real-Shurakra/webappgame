from django.db import models

class account(models.Model):
    """Account table"""
    userid = models.IntegerField(null=False, blank=False, name='User ID', primary_key=True)
    username = models.CharField(null=False, blank=False, name='Username', max_length=50)
    password = models.CharField(null=False, blank=False, name='Password', max_length=128)
    mailaddress = models.CharField(null=False, blank=False, name='Mail address', max_length=150)
    premium = models.BooleanField(null=False, blank=False, default=False, name='Premium member')
    
class planettemplate(models.Model):
    """Platent templates"""
    maxtemperature = models.IntegerField(null=False,  blank=False, name='Max temperature')
    mintemperature = models.IntegerField(null=False, blank=False, name='Min temperature')
    maxrange = models.IntegerField(null=False, blank=False, name='Max size')
    minrange = models.IntegerField(null=False, blank=False, name='Min size')
    
class moontemplate(models.Model):
    """Moon templates"""
    maxtemperature = models.IntegerField(null=False, blank=False, name='Max temperature')
    mintemperature = models.IntegerField(null=False, blank=False, name='Min temperature')
    maxrange = models.IntegerField(null=False, blank=False, name='Max size')
    minrange = models.IntegerField(null=False, blank=False, name='Min size')
    
class solarsystem(models.Model):
    """Solarsystems"""
    orbits = models.IntegerField(null=False, blank=False, name='Orbits')
    
class planet(models.Model):
    """Planets"""
    planetname = models.CharField(null=True, blank=False, name='Planet name', max_length=32)
    deltatemperature = models.IntegerField(null=False, blank=False, name="Delta Temperature")
    range = models.IntegerField(null=False, blank=False, name='Planet size')
    orbitof = models.ForeignKey(solarsystem, on_delete=models.CASCADE)
    
class planetorbit(models.Model):
    """Planet orbits"""
    range = models.IntegerField(null=False, blank=False, name='Planet orbit size')
    orbitof = models.ForeignKey(planet, on_delete=models.CASCADE)
    
class moon(models.Model):
    """moons"""
    moonname = models.CharField(null=True, blank=False, name='Moon name', max_length=32)
    deltatemperature = models.IntegerField(null=False, blank=False, name="Delta Temperature")
    range = models.IntegerField(null=False, blank=False, name='Moon size')
    orbitof = models.ForeignKey(planet, on_delete=models.CASCADE)
    
class moonorbit(models.Model):
    """Planet orbits"""
    range = models.IntegerField(null=False, blank=False, name='Moon orbit size')
    orbitof = models.ForeignKey(moon, on_delete=models.CASCADE)
    