from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import datetime

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def random_string():
    return "".join(random.choice(digits) for i in range(26))


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.useraccount.save()


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=26, default=random_string)
    balance = models.IntegerField(default=1_000)

    def __str__(self):
        return '{}'.format(self.user)


class Transaction(models.Model):
    from_account = models.ForeignKey(
        UserAccount, on_delete=models.DO_NOTHING, related_name="from_account")
    to_account = models.ForeignKey(
        UserAccount, on_delete=models.DO_NOTHING, related_name="to_account")
    message = models.TextField(default="")
    
    date = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    accepted = models.BooleanField(default=True) # False on list 7

    def save(self, *args, **kwargs):
        if self.accepted:
            self.to_account.balance += self.amount
            self.to_account.save()
        else:
            self.from_account.balance -= self.amount
            self.from_account.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return ''
