from rest_framework import serializers
from .models import User, Wishlist, Item, Group, Pair, Membership

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'profile_picture_link', 'email', 'birthday', 'bio']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['title', 'owner']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'item_picture_link', 'item_description', 'wishlist']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name', 'profile_picture_link']

class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = ['first_person', 'second_person', 'group']

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['member', 'group']