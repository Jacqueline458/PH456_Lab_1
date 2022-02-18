# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import scipy
import math
import time
import matplotlib.pyplot as plt
from numpy import random
from numpy.random import Generator, PCG64
from numpy.random import Generator, MT19937
from time import perf_counter
from scipy.stats import chisquare


#Two pseudo-random number generators
rng1 = Generator(PCG64(seed = 456))
rng2 = Generator(MT19937(seed = 456))


#Create two strings of 10000 random numbers between (0,1) using identical seeds
#Time both processes to see which generator is quicker

t1_start = perf_counter()

rand1 = []
for i in range(10000):
    rand1.append(rng1.random())

t1_stop = perf_counter()

print("Time taken for PCG64:", t1_stop-t1_start)


t2_start = perf_counter()

rand2 = []
for i in range(10000):
    rand2.append(rng2.random())

t2_stop = perf_counter()

print("Time taken for Mersenne Twister:", t2_stop-t2_start)

#Sort our two strings of random numbers into numerical order
#Find Frequency
#Run Chi square test on both sets of random numbers

rand1.sort()
rand2.sort()

def freq (rand_string,bin_size):
    string_length = len(rand_string)
    bin_freq = [0]*bin_size
    for i in range(0, string_length):
        for j in range(0,bin_size):
            if string_length[i] > ((j)/bin_size) and string_length[i] < ((j+1)/bin_size) :
                bin_freq[j] = bin_freq[j] + 1
    return bin_freq

freq_PCG64 = freq(rand1,9000)
freq_MT19937 = freq(rand2,9000)

chisquare(freq_PCG64)
chisquare(freq_MT19937)


#Scattergraph to check for sequence correlation for Mersenne Twister
def seq_cor_PCG64 (no_of_values,shift):
    x_axis_values= []
    y_axis_values= []
    random.seed(456)
    for i in range(no_of_values):
        x_axis_values.append(rng1.random())
    for i in range(shift,no_of_values+shift):
        y_axis_values.append(rng1.random())
    plt.scatter(x_axis_values,y_axis_values, s = 1)
    plt.suptitle('Sequential Correlation Plot for PCG64')
    plt.title('No. of Values (no_of_values) = {}, Shift (shift) = {}'.format(no_of_values,shift))
    plt.xlabel('$X_N$')
    plt.ylabel('$X_{N+L}$')

def seq_cor_MT19937 (no_of_values,shift):
    x_axis_values= []
    y_axis_values= []
    random.seed(456)
    for i in range(no_of_values):
        x_axis_values.append(rng2.random())
    for i in range(shift,no_of_values+shift):
        y_axis_values.append(rng2.random())
    plt.scatter(x_axis_values,y_axis_values, s = 1)
    plt.suptitle('Sequential Correlation Plot for Mersenne Twister')
    plt.title('No. of Values (no_of_values) = {}, Shift (shift) = {}'.format(no_of_values,shift))
    plt.xlabel('$X_N$')
    plt.ylabel('$X_{N+L$')

#Partition box simulation
def part_box_PCG64 (no_of_particles,total_time,probability):
    particles_left = [1]*no_of_particles
    particles_R = [-1]*no_of_particles
    no_of_particles_left = []
    no_of_particles_R = []
    random.seed(456)
    for i in range(total_time):
        probability_check = rng1.random()
        selected_particle = rng1.integers(0,no_of_particles)
        if probability_check <= probability:
            particles_left[selected_particle] = (-1)*particles_left[selected_particle]
        else:
            particles_R[selected_particle] = (-1)*particles_R[selected_particle]
        count_left = particles_left.count(1)
        count_R = particles_R.count(1)
        no_of_particles_left.append(count_left)
        no_of_particles_R.append(count_R)
    plt.scatter(range(total_time),no_of_particles_left)
    plt.scatter(range(total_time),no_of_particles_R)
    plt.title('Simulation of Partitioned box experiment - PCG64')
    plt.xlabel('Unit Time')
    plt.ylabel('No. of initial particles on either side of partition')


def part_box_MT19937 (no_of_particles,total_time,probability):
    particles_left = [1]*no_of_particles
    particles_R = [-1]*no_of_particles
    no_of_particles_left = []
    no_of_particles_R = []
    random.seed(456)
    for i in range(total_time):
        probability_check = rng2.random()
        selected_particle = rng2.integers(0,no_of_particles)
        if probability_check <= probability:
            particles_left[selected_particle] = (-1)*particles_left[selected_particle]
        else:
            particles_R[selected_particle] = (-1)*particles_R[selected_particle]
        count_left = particles_left.count(1)
        count_R = particles_R.count(1)
        no_of_particles_left.append(count_left)
        no_of_particles_R.append(count_R)
    plt.scatter(range(total_time),no_of_particles_left)
    plt.scatter(range(total_time),no_of_particles_R)
    plt.title('Simulation of Partitioned box experiment - MT19937')
    plt.xlabel('Unit Time')
    plt.ylabel('No. of initial particles on either side of partition')
