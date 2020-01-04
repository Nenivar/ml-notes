import numpy as np
import matplotlib as plt
from scipy.spatial.distance import cdist

def rbf_kernel(x1, x2, sigma, lengthscale):
    if x2 is None:
        d = cdist(x1, x1)
    else:
        d = cdist(x1, x2)
    
    K = sigma * np.exp(-np.power(d, 2) / lengthscale)

    return K

# choose index set for marginal
x = np.linspace(-6, 6, 200).reshape(-1, 1)
# compute covar matrix
K = rbf_kernel(x, None, 1.0, 2.0)
# create mean vec
mu = np.zeros(x.shape)

print(x.shape)
print(K.shape)

# draw 20 samples from Gauss dist
f = np.random.multivariate_normal(mu, K, 20)

fig = plt.figure()