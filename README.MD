# NDVR Quant engineer exercise

As you know, NDVR was born in Boston, home of the world-famous lobster roll. 

The cuisine of Boston is well known for its seafood, with lobster being the crown jewel of fine dining. 
Lesser known is that lobster was not always considered a delicacy. 
In the colonial era, it was dirt-cheap because they were so copious, lobsters were routinely fed to prisoners, 
apprentices, slaves, and children. In Massachusetts, some servants allegedly sought to avoid lobster-heavy 
diets by including stipulations in their contracts that they would only be served the shellfish twice a week.

Just as dishes, software will also benefit a whole lot from fine ingredients, 
careful preparation, and neat serving. We invite you to cook up a new feature for us and serve it 
in a pull request that **you’d be comfortable merging into your production** branch. 
The name of the dish is: 

    “Simulating future prices of a stock based on historical data”. 

The recipe is:

1. Setting up the project 
   1. Create a new GitHub (or similar) repository named `qe_hw_{your name}`
   2. Import the supplied project. The projects dependencies are maintained by 
Pipenv - the `pipenv update` command should get you started.
Python version is set to 3.8 - feel free to use an arbitrary version.
   3. Create a feature branch and work in that, separating your progress into commits.
2. Explore the project. It only has one .py file, `historic_prices.py`, which exposes a method
to fetch prices from Yahoo finance. This could be modified as well in the homework, if needed.
3. Add a new feature to project asset prices into the future for equity tickers. 
   - Extract historical price movements: Calculate a list of month-over-month price changes
from the available historical data using close prices.
   - Create a method to generate a `scenario`: A scenario is a list of monthly prices 20 years into the future: 
start with the current price and for each month apply a month-over-month price change 
that is randomly selected from the data set generated in the previous task.
   - Generate 1000 scenarios and return the one with the highest closing price 
at the end of the very last month. Also log the lowest as well as the median ending value.
4. Create a REST API endpoint which generates scenarios and returns the mentioned metrics - Use your favourite
Python REST library, if there is one.
The parameters of this endpoint should be:
   1. The ticker symbol
   2. Number of months
   3. Number of scenarios generated.

Notes: 
- Please include a short description on the work done. 
- Make sure to also include notes on how to run the application.
