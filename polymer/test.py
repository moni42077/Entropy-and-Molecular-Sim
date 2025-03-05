import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10       # Number of monomers in the chain
b = 1         # Length of each bond
num_steps = 1000  # Number of chains to generate (for averaging)

# Initialize variables to store results
end_to_end_distances = []
radii_of_gyration = []

# Function to generate an ideal chain and calculate properties
def generate_chain(N, b):
    # Generate random angles (uniformly distributed over a sphere)
    directions = np.random.randn(N, 3)
    directions /= np.linalg.norm(directions, axis=1)[:, np.newaxis]  # Normalize to unit vectors

    # Initialize chain's coordinates
    chain = np.zeros((N, 3))

    # Generate positions by adding each bond vector
    for i in range(1, N):
        chain[i] = chain[i - 1] + b * directions[i]  # Add bond vector

    # End-to-end distance (distance from first to last monomer)
    R = np.linalg.norm(chain[-1])

    # Radius of gyration calculation
    center_of_mass = np.mean(chain, axis=0)
    R_g = np.sqrt(np.mean(np.linalg.norm(chain - center_of_mass, axis=1)**2))

    return R, R_g

# Run simulation for multiple chains and collect results
for _ in range(num_steps):
    R, R_g = generate_chain(N, b)
    end_to_end_distances.append(R)
    radii_of_gyration.append(R_g)

# Calculate average values
avg_R = np.mean(end_to_end_distances)
avg_R_g = np.mean(radii_of_gyration)

# Plot one example of the chain
example_chain = np.zeros((N, 3))
directions = np.random.randn(N, 3)
directions /= np.linalg.norm(directions, axis=1)[:, np.newaxis]

for i in range(1, N):
    example_chain[i] = example_chain[i - 1] + b * directions[i]

# Plot the ideal chain
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(example_chain[:, 0], example_chain[:, 1], example_chain[:, 2], marker='o', markersize=3)
ax.set_title("Ideal Chain Simulation")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
