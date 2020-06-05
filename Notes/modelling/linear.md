# Linear Regression

* Prediction: when we have an updated posterior, we want to see what this says about new data.
    - we want to see the **expected value** of the new data point under the posterior over the weights
    - $$p(t_*|t, x_*, X, \alpha, \beta) = \int p(t_*|x_*, \beta)p(w|t, X, \alpha, \beta) dw$$
    - where:
      - $t_*$ is the output value at location $x_*$
      - $x_*$ is the location we are interested in evaluating the function
      - $w$ is the weights that multiplied with $x$ gives the output
      - $\alpha, \beta$ are parameters of the prior and likelihood
      - $X, t$ are the pairs of input-output training data pairs
    - $$p(t_*|x_*) = \mathbb{E}_{p(w)}[p(t_*|x_*, w)]$$