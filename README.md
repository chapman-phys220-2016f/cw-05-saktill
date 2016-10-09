# PHYS220 CW 5

**Author(s):** _\<Will and Sakthi\>_

[![Build Status](https://travis-ci.org/chapman-phys220-2016f/cw-05-saktill.svg?branch=master)](https://travis-ci.org/chapman-phys220-2016f/cw-05-saktill)

**Due date:** 2016/10/04

## Specification

**Note: As of this assignment, we will be switching to Python3 officially.**

1. Using a PocketLab in class, take the following set of data:
    * Turn on 2 graphs: 3-axis acceleration, and altitude
    * By holding the device with a rigid orientation (z-axis aligned with vertical - why is this advisable?), take a recorded set of data while moving the device along an interesting path. As a suggestion, try a vertical helix. Be sure to keep your motions smooth, and changing slowly enough that the data points are being sampled fast enough to resolve the acceleration data.
    * Email yourself the dataset, which will arrive as a ```.csv``` file.
1. Read up on the ```pandas``` extension to ```numpy``` [here](http://slides.com/profdressel/numpy-and-pandas-overview). Try out everything in an ```ipython``` interpreter to make sure you understand what is going on. Discuss with your teammates. 
1. Write a python module ```kinematics.py``` that integrates your acceleration data to produce a 3D position trajectory of the device during your experiment. Remember that $\vec{v}(t) = \int \vec{a}(t)dt$ and $\vec{x}(t) = \int \vec{v}(t)dt$ analytically. Explain what you have to do numerically to perform these integrations with the actual collected data.
1. Create a Jupyter notebook ```cw5.ipynb``` that uses ```pandas``` to plot the data sets you have taken using ```matplotlib```. Import ```kinematics.py``` and plot your reconstructed trajectory for the device. Compare the z-component of this trajectory to the collected altitude data. Do they agree? Discuss your findings and conclusions in your notebook.

Pro-tip: using git to manage conflicts on Jupyter notebooks is a pain. I recommend delegating one person from your group to edit the notebook, to avoid merge conflicts.

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

This assignment was great because it really forced us to address the issues that come with using a computer for problems that seem trivial to solve on paper. Also, the pocket labs are way too much fun. However, the fact that the integrated data was clearly very wrong is irksome to say the least, and I'm desperately hoping that that's my error, not just a fact of life in scientific computing. Also, I think it would have been much easier had our data been much better, so I'm sure there's a lesson to be learned there somewhere. 

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Will, Sakthi
