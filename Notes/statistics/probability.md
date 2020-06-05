# Probability

## Distributions

* **Joint:** $p(x,y)$: the probability that events $x$ and $y$ will occur simultaneously
* **Marginal**: $p(x) = \sum p(x, y)$: the probability of event $x$ in the presence of all outcomes of $y$
* **Conditional**: $p(x|y)$: the probability that the event $x$ will occur in the presence of $y$

## Rules

* **Sum**:
  $$p(x) = \sum_y p(y, x), p(x) = \int p(y,x) dy$$
* **Product**:
  $$p(x,y) = p(y|x)p(x)$$
* **Bayes**:
  $$p(\theta|d) = \frac {p(d|\theta)p(\theta)}{p(d)}$$
  $$\text{posterior} = \frac{\text{likelihood}\cdot\text{prior}}{\text{evidence}}$$
  where
  $$p(d) = \int p(d|\theta)p(\theta)$$

## Interpretations

* **Expectation**: taking an average of all possible values of the variable, weighted according to their probability (i.e. how likely I believe the variable to take this value)
    $$\mathbb{E}[x] = \sum_x p(x) \cdot x$$

* **Expectations**: we can take expectations over probability distributions
    $$p(y) = \int p(y, x) dx = \int p(y|x) p(x) dx$$
    this means: what do I believe the function is over *only* y if I create a new function $p(y)$ which is a weighted average of all possible settings of the variable $x$

* **Variance**: the expectations of how a variable varies around its expectations
    $$var[x] = \mathbb{E}[(x - \mathbb{E}[x])^2]$$

* **Covariance**: the expectation on how two variables varies *together* in relation to their means
    $$cov[x, y] = \mathbb{E}[(x - \mathbb{E}[x])(y - \mathbb{E}[y])]$$

- **Maximum Likelihood Estimation**: method of estimating the parameters of a probability distribution by maximizing a likelihood function, s.t. under the assumed model the observed data is most probable
  - $$\theta_{MLE} = \text{arg max}[\theta] \prod_i P(x_i|\theta)$$
  - point wise
  - however this avoids your belief
  - the likelihood is essentially a quantification of the error - we want to find the parameters which minimise the error

- **Maximum a Posteriori (MAP)**: gives you the mode of the posterior distribution
  - $$\theta_{MAP}(x) = \text{arg max} f(\theta | x)$$
  - also a point estimate
  - this is very similar to MLE but with prior probability over the distribution and parameters

> note: MAP and MLE can often converge to the same problem, but **not always** (you need to assume uniform prior probabilities (i.e. all values of theta are equally likely))