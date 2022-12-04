# NRCapital

NRCapital is a financial application for displaying statistically-derived equity and bond exchanged-traded funds (ETFs) and common stock expected returns. These expected returns can be used as inputs in securities analysis and portfolio optimization. Only ETFs and common stocks with sufficient data and statistically significant regression model results are included in the application. Please refer to the [documentation](https://nr-capital-management.gitbook.io/nrcapital/) for more details. 

## Table of Contents

 - [Quick Start](#Quick-Start)
 - [Forecast Tables](#Forecast-Tables)
 - [Forecast Dashboards](#Forecast-Dashboards)
 - [Forecast Charts](#Forecast-Charts)

## Quick Start

These instructions work on Windows 10. For any other system, simply do the equivalent commands on your system. These instructions assume the user is starting from nothing and so some steps may be redundant. Feel free to skip any step that has already been satisfied. After install, only steps 7-9 in Anaconda Prompt need to be used to run the application. If you have any issues installing or using the application, submit your issue to the project's GitHub [Issues](https://github.com/nathanramoscfa/nrcapital/issues) page. 

 1. Install the [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) package manager on your computer. 
 
 2. Open Anaconda Prompt and create a new environment with the following command: <br>
	 `conda create -n nrcapital python=3.10`
	
 3. Activate the new environment.<br>
	 `conda activate nrcapital`
	 
 4. If you don't have a folder for your projects, create one anywhere on your computer. In Anaconda Prompt, navigate to the project folder where you want to store project files.<br>
	 `cd C:\Users\JohnDoe\Projects`
	 
 5. Clone the NRCapital project repository into your environment. This downloads the project's files to your environment. <br>
	 `git clone https://github.com/nathanramoscfa/nrcapital.git`

 6. Install the project's dependencies into your environment. <br>
	 `python setup.py install`

 7. Navigate to folder containing the application's `manage.py` file. <br>
	 `cd C:\Users\JohnDoe\Projects\nrcapital\django_apps\mysite`

 8. Run the project's server. <br>
	 `python manage.py runserver`

 9. Open a web browser like Google Chrome and visit [127.0.0.1:8000/forecast/](127.0.0.1:8000/forecast/). 

The browser should then load the application's home page. See [Functions](/o/rvIrvgj6CnY7ZQwxkkP8/s/SKjgOWTTLSJxR5P9qKTd/functions) for a more detailed explanation of how to use the application. 
 
 ![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FSKjgOWTTLSJxR5P9qKTd%2Fuploads%2FQkmpI2Qq8bifNIdBzjeD%2Fimage.png?alt=media&token=c6f2afdb-e056-4935-b1a5-48b5923c6532)

## Forecast Tables

The application provides a sortable and searchable table of forecasts with 95% confidence intervals for equity ETFs, bond ETFs, and common stocks. Clicking on any row will open a dashboard of statistical plots specific to that ticker which shows the forecast in detail. 

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FSKjgOWTTLSJxR5P9qKTd%2Fuploads%2F5Q0Et5FHteo1EuSAZKiK%2Fimage.png?alt=media&token=7f03e6e5-06dc-4953-a841-e3ffaec56756)

## Forecast Dashboards

The application provides a dashboard of statistical plots for each ticker when the user clicks on any row in the forecast tables.  Clicking on any chart will expand it to full screen. 

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FSKjgOWTTLSJxR5P9qKTd%2Fuploads%2FSb4YGd08mK99n5CXJJ2n%2Fimage.png?alt=media&token=ae0e9f7c-2b6c-4a0a-b1f8-40a2ac5d6f09)

## Forecast Charts

The application provides statistical plots showing the results of the regression analysis behind the applications expected return forecasts. 

### Regression Plot

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FSKjgOWTTLSJxR5P9qKTd%2Fuploads%2Fyi0u0oS0ZBMLrK6aVwsT%2Fsample_regression_NDQ.jpg?alt=media&token=e992e025-6757-45ae-a680-a73f028811e4)

### Forecast Plots

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FSKjgOWTTLSJxR5P9qKTd%2Fuploads%2FyE254JXpQYEqxlxkJaeM%2Fsample_observed_forecast_NDQ.jpg?alt=media&token=e4efee77-362f-4c03-94cf-5cc8ba790df4)
![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FSKjgOWTTLSJxR5P9qKTd%2Fuploads%2Farxdad2idq1zDoc8jEuR%2Fexpected_fwd_return_NDQ.jpg?alt=media&token=0b5ce2d8-ff73-457d-8d4e-fbeb0c6dea87)

### CAPE Plot

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FSKjgOWTTLSJxR5P9qKTd%2Fuploads%2FrBKbFHvihZRV2K3gUtir%2Flong_term_pe_ratio_NDQ.jpg?alt=media&token=7bea9db5-b93a-49d1-991e-f1077e2e8bc6)

## Disclaimer

Nothing in this application should be interpreted as investment advice or a recommendation to buy or sell a security. No guarantees are made regarding the accuracy or reliability of the data or forecasts. We accept no liability for any actions made based on any data or forecasts from this application. This application is for purely research purposes only. Invest at your own risk.