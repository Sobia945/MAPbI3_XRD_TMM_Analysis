import matplotlib.pyplot as plt

# Data from XRD analysis
peaks = [1, 2, 3]
two_theta = [14.02, 28.42, 31.85]
d_spacing = [0.6312, 0.3138, 0.2807]
crystallite_size = [55.73, 47.55, 43.14]

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot 1 - d-spacing
ax1.bar(peaks, d_spacing, width=0.5)
ax1.set_title("d-Spacing vs Peak")
ax1.set_xlabel("Peak Number")
ax1.set_ylabel("d-Spacing (nm)")
ax1.set_xticks(peaks)

# Plot 2 - Crystallite Size
ax2.bar(peaks, crystallite_size, width=0.5)
ax2.set_title("Crystallite Size vs Peak")
ax2.set_xlabel("Peak Number")
ax2.set_ylabel("Crystallite Size (nm)")
ax2.set_xticks(peaks)

# Overall title
plt.suptitle("MAPbI3 XRD Analysis", fontsize=14, fontweight="bold")

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig("xrd_plot.png", dpi=300)

# Display figure
plt.show()

print("Plot saved as xrd_plot.png")
