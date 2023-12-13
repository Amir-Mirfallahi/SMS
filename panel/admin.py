from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from admin_interface.admin import Theme
from django.shortcuts import redirect
from django.urls import reverse

from .models import Profile, Student, Teacher, Class, Subject, TaughtClass
from .forms import CustomUserRegisterForm

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Theme)


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    add_form = CustomUserRegisterForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email')}),
        ('دسترسی ها', {'fields': ('is_superuser',)}),
        ('تاریخ های مهم', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2"),
        }),
        ("اطلاعات شخصی", {
            "classes": ("wide",),
            "fields": ('first_name', 'last_name'),
        }),
    )
    # region personalization
    # If you want to customize labels for individual fields in the model, you can use verbose_name
    User._meta.get_field('username').verbose_name = 'کدملی'
    User._meta.get_field('password').verbose_name = 'رمز عبور'
    User._meta.get_field('first_name').verbose_name = 'نام'
    User._meta.get_field('last_name').verbose_name = 'نام خانوادگی'
    User._meta.get_field('email').verbose_name = 'پست الکترونیکی'
    User._meta.get_field('is_superuser').verbose_name = 'آیا مدیر است'
    User._meta.get_field('last_login').verbose_name = 'آخرین ورود'
    User._meta.get_field('date_joined').verbose_name = 'تاریخ ثبت'
    User._meta.verbose_name = 'کاربر'
    User._meta.verbose_name_plural = 'کاربران'

    # endregion
    # def response_to_action(self, request, obj, post_url_continue, action):

    def response_add(self, request, obj, post_url_continue=None):
        role = request.POST.get('profile-0-role')

        # Redirect based on the user's role
        if role == Profile.STUDENT:
            return redirect(reverse('admin:panel_student_add') + f'?profile={obj.id}')
        elif role == Profile.TEACHER:
            return redirect(reverse('admin:panel_teacher_add') + f'?profile={obj.id}')

        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj, post_url_continue=None):
        role = request.POST.get('profile-0-role')

        # Redirect based on the user's role
        if role == Profile.STUDENT:
            return redirect(reverse('admin:panel_student_add') + f'?profile={obj.id}')
        elif role == Profile.TEACHER:
            return redirect(reverse('admin:panel_teacher_add') + f'?profile={obj.id}')
        return super().response_change(request, obj)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(TaughtClass)
class TaughtClassAdmin(admin.ModelAdmin):
    pass
