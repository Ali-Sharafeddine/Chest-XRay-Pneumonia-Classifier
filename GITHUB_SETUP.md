# GitHub Publishing Guide

The folder is already initialized as a local Git repository and contains an initial commit.

## Recommended repository name

`Chest-XRay-Pneumonia-Classifier`

## Recommended description

`PyTorch + ResNet18 transfer-learning project for Normal/Pneumonia chest X-ray classification, with training, evaluation, metrics, visualizations, and optional Grad-CAM.`

## Option A — GitHub website + Git commands

1. On GitHub, create a new **public** repository named:

   `Chest-XRay-Pneumonia-Classifier`

2. Do **not** initialize it with another README, `.gitignore`, or license, because those already exist locally.

3. In a terminal opened inside this project folder, run:

```bash
git branch -M main
git remote add origin https://github.com/Ali-Sharafeddine/Chest-XRay-Pneumonia-Classifier.git
git push -u origin main
```

If `origin` already exists:

```bash
git remote set-url origin https://github.com/Ali-Sharafeddine/Chest-XRay-Pneumonia-Classifier.git
git push -u origin main
```

## Option B — GitHub CLI

If `gh` is installed and authenticated:

```bash
gh repo create Chest-XRay-Pneumonia-Classifier --public --source=. --remote=origin --push
```

## Optional: verify Git identity before pushing

```bash
git config user.name
git config user.email
```

If you want to change the author identity used for the initial commit before pushing:

```bash
git config user.name "Ali Sharafeddine"
git config user.email "YOUR_GITHUB_EMAIL_OR_NOREPLY_EMAIL"
git commit --amend --reset-author --no-edit
```

## After pushing

On the GitHub repository page:

- Add the repository description shown above.
- Add topics such as `pytorch`, `deep-learning`, `computer-vision`, `resnet`, `transfer-learning`, `medical-imaging`, `machine-learning`.
- Confirm the project card renders at the top of the README.
- Do not upload the Kaggle dataset itself.
- Replace demo assets with real outputs after training.
