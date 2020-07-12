from django.contrib import admin
from .models import User,FollowUser,FriendRequest

from rangefilter.filter import DateTimeRangeFilter


# Register your models here.
@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
        'gender',
        'bio',
        'is_staff',
        'is_active',
        'is_superuser',
        'date_joined',
        'last_login',
        'last_activate_time'
    ]
    list_filter = [
        'username',
        'gender',
        'email',
        ('date_joined', DateTimeRangeFilter),
        'last_login',
        'last_activate_time'
    ]


@admin.register(FollowUser)
class FollowUserAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'follow_request_user',
        'follow_id',
        'follow_start_time'

    ]

    def follow_request_user(self,user):
        pass

    def follow_response_user(self,user):
        pass



@admin.register(FriendRequest)
class FriendsRequestAdmin(admin.ModelAdmin):
    list_display = [
        'request_id',
        'response_id',
        'status'
    ]
