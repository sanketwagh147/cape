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


class Charts(models.Model):
    index_ticker = models.CharField(max_length=10)
    expected_fwd_return = models.FilePathField(path="static/forecast/images/")
    long_term_pe_ratio = models.FilePathField(path="static/forecast/images/")
    sample_observed_forecast = models.FilePathField(path="static/forecast/images/")
    sample_regression = models.FilePathField(path="static/forecast/images/")
