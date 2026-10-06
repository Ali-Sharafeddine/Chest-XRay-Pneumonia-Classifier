# Model Card — Portfolio Project

## Model

ResNet18 transfer-learning classifier with a two-class output layer:

- NORMAL
- PNEUMONIA

## Intended use

Educational use only: learning transfer learning, computer vision, evaluation, and AI engineering project structure.

## Out-of-scope use

- Clinical diagnosis
- Treatment decisions
- Patient triage
- Medical-device use
- Any safety-critical healthcare deployment

## Evaluation plan

Evaluate on a held-out test set using:

- Accuracy
- Precision
- Recall / sensitivity
- F1 score
- ROC-AUC
- Confusion matrix

Inspect false positives and false negatives separately.

## Limitations to discuss in the final version

- Dataset-specific biases
- Possible class imbalance
- Distribution shift between datasets/hospitals
- Image acquisition differences
- Lack of clinical validation
- Potential shortcut learning
- Grad-CAM is not proof of causal medical reasoning

## Current status

Repository structure and evaluation pipeline prepared. Demo graphics are illustrative placeholders. Real metrics should be added only after running the experiment.
