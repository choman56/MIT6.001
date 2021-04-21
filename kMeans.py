#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:12:52 2021

@author: clarke homan  (copied and improved from text book)

Methods for k-means clustering determinations.

"""

import Clustering
import random


def dissimilarity(clusters: list) -> float:
    """
    Calculate total aggerate distance between cluster's centroid and elements.

    Args
    ----
        clusters (TYPE): DESCRIPTION.

    Returns
    -------
        totalDistance (float): aggregate  distances

    """
    totalDistance = 0.0
    for cluster in clusters:
        totalDistance += cluster.variability()

    return totalDistance


def kmeans(examples: list, numClusters: int, verbose: bool = False) -> list:
    """
    Generate numClusters Clusters using greedy algorithm.

    Args
    ----
        examples (list): List of sample points
        numClusters (int): Number of clusters to generate
        verbose (bool, optional): Print statements. Defaults to False.

    Returns
    -------
        list: Current set of defined clusters.

    Algorithm
    ---------
        Randomly choose numExamples examples as initial centroids
        while true
          - Assign each member of passed in examples to the cluster whose
            centroid is closest
          - Compute updated clusters centroid with the addition of new members
          - If new cluster centroids are not different then they were in the
            previous iteration of the while loop
            - return the current set of clusters

    """
    # Generate numClusters centroids and add them to separate cluster list
    # elements
    initialCentroids = random.sample(examples, numClusters)
    clusters = []
    for centroid in initialCentroids:
        clusters.append(Clustering.Cluster([centroid]))

    #
    # Iterate until centroids do not change (converge)
    #
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1

        # Create a list containing numClusters distinct empty lists
        newClusters = []
        for i in range(numClusters):
            newClusters.append([])
        #
        # Associate each example with the cluster with the closest centroid
        #
        for example in examples:
            # Find the centroid among the centroids of the cluster list
            # that is closest to the example starting with first centroid
            # group and compare other centroids
            currentSmallestDistance = \
              example.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, numClusters):
                # Comment out one of the two folllowing lines
                # if power paramter is 1, calculate Manhattan distance
                # if power paramter is 2, calculate Euclidean distance
                # power = 1
                power = 2
                distance = example.distance(clusters[i].getCentroid(), power)
                if distance < currentSmallestDistance:
                    currentSmallestDistance = distance
                    index = i
            # Add example element to the cluster list of examples, where the
            # distance between the element and the cluster list's 
            # centroid is minimum.
            newClusters[index].append(example)

        for cluster in newClusters:  # Check to see if any empty clusters
            if len(cluster) == 0:
                raise ValueError('Empty cluster')

        # Update each cluster; determine if cluster centroid has changed
        converged = True
        for i in range(numClusters):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False

        if verbose:
            print('Iteration num:', numIterations)
            for cluster in clusters:
                print(cluster)
            print("\n")
    return clusters


def tryKMeans(examples: list, numClusters: int, numTrials: int,
              verbose: bool = False) -> list:
    """
    Perform numtrials iterations of kmeans and returns result.

    With lowest dissimilarity. Calls kmeans numTrials times, each iteration
    of the trial only evaluated if kmeans returns with no exception (exception
    generated if kmeans generating empty cluster). After each iteration of
    kmeans, tryKMeans compares the new clusters' dissimilarity with the prior
    clusters' dissimarilty and if the new set ofcluster has lower
    dissimilarity, that cluster becomes the new minimum candidate cluster.
    Dissimilarity is calculated by the Cluster by summing up the square
    distance between all of the cluster's examples with the cluster's centroid
    as a total distance.

    Args
    ----
        examples (list): List of Example objects.
        numClusters (int): Number of clusters to generate.
        numTrials (int): Number of iterations of kmeans to perform.
        verbose (boolean): (Debug) Essentially print statements.

    Returns
    -------
        list: best cluster with lowest dissimilarity.

    """
    best = kmeans(examples, numClusters, verbose)
    minDissimalarity = dissimilarity(best)
    trial = 1

    while trial < numTrials:
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue  # If kmeans generates empty cluster exception

        currentDissimilarity = dissimilarity(clusters)
        if currentDissimilarity < minDissimalarity:
            best = clusters
            minDissimalarity = currentDissimilarity
        trial += 1

    return best