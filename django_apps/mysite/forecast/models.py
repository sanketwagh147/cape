from django.db import models


class Forecast(models.Model):
    etf_ticker = models.CharField(max_length=10)
    etf_name = models.CharField(max_length=200)
    index_name = models.CharField(max_length=200)
    cape = models.CharField(max_length=10)
    fwd_return_forecast = models.CharField(max_length=10)
    lower_confidence = models.CharField(max_length=10)
    upper_confidence = models.CharField(max_length=10)
    index_ticker = models.CharField(max_length=10)
    expected_fwd_return_chart = models.CharField(max_length=100)
    long_term_pe_ratio_chart = models.CharField(max_length=100)
    sample_observed_forecast_chart = models.CharField(max_length=100)
    sample_regression_chart = models.CharField(max_length=100)

    def __str__(self):
        return self.etf_ticker
