# Linear Reference Elbow (LRE)

This repository implements the **Linear Reference Elbow (LRE)** method for automatically determining the optimal number of clusters in the K-Means algorithm.

Unlike the traditional visual elbow method, LRE uses a geometric approach by computing the orthogonal distance between each WCSS point and a reference line. The method is:
- **Objective** (no manual intervention)
- **Fast** (linear time complexity O(n))
- **Reproducible**

This implementation is part of the author's research presented in the IOP Conference Series 2025.

## 📊 Example Dataset
The notebook includes examples using:
- Iris dataset (from `sklearn.datasets`)
- Synthetic dataset (planned for next version)

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

Yusuf, A. (2025). Computational Implementation of Linear Reference Elbow (LRE) Method for Optimal Cluster Determination in K-Means Algorithm. IOP Conference Series. [DOI pending]
DOI for the code version (upcoming via Zenodo).
