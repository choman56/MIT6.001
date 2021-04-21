#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 08:35:53 2021

@author: clarke homan (copied from textbook)
"""

import Clustering
import kMeans
import random
import pylab


def genDistribution(xMean: int, xStdDev: int, yMean: int, yStdDev: int,
                    n: int, namePrefix: str) -> list:
    """
    Generate n samples list using normal (gaussian) random number generator.

    Args
    ----
        xMean (int): mean X position of samples.
        xStdDev (int): standard deviation of X position of samples.
        yMean (int): mean Y position of samples.
        yStdDev (int): standard deviation of y position of samples.
        n (int): number of samples to generate.
        namePrefix (str): label prfix for each sample.

    Returns
    -------
        list: generated samples.

    """
    samples = []
    for sample in range(n):
        sampleX = random.gauss(xMean, xStdDev)
        sampleY = random.gauss(yMean, yStdDev)
        example = Clustering.Example(namePrefix+str(sample),
                                     [sampleX, sampleY])
        samples.append(example)

    return samples


def plotSamples(samples: list, marker: str) -> None:
    """
    Scatter plot samples with labels.

    Args
    ----
        samples (list): List of samples to plot.
        marker (str): String marker type for plotting samples.

    Returns
    -------
        None.

    """
    xVals, yVals = [], []
    for sample in samples:
        x = sample.getFeatures()[0]
        y = sample.getFeatures()[1]
        pylab.annotate(sample.getName(),
                       xy=(x, y),
                       xytext=(x+0.13, y-0.07),
                       fontsize='small')
        xVals.append(x)
        yVals.append(y)
    pylab.plot(xVals, yVals, marker)

    return None


def contrivedTest(numTrials: int, numClusters: int, verbose: bool = False) -> \
                  None:
    """
    Perform contrived Test.

    Args
    ----
        numTrials (int): Number of trials to perform.
        numClusters (int): Number of clusters to create.
        verbose (bool+False): Enample debug print statements.

    Returns
    -------
        None.

    """
    xMean = 3
    xStdDev = 1
    yMean = 5
    yStdDev = 1
    numSamples = 15

    dist1Samples = genDistribution(xMean, xStdDev, yMean, yStdDev, numSamples,
                                   'A')
    plotSamples(dist1Samples, 'k.')

    dist2Samples = genDistribution(xMean+3, xStdDev, yMean+1, yStdDev,
                                   numSamples, 'B')
    plotSamples(dist2Samples, 'r+')

    clusters = kMeans.tryKMeans(dist1Samples+dist2Samples, numClusters,
                                numTrials, verbose)

    print('Final Result')
    for cluster in clusters:
        print('', str(cluster))


contrivedTest(10, 3, False)
