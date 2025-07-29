import numpy as np

def lre(wcss):
    """
    Linear Reference Elbow (LRE) method to determine optimal number of clusters.
    
    Parameters:
    -----------
    wcss : list or numpy array
        List of Within-Cluster Sum of Squares values for each k (ordered).
    
    Returns:
    --------
    int : Optimal number of clusters (k)
    """
    k_vals = np.arange(1, len(wcss) + 1)
    
    # Coordinates of first and last point
    x1, y1 = k_vals[0], wcss[0]
    x2, y2 = k_vals[-1], wcss[-1]
    
    # Vector components of the reference line
    A = y1 - y2
    B = x2 - x1
    C = x1 * y2 - x2 * y1
    
    # Compute orthogonal distance from each point to the line
    distances = np.abs(A * k_vals + B * wcss + C) / np.sqrt(A**2 + B**2)
    
    # Get index of maximum distance (optimal elbow)
    optimal_k = k_vals[np.argmax(distances)]
    
    return int(optimal_k)
