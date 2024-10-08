from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,password=False):
        if not email:
            raise ValueError('Users must be email')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self,email,password=False):
        if not email:
            raise ValueError('Users must be email')
        
        user = self.create_user(email,password=password)
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=False):
        if not email:
            raise ValueError('Users must be email')
        
        user = self.create_user(email,password=password)
        user.admin = True
        user.driver = False
        user.customer = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    driver = models.BooleanField(default=False)
    staff= models.BooleanField(default=False)
    customer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True


    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    


