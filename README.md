# Linear Reference Elbow (LRE)

This repository implements the **Linear Reference Elbow (LRE)** method for automatically determining the optimal number of clusters in the K-Means algorithm.

Unlike the traditional visual elbow method, LRE uses a geometric approach by computing the orthogonal distance between each WCSS point and a reference line. The method is:
- **Objective** (no manual intervention)
- **Fast** (linear time complexity O(n))
- **Reproducible**

This implementation is part of the author's research presented in the IOP Conference Series 2025.

## 📊 Iris dataset
The notebook includes examples using:
- Iris dataset (from `sklearn.datasets`)
---

## 📦 Synthetic Dataset
The file `synthetic.xlsx` contains 2000 samples divided into 4 clusters:
- **2 clusters** generated from uniform distributions
  - Located in opposite quadrants
- **2 clusters** generated from multivariate normal distributions
  - One with negative correlation (skewed elliptical shape)
  - One with unequal variances (vertical ellipse)

This dataset is the same as the one used in the IOP Conference publication. It challenges clustering methods with heterogeneity and variance structure, making it ideal for benchmarking automated methods like LRE.


## 🚀 How to Use

1. **Clone this repository:**
   ```bash
   git clone https://github.com/mattbit212/LRE.git
   cd LRE
2. **Install dependencies (if needed):**
   ```bash
   pip install -r requirements.txt OR pip install numpy matplotlib scikit-learn
4. **Open and run the notebook:** 
   ```bash
   KMeans_LRE.ipynb
5. **Citation**
If you use this method or code in your research, please cite the following:

Yusuf, A. (2025). Computational Implementation of Linear Reference Elbow (LRE) Method for Optimal Cluster Determination in K-Means Algorithm. IOP Conference Series. [https://doi.org/10.5281/zenodo.16574800]
