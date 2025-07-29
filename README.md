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
## 📦 Synthetic Dataset
The file `synthetic.xlsx` contains a challenging synthetic dataset designed to evaluate clustering algorithms. It consists of **2000 samples** divided into **4 clusters**:

- **2 clusters** with uniform distribution (in distinct quadrants)
- **2 clusters** with multivariate normal distribution:
  - One with negative correlation (skewed ellipse)
  - One with unequal variances (vertical ellipse)

This dataset replicates the complexity presented in the original IOP Conference paper, making it useful for testing LRE performance under real-world-like variance and structure.

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
