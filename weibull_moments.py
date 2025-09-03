import numpy as np
import matplotlib.pyplot as plt

# Equation for the generation of the weibull sample using the 
# cumulucative distribution F(x), with k=2, λ=1:

def generate_weibull_sample(size):
    F = np.random.rand(size)
    return (-(np.log(1 - F))) ** (1/2)

# Parameter of the Weibul distribution:
sample_size = 1000

# Generation of the sample:
sample = generate_weibull_sample(sample_size)

#Showing of the sample:
print("The sample consists of the values: ", sample)

#Calculating the first four moments using the random sample:
first_moment  = np.mean(sample ** 1)
second_moment = np.mean(sample ** 2)
third_moment  = np.mean(sample ** 3)
forth_moment  = np.mean(sample ** 4)

#Print the results:
print("The first moment (or the mean value) is:", first_moment )
print("The second moment (or the variance)  is:", second_moment)
print("The third moment is:",                     third_moment )
print("The forth moment is:",                     forth_moment )

#Determination of the histogram made of the sample Σ with 50 bins:
hist, bin_edges = np.histogram(sample, bins=20)

#Calculation of the integral of the histogram in order to 
#properly normalize the Weibull distribution in the histogram:
bin_widths = np.diff(bin_edges)
integral_of_the_sample = np.sum(hist * bin_widths)

#Determine the f(x) Weibull distribution with k=2, λ=1:
x = np.linspace(np.min(sample), np.max(sample), np.size(sample))
Weibull_distribution = 2 * integral_of_the_sample * x * np.exp(-x ** 2)

#Plot the Weibull distribution and the sample in the same plot:
plt.plot(x, Weibull_distribution,'r', label='f(x)')
plt.hist(sample, bins=20, label="Random sample, Σ")
plt.xlabel("X")
plt.ylabel("Counts")
plt.legend()
plt.grid(True)
plt.show()

