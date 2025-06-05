#!/bin/bash

# This script sets up a conda environment for a sequence analysis project.
conda create -n seq_env python=3.10 -y 
conda activate seq_env

#Install Biopython 
conda install bipython -y

# Install git and push to GitHub
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/nadiatasevski/Homework_1_OBC.git
git push -u origin main

#Run the Python script and save output
python analyze_sequences.py > output.txtgit commit
