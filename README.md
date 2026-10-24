# PixelBudget: Autoregressive Image Generation Under Latency & Memory Constraints

> **Author & Lead Researcher**: Nguyen Huynh Dang Nhut (@nhutnhd)  
> **Affiliation**: University of Information Technology (UIT), VNU-HCM  
> **Evolutionary Lineage**: Developed as an empirical continuation of `neural-network-from-scratch`  
> **Execution Environments**: NVIDIA T4 GPU (Colab) & Validated CPU Reference Benchmarks  

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Environment: PyTorch](https://img.shields.io/badge/Environment-PyTorch%20%7C%20CUDA-ee4c2c?style=flat-square&logo=pytorch)](https://pytorch.org/)
[![Hardware: NVIDIA T4 / CPU](https://img.shields.io/badge/Hardware-NVIDIA%20T4%20%2F%20CPU-76b900?style=flat-square&logo=nvidia)](https://colab.research.google.com/)

---

## 1. Executive Summary

**PixelBudget** investigates the trade-off space between computational budgets (GPU VRAM, cache line capacity, memory bandwidth) and image quality in autoregressive generative modeling.

Originating from first-principles multilayer perceptron (MLP) implementations, this research formulates pixel-level autoregressive generation under strict latency constraints on commodity edge hardware (NVIDIA Tesla T4 GPU and multi-core CPU).

---

## 2. Key Research Contributions

1. **Analytical vs Autograd Loss Modeling**: Comparing custom analytical backpropagation routines against PyTorch autograd graph overheads.
2. **Memory Budget Allocation**: Profiling memory bandwidth bottlenecks during autoregressive pixel-by-pixel decoding versus parallel patch generation.
3. **Hardware-Validated Benchmarks**: Empirical validation curves, loss convergence plots, and latency histograms comparing CPU execution with GPU acceleration.

---

## 3. Artifact Manifest

- `PixelBudget_CPU_Validated.ipynb`: Self-contained interactive computational laboratory containing source code, profiling loops, and reproduction instructions (68 cells).
- `PixelBudget_CPU_Report.html`: Rendered empirical analysis report and visualizations for offline scientific peer review.
