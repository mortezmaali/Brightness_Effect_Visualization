import cv2
import numpy as np

# Define the Macbeth Color Checker colors in RGB
macbeth_colors = np.array([
    [115, 82, 68], [194, 150, 130], [98, 122, 157], [87, 108, 67], [133, 128, 177], [103, 189, 170],
    [214, 126, 44], [80, 91, 166], [193, 90, 99], [94, 60, 108], [157, 188, 64], [224, 163, 46],
    [56, 61, 150], [70, 148, 73], [175, 54, 60], [231, 199, 31], [187, 86, 149], [8, 133, 161],
    [243, 243, 242], [200, 200, 200], [160, 160, 160], [122, 122, 121], [85, 85, 85], [52, 52, 52]
], dtype=np.uint8)

# Define the size of each patch, border, and the checkerboard size
patch_size = 50
border_size = 5  # Size of the black border between patches
rows, cols = 4, 6
checkerboard_size = (
    rows * (patch_size + border_size) + border_size, 
    cols * (patch_size + border_size) + border_size, 
    3
)

# Initialize the checkerboard with black background (for borders)
checkerboard = np.zeros(checkerboard_size, dtype=np.uint8)

# Fill the checkerboard with colors and black borders
for i in range(rows):
    for j in range(cols):
        color = macbeth_colors[i * cols + j]
        start_row = i * (patch_size + border_size) + border_size
        start_col = j * (patch_size + border_size) + border_size
        checkerboard[start_row:start_row + patch_size, start_col:start_col + patch_size] = color

# Video writer initialization
output_file = 'macbeth_brightness_variation_with_borders_faster.mp4'
fps = 0.5  # Faster frames per second, showing each brightness level for 1 second
height, width, _ = checkerboard.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Varying brightness levels
brightness_levels = np.linspace(0.1, 2.0, num=20)  # From 10% to 200% brightness with fewer steps

for brightness in brightness_levels:
    bright_checkerboard = np.clip(checkerboard * brightness, 0, 255).astype(np.uint8)
    out.write(bright_checkerboard)

# Release the video writer
out.release()

print(f"Video saved as {output_file}")
