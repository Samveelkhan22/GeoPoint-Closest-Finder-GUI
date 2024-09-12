# GeoPoint-Closest-Finder-GUI
This project is a Python application that allows users to find the closest geographical point to their location based on a file of pre-defined points. The program demonstrates the use of a **Graphical User Interface (GUI)** using **wxPython** and incorporates classes and functions from a previous assignment.

The GUI takes a file containing multiple points (latitude, longitude, and description), accepts the user's current latitude and longitude, and displays the closest point in the dataset.

## Features

- **GeoPoint Class**: Models geographical points with latitude, longitude, and a description.
- **Distance Calculation**: Calculates the Euclidean distance between two geographical points.
- **File Input**: Reads a file with predefined geographical points.
- **User Location Input**: Allows users to input their latitude and longitude through a GUI.
- **Closest Point Finder**: Displays the closest point from the dataset to the user's location.
- **wxPython GUI**: User-friendly interface with textboxes and buttons for easy interaction.

## Files 

- program10.py         # Library with GeoPoint class and utility functions
- LastnameP11.py       # Main GUI application using program10 as a library
- points.txt           # Example data file containing predefined points
- requirements.txt     # List of dependencies (optional)

