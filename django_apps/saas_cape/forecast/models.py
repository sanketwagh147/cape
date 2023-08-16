from django.db import models
from django.contrib.auth.models import User


class Forecast(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    index_name = models.CharField(max_length=200)
    cape = models.CharField(max_length=10)
    fwd_return_forecast = models.CharField(max_length=10)
    acf_yield = models.CharField(max_length=10)
    volatility = models.CharField(max_length=10)
    yield_vol_ratio = models.CharField(max_length=10)
    bond_pe_ratio = models.CharField(max_length=10)
    lower_confidence = models.CharField(max_length=10)
    upper_confidence = models.CharField(max_length=10)
    f_pvalue = models.CharField(max_length=100, default='')
    index_ticker = models.CharField(max_length=10)
    expected_fwd_return_chart = models.CharField(max_length=100)
    long_term_pe_ratio_chart = models.CharField(max_length=100)
    sample_observed_forecast_chart = models.CharField(max_length=100)
    sample_regression_chart = models.CharField(max_length=100)
    security_type = models.CharField(max_length=100)
    outlier_bool = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticker


class Subscription(models.Model):
    FREE = 'free'
    MONTHLY = 'monthly'
    SEMI_ANNUAL = 'semi_annual'
    ANNUAL = 'annual'

    PLAN_CHOICES = [
        (FREE, 'Free'),
        (MONTHLY, 'Monthly'),
        (SEMI_ANNUAL, 'Semi-Annual'),
        (ANNUAL, 'Annual'),
    ]

    name = models.CharField(choices=PLAN_CHOICES, max_length=12)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trial_ends_at = models.DateField(null=True, blank=True)
    # Other fields like billing information, etc.
