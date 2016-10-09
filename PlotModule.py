#! /usr/bin/env python

"""For plotting all the data from the acceleration file of pocketlab."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import kinematics as kin

def plotDriftCorrected(coord,a,b,c,d,filename):
    #getting acceleration values
    df = pd.read_csv(filename)
    t = df['Time']
    #vDevice = kin.zero(df[' Speed (m/2)'],0,43)
    #use zero function in module to zero each acceleration;
    #also multiply by 9.81 to changes units from g to m/s^2

    #The data set was taken with a 2s (43 interval) calibration period
    #such that i can say a(0)=0, v(0)=0, x(0)=0

    a_x = kin.zero(df[' Acceleration(m/s²)'],a,b)
    a_y = kin.zero(df[' Acceleration(m/s²).1'],a,b)
    a_z = kin.zero(df[' Acceleration(m/s²).2'],a,b)



    slopeX = (a_x[d]-a_x[c])/(t[d]-t[c])
    slopeY = (a_y[d]-a_y[c])/(t[d]-t[c])
    slopeZ = (a_z[d]-a_z[c])/(t[d]-t[c])

    for i in range(c,d): 
    	a_x[i] -= slopeX*(t[i]-t[c])
    	a_y[i] -= slopeY*(t[i]-t[c])
    	a_z[i] -= slopeZ*(t[i]-t[c])

    v_x = kin.zero(kin.integral(t, a_x),a,b)
    v_y = kin.zero(kin.integral(t, a_y),a,b)
    v_z = kin.zero(kin.integral(t, a_z),a,b)

    x = kin.zero(kin.integral(t, v_x),a,b)
    y = kin.zero(kin.integral(t, v_y),a,b)
    z = kin.zero(kin.integral(t, v_z),a,b)

    if (coord == 'x'):
        plt.plot(t, a_x)
        plt.xlabel('t')
        plt.ylabel('a_x (m/s^2)')
        plt.title('Measured X Acceleration')
        plt.show()

        plt.plot(t, v_x)
        plt.xlabel('t')
        plt.ylabel('v_x (m/s)')
        plt.title('Calculated X Velocity')
        plt.show()

        plt.plot(t, x)
        plt.xlabel('t')
        plt.ylabel('x (m)')
        plt.title('Calculated X Position')
        plt.show()
    elif (coord == 'y'):
        plt.plot(t, a_y)
        plt.xlabel('t')
        plt.ylabel('a_y (m/s^2)')
        plt.title('Measured Y Acceleration')
        plt.show()

        plt.plot(t, v_y)
        plt.xlabel('t')
        plt.ylabel('v_y (m/s)')
        plt.title('Calculated Y Velocity')
        plt.show()

        plt.plot(t, y)
        plt.xlabel('t')
        plt.ylabel('y (m)')
        plt.title('Calculated Y Position')
        plt.show()
    elif (coord == 'z'):
        plt.plot(t, a_z)
        plt.xlabel('t')
        plt.ylabel('a_z (m/s^2)')
        plt.title('Measured Z Acceleration')
        plt.show()

        plt.plot(t, v_z)
        plt.xlabel('t')
        plt.ylabel('v_z (m/s)')
        plt.title('Calculated Z Velocity')
        plt.show()

        plt.plot(t, z)
        plt.xlabel('t')
        plt.ylabel('z (m)')
        plt.title('Calculated Z Position')
        plt.show()

def plotZero(coord,a,b,filename):
    #getting acceleration values
    df = pd.read_csv(filename)
    t = df['Time']
    #vDevice = kin.zero(df[' Speed (m/2)'],0,43)
    #use zero function in module to zero each acceleration;
    #also multiply by 9.81 to changes units from g to m/s^2

    #The data set was taken with a 2s (43 interval) calibration period
    #such that i can say a(0)=0, v(0)=0, x(0)=0

    a_x = kin.zero(df[' Acceleration(m/s²)'],a,b)
    a_y = kin.zero(df[' Acceleration(m/s²).1'],a,b)
    a_z = kin.zero(df[' Acceleration(m/s²).2'],a,b)

    v_x = kin.zero(kin.integral(t, a_x),a,b)
    v_y = kin.zero(kin.integral(t, a_y),a,b)
    v_z = kin.zero(kin.integral(t, a_z),a,b)

    x = kin.zero(kin.integral(t, v_x),a,b)
    y = kin.zero(kin.integral(t, v_y),a,b)
    z = kin.zero(kin.integral(t, v_z),a,b)

    if (coord == 'x'):
        plt.plot(t, a_x)
        plt.xlabel('t')
        plt.ylabel('a_x (m/s^2)')
        plt.title('Measured X Acceleration')
        plt.show()

        plt.plot(t, v_x)
        plt.xlabel('t')
        plt.ylabel('v_x (m/s)')
        plt.title('Calculated X Velocity')
        plt.show()

        plt.plot(t, x)
        plt.xlabel('t')
        plt.ylabel('x (m)')
        plt.title('Calculated X Position')
        plt.show()
    elif (coord == 'y'):
        plt.plot(t, a_y)
        plt.xlabel('t')
        plt.ylabel('a_y (m/s^2)')
        plt.title('Measured Y Acceleration')
        plt.show()

        plt.plot(t, v_y)
        plt.xlabel('t')
        plt.ylabel('v_y (m/s)')
        plt.title('Calculated Y Velocity')
        plt.show()

        plt.plot(t, y)
        plt.xlabel('t')
        plt.ylabel('y (m)')
        plt.title('Calculated Y Position')
        plt.show()
    elif (coord == 'z'):
        plt.plot(t, a_z)
        plt.xlabel('t')
        plt.ylabel('a_z (m/s^2)')
        plt.title('Measured Z Acceleration')
        plt.show()

        plt.plot(t, v_z)
        plt.xlabel('t')
        plt.ylabel('v_z (m/s)')
        plt.title('Calculated Z Velocity')
        plt.show()

        plt.plot(t, z)
        plt.xlabel('t')
        plt.ylabel('z (m)')
        plt.title('Calculated Z Position')
        plt.show()

def plotRaw(coord,filename):
    #getting acceleration values
    df = pd.read_csv(filename)
    t = df['Time']
    #vDevice = kin.zero(df[' Speed (m/2)'],0,43)
    #use zero function in module to zero each acceleration;
    #also multiply by 9.81 to changes units from g to m/s^2

    #The data set was taken with a 2s (43 interval) calibration period
    #such that i can say a(0)=0, v(0)=0, x(0)=0

    a_x = df[' Acceleration(m/s²)']
    a_y = df[' Acceleration(m/s²).1']
    a_z = df[' Acceleration(m/s²).2']

    v_x = kin.integral(t, a_x)
    v_y = kin.integral(t, a_y)
    v_z = kin.integral(t, a_z)

    x = kin.integral(t, v_x)
    y = kin.integral(t, v_y)
    z = kin.integral(t, v_z)

    if (coord == 'x'):
        plt.plot(t, a_x)
        plt.xlabel('t')
        plt.ylabel('a_x (m/s^2)')
        plt.title('Measured X Acceleration')
        plt.show()

        plt.plot(t, v_x)
        plt.xlabel('t')
        plt.ylabel('v_x (m/s)')
        plt.title('Calculated X Velocity')
        plt.show()

        plt.plot(t, x)
        plt.xlabel('t')
        plt.ylabel('x (m)')
        plt.title('Calculated X Position')
        plt.show()
    elif (coord == 'y'):
        plt.plot(t, a_y)
        plt.xlabel('t')
        plt.ylabel('a_y (m/s^2)')
        plt.title('Measured Y Acceleration')
        plt.show()

        plt.plot(t, v_y)
        plt.xlabel('t')
        plt.ylabel('v_y (m/s)')
        plt.title('Calculated Y Velocity')
        plt.show()

        plt.plot(t, y)
        plt.xlabel('t')
        plt.ylabel('y (m)')
        plt.title('Calculated Y Position')
        plt.show()
    elif (coord == 'z'):
        plt.plot(t, a_z)
        plt.xlabel('t')
        plt.ylabel('a_z (m/s^2)')
        plt.title('Measured Z Acceleration')
        plt.show()

        plt.plot(t, v_z)
        plt.xlabel('t')
        plt.ylabel('v_z (m/s)')
        plt.title('Calculated Z Velocity')
        plt.show()

        plt.plot(t, z)
        plt.xlabel('t')
        plt.ylabel('z (m)')
        plt.title('Calculated Z Position')
        plt.show()

