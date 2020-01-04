import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

def plot_distribution(ax, mu, Sigma):
    x = np.linspace(-1, 1, 100)
    #y = np.full((100, 1), 1)
    x1p, x2p = np.meshgrid(x, x)
    #x1p, x2p = np.meshgrid(x, y)
    pos = np.vstack((x1p.flatten(), x2p.flatten())).T

    pdf = multivariate_normal(mu.flatten(), Sigma)
    Z = pdf.pdf(pos)
    Z = Z.reshape(100, 100)

    ax.contour(x1p, x2p, Z, 5, colors='r', lw=5, alpha=0.7)
    ax.set_xlabel('w_0')
    ax.set_ylabel('w_1')

    return pos

fig, ax = plt.subplots()

#prior_mu = np.zeros((2,1))
prior_mu = np.array([-0.5, 0.5])
#prior_mu = np.vstack([-1.3, 0.5])
prior_cov = 1.0 * np.eye(2)
#prior_cov = 1.0 * np.vstack([[1.0, 0.2],[0.0, 0.4]])

#x = np.linspace(-1, 1, 200)
#xx = np.full((200, 1), 1)
#x1p, x2p = np.meshgrid(x, xx)
#x1p, x2p = np.meshgrid(x, x)
#xx = np.linspace(1, 1, 200)
#pos = np.vstack((x1p.flatten(), x2p.flatten())).T
#print(pos)

print('prior mu', prior_mu)
print('prior cov', prior_cov)

pos = plot_distribution(ax, prior_mu, prior_cov)
plt.show()

# todo: add error?

index = np.random.permutation(pos.shape[0])
#for i in range(0, index.shape[0]):
for i in range(0, 5):
    error = np.random.normal(0, 0.3, 1)
    print('error', error)
    precision = abs(1 / error)

    X_i = pos[index, :]
    # gen ys
    y = np.dot(prior_mu, X_i.T) + error
    y_i = y[index]

    print('X_i', X_i)
    print('y_i', y_i)

    # compute posterior
    # w0 is mean of distribution for w (prior mean)
    # s0 is cov of distribution for w (prior cov)
    w0 = prior_mu
    s0 = np.linalg.inv(prior_cov)
    
    # mean_1 = s0 + precision * np.matmul(X_i.T, X_i)
    # mean_2 = np.matmul(s0, w0) + precision * np.matmul(X_i.T, y_i)
    # mean = np.matmul(np.linalg.inv(mean_1), mean_2)
    # cov = mean_1
    mean = np.matmul(np.linalg.inv((np.matmul(X_i.T, X_i) + s0)), np.matmul(X_i.T, y_i));
    #cov = np.linalg.inv(np.matmul(X_i.T, X_i) + s0)
    cov = prior_cov
    
    print('mean', mean)
    print('cov', cov)

    prior_mu = mean
    prior_cov = cov
    
    # visualise posterior
    fig, ax = plt.subplots()
    pos = plot_distribution(ax, mean, cov)
    plt.show()

    # visualise samples from posterior w data

    # print out mean of posterior
