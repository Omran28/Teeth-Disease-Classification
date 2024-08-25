# Teeth Classification
# Overview
This repository contains a machine learning project focused on classifying dental images into different disease categories. The project utilizes convolutional neural networks (CNNs) to analyze and classify images of teeth based on various conditions.

# Dataset
The dataset used in this project is the "Teeth Dataset," which includes images categorized into the following disease classes:

CaS (Caries)
CoS (Crown)
Gum (Gum Diseases)
MC (Mouth Cancers)
OC (Oral Cancers)
OLP (Oral Lichen Planus)
OT (Other Types)
The dataset is augmented to balance the number of images per category, with each class reaching 1000 images.

# Features
Data Augmentation: Techniques used to increase the dataset size and variability.
Model Architecture: Custom CNN architectures designed for classifying dental images.
Evaluation: Metrics and methods used to evaluate model performance on training, validation, and test sets.
Visualization: Tools for visualizing images and their classifications, including grid-based displays of example images.

# Installation
To run this project, you will need Python and the following libraries:

TensorFlow
Keras
NumPy
Matplotlib
Pillow
Scikit-learn
