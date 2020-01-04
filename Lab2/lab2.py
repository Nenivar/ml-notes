import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt


a_curr = 1
b_curr = 1


def posterior(a, b, X):
    print(len(X))
    a_n = a + X.sum()
    b_n = b + (X.shape[0] - X.sum())

    return beta.pdf(mu_test, a_n, b_n), a_n, b_n


mu = 0.2
N = 100

# gen data
X = np.random.binomial(1, mu, N)
mu_test = np.linspace(0, 1, 100)

# prior
a = 10
b = 10

prior_mu = beta.pdf(mu_test, a, b)

# plot stuff
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(211)

ax.plot(mu_test, prior_mu, 'g')
ax.fill_between(mu_test, prior_mu, color='green', alpha=0.3)

ax.set_xlabel('$\mu$')
ax.set_ylabel('$p(\mu|\mathbf{x})$')

# pick random uniform point
# and update assumption
points = []

index = np.random.permutation(X.shape[0])
for i in range(0, X.shape[0]):
    y, a_n, b_n = posterior(a, b, X[:index[i]])
    plt.plot(mu_test, y, 'r', alpha=0.3)

    print(a_n, b_n)
    post_mean = beta.mean(a_n, b_n)
    prior_mean = beta.mean(a, b)

    points.append(post_mean - prior_mean)

y, _, _ = posterior(a, b, X)
plt.plot(mu_test, y, 'b', linewidth=4.0)

# q3
ax = fig.add_subplot(212)
xx = [i for i in range(0, len(points))]
plt.plot(xx, points)


plt.tight_layout()
plt.show()
#plt.savefig(path, transparent=True)
# return path
