```markdown
# Mathematics for Machine Learning & Data Science: Capstone Engine

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sevinc001/Math-ML-Statistical-inference-engine/blob/main/notebooks/exploratory_analysis.ipynb)

A modular Python framework demonstrating core mathematical foundations—**Linear Algebra**, **Multivariate Calculus (Optimization)**, and **Probability & Statistics**—implemented from scratch without relying on black-box machine learning libraries for core computational logic.

This repository serves as the final capstone project for the **Mathematics for Machine Learning and Data Science Specialization**.

* **Official Certificate:** [View Coursera Certificate](https://www.coursera.org/account/accomplishments/specialization/M3RLK0DMV6DM)

---

## 🏗️ Project Architecture

The engine is structured modularly to separate matrix operations, optimization routines, and statistical inference:

```text
Math-ML-Statistical-inference-engine/
│
├── src/
│   ├── linear_algebra.py    # Vector and matrix transformation routines
│   ├── optimizer.py         # Gradient descent and multivariate calculus solvers
│   └── statistics.py        # Sample statistics, degrees of freedom, and t-tests
│
├── notebooks/
│   └── exploratory_analysis.ipynb # End-to-end data pipeline and visualization engine
│
├── requirements.txt
└── README.md


```

---

## 🧮 Core Mathematical Components

### 1. Linear Algebra & Vector Spaces (`linear_algebra.py`)

* Implements foundational array representations, vector dot products, and matrix transformations.
* Handles data shaping and scaling required for multi-feature machine learning inputs.

### 2. Multivariate Calculus & Optimization (`optimizer.py`)

* Implements **Gradient Descent** by computing partial derivatives of cost functions (Mean Squared Error).
* Iteratively optimizes weights and biases to find global/local minima for predictive modeling.

### 3. Probability & Statistics (`statistics.py`)

* **Sample Statistics:** Calculates group size ($n$), mean ($\bar{x}$), and sample standard deviation ($s$ with $N-1$ degrees of freedom).
* **Welch’s t-Test & Degrees of Freedom ($d$):** Computes robust degrees of freedom for samples with unequal variances:

$$d = \frac{\left( \frac{s_c^2}{n_c} + \frac{s_v^2}{n_v} \right)^2}{\frac{(s_c^2 / n_c)^2}{n_c - 1} + \frac{(s_v^2 / n_v)^2}{n_v - 1}$$

* **Hypothesis Testing Engine:** Automates decision-making (`Reject H_0` vs `Do not reject H_0`) using $t$-values and $p$-values derived from Student's t-distribution.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed along with the required libraries:

```bash
pip install numpy scipy pandas matplotlib


```

### Running the Tests

To verify the statistical and optimization modules:

```bash
python -m unittest discover


```

---

## 👤 Author

Developed as a portfolio project showcasing the rigorous mathematical principles underlying Artificial Intelligence and Data Science.

```

Bunu yapışdırıb **Commit changes** etdikdən sonra sertifikat linkin də tam işlək vəziyyətə gələcək!

```
