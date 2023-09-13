# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 04:04:14 2023

@author: sarat
"""

from movies import movie_dataset, movie_labels

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, labels, k):
  distances = []
  num_good = 0
  num_bad = 0
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]

  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 1:
      num_good += 1
    elif labels[title] == 0:
      num_bad += 1
    if num_good > num_bad:
      return 1
    else:
      return 0


print(classify([0.4, 0.2, 0.9], movie_dataset, movie_labels, k=5))