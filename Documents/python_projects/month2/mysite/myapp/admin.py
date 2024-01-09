from django.contrib import admin

from myapp.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "brand", "short_description", "price"]
    list_display_links = ["id", "name"]
    def short_description(self, obj:Car):
        if len(obj.description) > 48:
            return obj.description[:48] + "..."
        else:
            return obj.description

admin.site.register(Car, CarAdmin)