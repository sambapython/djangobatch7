from django.contrib.auth.models import User
username=raw_input("enter username:")
password=raw_input("Enter password:")
u1 = User(username=username, password=password)
u1.save()
print u1.username
print u1.password