import math
import matplotlib.pyplot as plt

# Generate angles from -180 to 180 degrees
angles = list(range(-180, 181, 1))

# Calculate the analytical torque: T = -0.114 * sin(2 * theta)
torques = []
for angle in angles:
    # Convert degree to radian for the math.sin() function
    rad = math.radians(angle)
    t = -0.114 * math.sin(2 * rad)
    torques.append(t)

# --- GRAPH GENERATION ---
plt.figure(figsize=(10, 5))

# Plot the pure analytical wave
plt.plot(angles, torques, color='red', linewidth=2, label='T = -0.114 * sin(2θ)')

# Formatting the graph
plt.title("Pure Analytical Torque Profile (-180° to 180°)")
plt.xlabel("Rotor Angle (Degrees)")
plt.ylabel("Torque (N·m)")
plt.grid(True, linestyle='--', alpha=0.7)

# Set the X-axis ticks to show up every 45 degrees for better readability
plt.xticks(range(-180, 181, 45))

# Draw bold lines for the X and Y zero-axes
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.legend()
plt.tight_layout()

# Show the graph
plt.show()
