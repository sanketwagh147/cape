from django.contrib.auth.models import AbstractUser
from django.db import models
import stripe


class User(AbstractUser):
    # region			  -----Informations-----
    stripe_subscription_id = models.CharField(
        help_text="This field will be populated automatically "
                  "after the first transaction",
        verbose_name="Stripe Subscription ID",
        max_length=255,
        blank=True,
        null=True
    )

    stripe_customer_id = models.CharField(
        help_text="This field will be populated automatically "
                  "after the first transaction",
        verbose_name="Stripe Customer ID",
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    # endregion


    # region			      -----Meta-----
    class Meta(object):
        verbose_name_plural = "Users"
        verbose_name = "User"
    # endregion

    
    # region			    -----Functions-----
    def get_subscription_status(self)\
        -> str:
        if self.stripe_subscription_id:
            return stripe.Subscription\
                .retrieve(
                    id=self.stripe_subscription_id
                ).status
        
        return "unpaid"
    

    def __str__(self)\
        -> str:
        return self.email
    # endregion