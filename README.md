# CPCB Downloader
Python script to automatically download individual station data from the [cpcb website](https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data).
Requirements:
1. Python 3.8 and above
2. [Selinium](https://www.selenium.dev/)
3. [Chromedriver](https://chromedriver.chromium.org/downloads) 

Description:
Downloading air pollutant data from the CPCB websit is a tedious task. The user needs to fill forms in differnet stages, which involves human input at various stages.
I have automated the task and the user can downlaod the data from all the stations by simply providing the date range. Moreover, data for individual states can also be downloaded.

Method:
I have used Selinium for web scrapping. The elements on the website are traced as xpath and desired options are clicked to submit the form and download data subsequently.
Since the website redirects to a new page for each download, the previous links become stale.
Hence, I first get the list of all the stations and then specifically download data for each station in a loop by opening the website again.
