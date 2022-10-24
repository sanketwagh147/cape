
# Forecasting Future Long-Run Stock Returns with Robert Shiller's Cyclically Adjusted Price-Earnings Ratio (CAPE)

This project is the framework for an application designed to forecast future long-run stock returns with Robert Shiller's Cyclically 
Adjusted Price-Earnings Ratio (CAPE) and present these forecasts visually. 

## Theoretical Basis

In 1998, Robert Shiller and John Campbell published the pathbreaking article “Valuation Ratios and the Long-Run Stock Market Outlook.” 
A follow-up to some of their earlier work on stock market predictability, it established that long-term stock market returns were not 
random walks but, rather, could be forecast by a valuation measure called the “cyclically adjusted price–earnings ratio,” or CAPE ratio. 
Shiller and Campbell calculated the CAPE ratio by dividing a long-term broad-based index of stock market prices and earnings from 1871 
by the average of the last 10 years of earnings per share, with earnings and stock prices measured in real terms. **They regressed 
10-year real stock returns against the CAPE ratio and found that the CAPE ratio is a significant variable that can predict long-run 
stock returns.** The predictability of real stock returns implies that long-term equity returns are mean reverting. In other words, if 
the CAPE ratio is above (below) its long-run average, the model predicts below average (above-average) real stock returns for the next 
10 years.

*Jeremy J. Siegel (2016) The Shiller CAPE Ratio: A New Look, Financial Analysts Journal, 72:3, 41-50, DOI: 10.2469/faj.v72.n3.1*

## Methodology

This application regresses five-year forward stock returns on historical CAPE ratios to measure the degree upon which future stock 
returns are dependent on the level of the CAPE ratio. 

### Formulas

$\text{CAPE} = \frac{\text{Price}}{\text{Ten-year average of inflation adjusted earnings}}$

$\text{Five-Year Forward Return}=\frac{\text{Price Five Years into the Future}}{\text{Current Price}}$

$\text{Regression Forecast}=\beta_{0}+\beta_{1}ln(CAPE)$

### Regression Analysis and Plots

The following plots are an example analysis of the S&P 500 Index as of September 30, 2022. However, the sample ends in September 29, 2017 
because that is the last date in which an ex-post 5-year annualized forward return can be computed. The regression model predicts the 
S&P 500 Index will have an annualized 2.95% with a 95% confidence interval of between -8.10% and 13.90% over the next 5 years based on a 
CAPE ratio of 25.5. 

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/sample_regression_SPX.png)

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/sample_regression_heatmap_SPX.png)

### Forecasts

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/sample_observed_forecast_SPX.png)

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/long_term_pe_ratio_SPX.png)

![S&P 500 INDEX](https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/expected_fwd_return_5y_SPX.png)

### DATA SOURCE

Data to compute regression models comes from Bloomberg Finance LP. However, this data cannot be published due to licensing agreements. 
What is presented by this application is the output of regression models based on the source data. 

## DISCLAIMER

Nothing in this application should be interpreted as investment advice or a recommendation to buy or sell a security. 
No guarantees are made regarding the accuracy or reliability of the data or forecasts. This application is for 
purely research purposes only. Invest at your own risk. 