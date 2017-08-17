# pco_intensity_response

Using a torch and neutral density filters, the relationship between theoretical intensity and detected PCO intensity was analysed.

ND filters used:

ND505A, ND510A, ND520A, ND530A & LEE filters Neutral Density 2 stop filter.

We collected 100 frames on the PCO at exposure times of 0.1s, 0.2s & 0.5s with many conbinations of filters

# intensity_data.py

This python script analyses the data for a specific exposure time and plots the fit of the photon counts agaianst filter tranmission values.

# matrix.py

Analyses the intensity data and saves a 3x2048x2060 matrix containing the intercept & slope of count/filter value line of best fit for each pixel, and the correlation coefficient of such fits.
