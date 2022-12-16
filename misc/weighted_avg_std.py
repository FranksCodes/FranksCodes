#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 14:47:08 2022

This program takes a list of values an a list of weights and recturns the unweighted mean, 
weighted mean, standard deviation, and weighted standard deviation using a standard formula that 
includes Bessel's Correction. The formula can be found here: 
    
    https://www.itl.nist.gov/div898/software/dataplot/refman2/ch2/weightsd.pdf


@author: Franks Codes
"""
import statistics
import math


vals = [4.6, 4.5, 4.0, 3.8, 4.2]
weight = [174, 230, 169, 275, 224]

vals_n_weight = [(vals[i], weight[i]) for i in range(0, len(weight))]

def get_wmean(vals, weight):
    weighted_vals = []
    for tup in vals_n_weight:
        weighted_vals.append(round(tup[0]*tup[1]/sum(weight), 3))    
    answer = sum(weighted_vals)
    return answer


def get_wstd(vals, weight):
    numerator = []
    for i in range(0, len(weight)):
        numerator.append(weight[i]*(vals[i]-get_wmean(vals, weight))**2)
    var = sum(numerator)/(((len(weight)-1)*sum(weight))/len(weight))
    wstdev = math.sqrt(var)
    return wstdev
    
print("Values:", vals)
print("Weights:", weight)
print("Unweighted mean:", sum(vals)/len(vals))     
print("Weighted mean:", get_wmean(vals, weight))
print("Standard deviation:", statistics.stdev(vals))
print("Weighted standard deviation", get_wstd(vals, weight))
