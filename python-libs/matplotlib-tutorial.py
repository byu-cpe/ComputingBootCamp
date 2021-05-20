import matplotlib.pyplot as plt
import numpy as np

#######################
# Simple Example

# Basic Plot
idx = np.array([1, 2, 3, 4, 5])
data = np.array([5, 10, 12, 16, 18])

plt.plot(idx, data)
plt.show()


# Add title/labels
plt.plot(idx, data)
plt.xlabel('test number')
plt.ylabel('result')
plt.title('my graph')
plt.show()

# add more data and legend
plt.plot(idx, data, label='Method 1')
plt.plot(idx, [5, 11, 13, 15, 19], label='Method 2')
plt.xlabel('test number')
plt.ylabel('result')
plt.title('my graph')
plt.legend()
plt.show()

##################################
# Figures, Axes, Axis
fig, axs = plt.subplots(2)
print(axs)

axs[0].plot(idx, data, label='Method 1')
axs[0].plot(idx, [5, 11, 13, 15, 19], label='Method 2')
axs[0].set_xlabel('test number')
axs[0].set_ylabel('result')
axs[0].set_title('my graph')
axs[0].legend()

axs[1].plot(idx, data, label='Method 1')
axs[1].plot(idx, [3, 5, 1, 7, 10], label='Method 2')
axs[1].set_xlabel('test number')
axs[1].set_ylabel('result')
axs[1].set_title('my graph2')

fig.tight_layout()

plt.show()

#############################
# Many other kinds of plots

# Hist
rng = np.random.RandomState(10)
a = rng.normal(size=1000)
_ = plt.hist(a, bins=30)
plt.title('Histogram - Gaussian')
plt.show()

# Scatter plot
a = np.random.rand(2, 1000)
plt.scatter(a[0, :], a[1, :])
plt.title("Scatter plot of ...")
plt.show()

##################################
# Change formatting
fig, axs = plt.subplots(2)
print(axs)

axs[0].plot(idx, data, 'go-', label='Method 1')
axs[0].plot(idx, [5, 11, 13, 15, 19], 'rs--', label='Method 2')
axs[0].set_xlabel('test number')
axs[0].set_ylabel('result')
axs[0].set_title('my graph')
axs[0].legend()

axs[1].plot(idx, data, 'mp-.', label='Method a')
axs[1].plot(idx, [3, 5, 1, 7, 10], 'b8:', label='Method b')
axs[1].set_xlabel('test number')
axs[1].set_ylabel('result')
axs[1].set_title('my graph2')
axs[1].legend()

fig.tight_layout()

plt.show()
