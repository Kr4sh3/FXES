from django.contrib import admin

from .models import User, Tweet, SearchTerm

admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(SearchTerm)
