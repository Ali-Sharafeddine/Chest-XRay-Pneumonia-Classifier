# Project Summary / Interview Cheat Sheet

## 15-second explanation

I built a PyTorch computer-vision pipeline for classifying chest X-rays as Normal or Pneumonia using ResNet18 transfer learning. The project covers preprocessing, training, validation, test evaluation, confusion-matrix analysis, prediction visualization, and optional Grad-CAM inspection.

## 30-second explanation

I used a pretrained ResNet18 as the feature extractor and replaced its final classifier with a two-class output layer. I prepared the dataset using torchvision transforms and DataLoaders, trained the classifier head, tracked validation performance, and evaluated the final model on a held-out test set. Instead of reporting only accuracy, I included precision, recall, F1, ROC-AUC, a confusion matrix, and prediction examples so I could inspect false positives and false negatives.

## Why transfer learning?

A medical-imaging learning project usually has far less data than the datasets used to train large vision models. Transfer learning provides useful pretrained visual features and allows a strong baseline without training a large CNN from scratch.

## Why recall matters

For the positive Pneumonia class, recall measures how many actual positive cases the model detects. A false negative means an actual pneumonia image was predicted as Normal. In a real clinical setting that could be important, although this portfolio model is not clinically validated.

## Why not trust accuracy alone?

If classes are imbalanced, accuracy can hide weak behavior on the minority class. Precision, recall, F1 and the confusion matrix reveal the kinds of mistakes being made.

## What would I improve next?

1. Fine-tune some pretrained ResNet layers.
2. Compare architectures.
3. Analyze thresholds.
4. Investigate class imbalance.
5. Review false positives/false negatives.
6. Add real Grad-CAM examples.
7. Track experiments and export the best checkpoint.
