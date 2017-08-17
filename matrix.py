# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 09:54:07 2017

@author: stella
"""
import numpy as np
import matplotlib.pyplot as plt
import h5py
from scipy.optimize import curve_fit

## exposure times (better to choose manually)
# exp_time=[0.1,0.2,0.5]

## intensities
# for exposrue times 0.1 & 0.2
intensities=['320000','100000','032000','010000','003200','001000','000320','000100']
# for exposure time 0.5
#intensities=['100000','032000','010000','003200','001000','000320','000100']
#datasheet_ints=[0.39,0.1,0.039,0.008,0.00312,0.0008,0.000312,0.00008]
datasheet_ints=[0.35,0.098,0.0343,0.007,0.00245,0.000784,0.0002401,0.000098] #for wavelengths 400-600
other_filters=['sharif']

filter_value=[]
count=[]
adjfilter=[]



exp_time='0p1'
final_array=np.empty((3,2048,2060))
for ypixel in range(2048):
    for xpixel in range(2060):
        for i in range(len(intensities)):
            """
            Get mean value of the pixel at each filter value and append to counts
            """
            # lab filters
            fid=h5py.File('/media/stella/F0B427B9B42780E8/Stella/exp_time%s/intensity_0p%s/pco_000001.h5' %(exp_time,intensities[i]),'r')
            data=fid['/entry/data']
            mean_frame=np.mean(data, axis=0)
            filter_value.append(datasheet_ints[i])
            count.append(mean_frame[ypixel, xpixel])
            
            sharif_filters=intensities[:-1]
        for j in range(len(sharif_filters)):
               fid=h5py.File('/media/stella/F0B427B9B42780E8/Stella/exp_time%s/sharif/intensity_0p%s/pco_000001.h5' %(exp_time,intensities[j]),'r')
               data=fid['/entry/data']
               mean_frame=np.mean(data, axis=0)
               filter_value.append(datasheet_ints[j]*0.2)
               count.append(mean_frame[ypixel, xpixel])
            
        # dark frame
        fid=h5py.File('/media/stella/F0B427B9B42780E8/Stella/exp_time%s/dark/pco_000001.h5'%exp_time,'r')
        data=fid['/entry/data']
        mean_frame=np.mean(data, axis=0)
        filter_value.append(0.0)
        count.append(mean_frame[ypixel, xpixel])
        
        """
        Find linear fit of the pixel and append gradient & intercept to a 2D matrix
        """
        fit=np.polyfit(filter_value, count,1)
        #fit=fitx*line[0]+line[1] #equation for fit
        line=np.poly1d(fit) #gives function for line of best fit
        straight_coeff=np.corrcoef(line(filter_value), count)[0,1]
        final_array[0,ypixel,xpixel]=fit[1] #intercept
        final_array[1,ypixel,xpixel]=fit[0] #gradient
        final_array[2,ypixel,xpixel]=straight_coeff #correlation coefficient

np.save('pco_intensity_response', final_array)
            


