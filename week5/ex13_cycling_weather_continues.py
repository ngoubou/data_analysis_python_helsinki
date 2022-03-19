#!/usr/bin/env python3



def cycling_weather_continues(station):
    return ((0.0, 0.0, 0.0), 0.0)
    
def main():
    return

if __name__ == "__main__":
    main()

# Write function cycling_weather_continues that tries to explain with linear regression the variable of a cycling measuring station's counts
# using the weather data from corresponding day. 
# The function should take the name of a (cycling) measuring station as a parameter and return the regression coefficients and the score. 
# In more detail:

# Read the weather data set from the src folder. Read the cycling data set from folder src and restrict it to year 2017. 
# Further, get the sums of cycling counts for each day. Merge the two datasets by the year, month, and day. 
# Note that for the above you need only small additions to the solution of exercise cycling_weather. 
# After this, use forward fill to fill the missing values.

# In the linear regression use as explanatory variables the following columns 
# 'Precipitation amount (mm)', 'Snow depth (cm)', and 'Air temperature (degC)'. 
# Explain the variable (measuring station), whose name is given as a parameter to the function cycling_weather_continues. 
# Fit also the intercept. The function should return a pair, 
# whose first element is the regression coefficients and the second element is the score. 
# Above, you may need to use the method reset_index (its counterpart is the method set_index).

# The output from the main function should be in the following form:

# Measuring station: x
# Regression coefficient for variable 'precipitation': x.x
# Regression coefficient for variable 'snow depth': x.x
# Regression coefficient for variable 'temperature': x.x
# Score: x.xx

# Use precision of one decimal for regression coefficients, and precision of two decimals for the score. 
# In the main function test you solution using some measuring station, for example Baana.