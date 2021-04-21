#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 09:02:38 2021

@author: clarke homan (copied and improved from text book)
"""
import pylab


def minkowski(vector1: list, vector2: list, power: int) -> float:
    """
    Calculate Minkowski distance between two vectors.

    power = 1 = Manhattan distance (edges)
            D(X,Y) = (sum(|x - y|**power))**(1/p)

    power = 2 = Euclidean distance
            D(X,Y) = sqrt(sum((x-y)**2))


    Args
    ----
        vector1 (array): feature vector 1.
        vector2 (array): feature vector 2.
        power (int): determines which Minkowski distance to calculate and ret

    Returns
    -------
        distanceArray (float): overall distance of order power between the two
                               input vectors

    """
    #
    # Paramter validation section
    #
    assert len(vector1) == len(vector2)
    assert type(power) is int
    assert power == 1 or power == 2

    distanceArray = 0.0

    for i in range(len(vector1)):  # process vector elements sequentially
        distanceArray += (abs(vector1[i] - vector2[i]))**power

    return distanceArray


class Example(object):
    """Class used to build samples to be clustered."""

    def __init__(self, name: str, features: list, label: str = None) -> None:
        # Assumes features is an array of floats
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self) -> int:
        """Return Example object dimensionality (len)."""
        return len(self.features)

    def getFeatures(self) -> list:
        """Return Example object feature array."""
        return self.features[:]  # return entire array

    def getLabel(self) -> str:
        """Return Example object label."""
        return self.label

    def getName(self) -> str:
        """Return Example object name."""
        return self.name

    def distance(self, otherArray: list, power: int = 2) -> float:
        """Calculate Minkowski distance between self and otherArray."""
        # power should be 1 or 2 (Manhattan or Euclidean)
        assert power == 1 or power == 2
        return minkowski(self.features, otherArray.getFeatures(), power)

    def __str__(self) -> str:
        """Return string representation of Example object."""
        return self.name + ':' + str(self.features) + ':' + str(self.label)


class Cluster(object):
    """Cluster object is a group of examples, centered around its centroid."""

    def __init__(self, examples: list):
        self.examples = examples
        self.centroid = self.computeCentroid()

    def update(self, examples: list):
        """
        Examples is a non-empty list of Examples objects.

        Calculate updated centroid based on supplied examples. Return Minkowski
        distance amount between new centroid and previous centroid.

        Args
        ----
            examples (list): New list of examples to replace previous list.

        Returns
        -------
            Difference in Minkowski distance between new centroid and previous
        """
        assert len(examples) > 0

        oldCentroid = self.centroid  # save old centroid position

        self.examples = examples  # update examples list

        self.centroid = self.computeCentroid()  # compute new centroid

        # calculate distance difference between old and new centroids
        centroidDistanceDifference = oldCentroid.distance(self.centroid)

        return centroidDistanceDifference

    def computeCentroid(self):
        """
        Compute centroid of existing list of Examples.

        Returns
        -------
            centroid (Example): Centroid positions (X, Y) of examples
        """
        # Create an array of 0.0's with length of example's 1st array
        vals = pylab.array([0.0]*self.examples[0].dimensionality())

        # compute mean by adding up features in example's feature vector
        # Calculate centroid of existing examples list by dividing sum
        # of features by number of features
        # creating and returning centroid Example object
        for example in self.examples:
            vals += example.getFeatures()

        centroid = Example('centroid', vals / len(self.examples))
        return centroid

    def getCentroid(self):
        """Fetch Cluster object's current centroid."""
        return self.centroid

    def variability(self):
        """
        Caluclate sum of squares of distance between centroid and elements.

        Returns
        -------
        totalDistance (float): Sum of squares distance between centroid and
                               elements
        """
        totalDistance = 0.0
        for example in self.examples:
            totalDistance += (example.distance(self.centroid))**2

        return totalDistance

    def members(self):
        """
        Iterate and return each member example of the cluster's elements.

        Returns
        -------
           Yeilds individual members of cluster's elements'

        """
        for example in self.examples:
            yield example

    def __str__(self):
        """
        Generate and return string representation of Cluster.

        Presume for printing.

        Returns
        -------
            stringRep (str)

        """
        names = []
        for example in self.examples:  # extract list of example names
            names.append(example.getName())

        names.sort()  # sort names alphabetically

        stringRep = 'Cluster with centroid ' + \
            str(self.centroid.getFeatures()) + \
            ' contains: \n '

        for name in names:  # concatentate name list
            stringRep += name + ', '

        stringRep = stringRep[: -2]  # remove trailing comma and space
        return stringRep
