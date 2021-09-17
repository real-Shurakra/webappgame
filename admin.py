from django.contrib import admin

from .models import (account, moon, moonorbit, moontemplate, planet,
                     planetorbit, planettemplate, solarsystem)

admin.site.register(account)

admin.site.register(planettemplate)

admin.site.register(moontemplate)

admin.site.register(solarsystem)

admin.site.register(planet)

admin.site.register(planetorbit)

admin.site.register(moon)

admin.site.register(moonorbit)
