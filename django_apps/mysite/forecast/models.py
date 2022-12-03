from django.db import models


class Forecast(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    index_name = models.CharField(max_length=200)
    cape = models.CharField(max_length=10)
    fwd_return_forecast = models.CharField(max_length=10)
    acf_yield = models.CharField(max_length=10)
    volatility_162W = models.CharField(max_length=10)
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

    def __str__(self):
        return self.ticker
