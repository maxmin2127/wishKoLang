from django.contrib import admin

# Register your models here.
from .models import User, Wishlist, Item, Group, Pair, Membership

admin.site.register([User, Wishlist, Item, Group, Pair, Membership])