

# Forecasting Future Long-Run Stock Returns with Robert Shiller's Cyclically Adjusted Price-Earnings Ratio (CAPE)

This application is designed to present forecasts of future long-run stock returns using Robert Shiller's Cyclically 
Adjusted Price-Earnings Ratio (CAPE) and present these forecasts visually. 

## Theoretical Basis

In 1998, Robert Shiller and John Campbell published the pathbreaking article “Valuation Ratios and the Long-Run Stock Market Outlook.” A follow-up to some of their earlier work on stock market predictability, it established that long-term stock market returns were not random walks but, rather, could be forecast by a valuation measure called the “cyclically adjusted price–earnings ratio,” or CAPE ratio. Shiller and Campbell calculated the CAPE ratio by dividing a long-term broad-based index of stock market prices and earnings from 1871 by the average of the last 10 years of earnings per share, with earnings and stock prices measured in real terms. **They regressed 10-year real stock returns against the CAPE ratio and found that the CAPE ratio is a significant variable that can predict long-run stock returns.** The predictability of real stock returns implies that long-term equity returns are mean reverting. In other words, if the CAPE ratio is above (below) its long-run average, the model predicts below average (above-average) real stock returns for the next 10 years.

*Jeremy J. Siegel (2016) The Shiller CAPE Ratio: A New Look, Financial Analysts Journal, 72:3, 41-50, DOI: 10.2469/faj.v72.n3.1*

## Methodology

This application regresses forward five-year annualized stock returns (referred to in this documentation as "forward return") on historical CAPE ratios to measure the degree upon which future stock returns are dependent on the level of the CAPE ratio. 

### Formulas

$\Large\text{CAPE} = \frac{\text{Price}}{\text{Inflation adjusted earnings ten-year average}}$

$\Large\text{Forward five-year annualized return}=\frac{\text{Price five years into the future}}{\text{Current price}}$

$\Large\text{Forward five-year annualized return forecast}=\beta_{0}+\beta_{1}ln(CAPE)$


### Regression Model

The following is an example analysis of the S&P 500 Index as of September 30, 2022. The observation sample ends in September 29, 2017 because that is the last date in which an ex-post forward 5-year return can be computed. Therefore, forward returns computed by the regression model after the date the sample ends on September 29, 2017 is considered an out-of-sample forecast. 

The plot below shows the OLS regression model output where the forward return was regressed against the monthly natural log of the S&P 500's CAPE ratio from September 30, 1994 to September 29, 2017. The adjusted R-squared was high at 46.7%. The p-value of the F-statistic at 1.43e-60 is extremely low and much below an alpha of 0.05 at the 95% confidence level indicating the model is statistically significant. The regression model coefficients' p-values are both also very low (showing 0.000 under P>|t| column), indicating both coefficients are statistically significant. The regression model was made more robust by adjusting the covariance matrix and standard errors for heteroscedasticity and autocorrelation effects utilizing the Newey-West method. Accordingly, the variation in the S&P 500's CAPE ratio appears to predict about 46.7% of the S&P 500's forward 5-year return with 95% confidence. Knowing this, predictions of future S&P 500 returns can be reliably made with the CAPE ratio assuming the regression model is correctly specified and unbiased. 

<img src="https://raw.githubusercontent.com/nathanramoscfa/cape/main/django_apps/mysite/forecast/static/forecast/images/regression_results_SPX.png" alt="ols_results" width="800"/>

### Regression Plots

The plot below shows the observed CAPE ratio versus forward return scatterplot (yellow dots) along with the regression model's forecast of the current forward return based on the last observed CAPE ratio of 25.5 (solid cyan star). The regression model plot below predicts the S&P 500 Index will have an annualized 2.95% return (solid cyan star) with a 95% confidence interval (dashed red lines) of between -8.10% and 13.90% over the next 5 years based on the current CAPE ratio of 25.5 (solid cyan star). Most portfolio managers would probably not like earning 2.95% annualized return over the next 5 years which might cause them to underweight the S&P 500 index in favor of higher expected returns elsewhere. However, the plot shows that actual observed 5-year returns when the S&P 500's CAPE ratio is between 25 and 26 seem to show anything from approximately 4 to 11% which is higher than forecasted by the regression model. 

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/django_apps/mysite/forecast/static/forecast/images/sample_regression_SPX.jpg)

This plot shows the observed forward return (solid white line) for the S&P 500. The regression model's forecast of the forward return (solid red line) is shown along with 95% confidence intervals (dashed red lines). Observations of forward return end 5 years from the present (as of September 30, 2022) in September 29, 2017. After this date, the plot shows the out-of-sample forecast of forward return made by the regression model (solid green line) along with 95% confidence intervals for out-of-sample forecast period (dashed green lines). The out-of-sample forecast ends at the current forecast of 2.95%. The average forward return observation for the S&P 500 is also shown (solid cyan horizontal line) equaling 6.65%. Accordingly, the regression models seems to predict below-average returns for the S&P 500 over the next 5 years (2022-2027). This might lead a portfolio manager to underweight the S&P 500. This plot also shows that the best time to invest in the S&P 500 was from 1995-2000 (beginning of the plot) and the worst time was 2004-2009. Spikes in the forward return occurred in 2002, 2009, and 2017...2002 and 2008 coincide with a period of high volatility, low CAPE valuation ratio, and negative investor sentiment. This observation suggests that the best times to overweight the S&P 500 index is when volatility is at its highest, CAPE ratio is at its lowest, and investor sentiment at its most negative. However, 2017 seems to be an anomaly as the plot shows the observed forward return from 2017-2022 touches the "In-Sample Upper 95%" confidence bound suggesting that this period's high return statistically only happens 5% or less of the time. 

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/django_apps/mysite/forecast/static/forecast/images/sample_observed_forecast_SPX.jpg)

This plot shows the CAPE ratio of the S&P 500 index from 1994 to 2022 (solid white line) and then displays a SARIMAX 10-year forecast of the expected CAPE ratio (dashed white line) from 2022-2032. The average CAPE ratio is shown (solid cyan) at 23.13 along with +/- 1 and 2 standard deviations (dashed red and green lines). The current CAPE ratio is 25.5 which is above average implying the S&P 500's valuation is historically high. However, as shown in the plot, the S&P 500's valuation level is rapidly adjusting downwards, with expected returns increasing as it does so. The SARIMAX forecasts the CAPE ratio to be declining towards the long-term average with a cone of uncertainty (shaded white) that suggests it could overshoot to below the long-term average. The CAPE ratio crossed above the +2 standard deviation suggesting the S&P 500's valuation was statistically high, happening 5% or less of the time. This might lead a portfolio manager to underweight the S&P 500 in their portfolio. The lowest the CAPE ratio ever reached was in 2009 during the aftermath of the 2007-2008 global financial crisis. 

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/django_apps/mysite/forecast/static/forecast/images/long_term_pe_ratio_SPX.jpg)

This plot show the forward return (solid white) from 1994 to 2022, SARIMAX 10-year forecast (shaded white) from 2022 to 2032, average forward return (solid cyan), and standard deviations +/- 1 and 2 (dashed green and red). Concurrent with expected declines in the CAPE ratio shown above, the forward return would be expected to rise as shown by the SARIMAX forecast below. 

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/django_apps/mysite/forecast/static/forecast/images/expected_fwd_return_5y_SPX.jpg)

### Data Source

Data to compute regression models comes from Bloomberg Finance LP. However, this data cannot be published due to licensing agreements. What is presented by this application is the output of regression models based on the source data. 

## Disclaimer

Nothing in this application should be interpreted as investment advice or a recommendation to buy or sell a security. No guarantees are made regarding the accuracy or reliability of the data or forecasts. This application is for purely research purposes only. Invest at your own risk. 