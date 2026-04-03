# Apex-NFT-Stability-Predictor

An AI model built on the OpenGradient infrastructure to evaluate the stability and risk profile of NFT collections.

## Project Status: Testnet

This model is currently deployed and tested on the OpenGradient Testnet.

## How it Works

The model analyzes market data and classifies an NFT collection into one of two risk levels:
* Level 0: Stable Floor Price (Low Risk)
* Level 1: Volatile Floor Price (High Risk)

It predicts this stability based on multiple on-chain indicators.

## Technical Details

* Model Type: Classification Model (trained using Scikit-Learn's RandomForestClassifier).
* Format: ONNX (Deployed as a verifiable model on OpenGradient).
* Input: Float array representing market features.
* Output: [0] for Stable, [1] for Volatile.
<img width="1324" height="564" alt="Screenshot 2026-04-03 023105" src="https://github.com/user-attachments/assets/3437e5dc-b7ca-494a-aeb6-fe06711b44b7" />
