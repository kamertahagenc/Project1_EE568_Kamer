import femm
import math
import matplotlib.pyplot as plt
from PIL import Image
import os


# --- INITIALIZATION ---
femm.openfemm()
femm.newdocument(0)
femm.mi_probdef(0, 'millimeters', 'planar', 1e-8, 25, 30)

# --- 1. DEFINE MATERIALS & CIRCUITS ---
femm.mi_addmaterial('Air', 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0)
femm.mi_addmaterial('M19 Steel', 4416, 4416, 0, 0, 0, 0, 0, 1, 0, 0, 0)
femm.mi_addmaterial('Copper', 1, 1, 0, 0, 59, 0, 0, 1, 0, 0, 0)
femm.mi_addcircprop('Coil', 2.5, 1)

# --- 2. ADD ALL NODES ---
# Stator Outer Boundary
femm.mi_addnode(60, 25)
femm.mi_addnode(60, 0)
femm.mi_addnode(0, 0)
femm.mi_addnode(0, 70)
femm.mi_addnode(60, 70)
femm.mi_addnode(60, 45)

# Stator Inner Window
femm.mi_addnode(45, 25)
femm.mi_addnode(45, 15)
femm.mi_addnode(15, 15)
femm.mi_addnode(15, 55)
femm.mi_addnode(45, 55)
femm.mi_addnode(45, 45)

# Coil Nodes
femm.mi_addnode(15, 20)
femm.mi_addnode(25, 20)
femm.mi_addnode(25, 50)
femm.mi_addnode(15, 50)

femm.mi_addnode(0, 20)
femm.mi_addnode(0, 50)
femm.mi_addnode(-10, 50)
femm.mi_addnode(-10, 20)

# Rotor Nodes
femm.mi_addnode(60, 25.63)
femm.mi_addnode(60, 28.13)
femm.mi_addnode(60, 41.87)
femm.mi_addnode(60, 44.37)
femm.mi_addnode(45, 44.37)
femm.mi_addnode(45, 41.87)
femm.mi_addnode(45, 28.13)
femm.mi_addnode(45, 25.63)

# --- 3. DRAW SEGMENTS AND ARCS ---
# Stator perimeter
femm.mi_addsegment(60, 25, 60, 0)
femm.mi_addsegment(60, 0, 0, 0)
femm.mi_addsegment(0, 0, 0, 70)
femm.mi_addsegment(0, 70, 60, 70)
femm.mi_addsegment(60, 70, 60, 45)

# Stator inner window
femm.mi_addsegment(45, 25, 45, 15)
femm.mi_addsegment(45, 15, 15, 15)
femm.mi_addsegment(15, 15, 15, 55)
femm.mi_addsegment(15, 55, 45, 55)
femm.mi_addsegment(45, 55, 45, 45)

# Stator Bore Arcs
femm.mi_addarc(60, 45, 45, 45, 73.74, 0.5)
femm.mi_addarc(45, 25, 60, 25, 73.74, 0.5)

# Right Coil
femm.mi_addsegment(15, 20, 25, 20)
femm.mi_addsegment(25, 20, 25, 50)
femm.mi_addsegment(25, 50, 15, 50)
femm.mi_addsegment(15, 50, 15, 20)

# Left Coil
femm.mi_addsegment(0, 20, 0, 50)
femm.mi_addsegment(0, 50, -10, 50)
femm.mi_addsegment(-10, 50, -10, 20)
femm.mi_addsegment(-10, 20, 0, 20)

# Rotor
femm.mi_addsegment(60, 25.63, 60, 28.13)
femm.mi_addarc(60, 28.13, 60, 41.87, 84.96, 0.5)
femm.mi_addsegment(60, 41.87, 60, 44.37)
femm.mi_addarc(60, 44.37, 45, 44.37, 77.36, 0.5)
femm.mi_addsegment(45, 44.37, 45, 41.87)
femm.mi_addarc(45, 41.87, 45, 28.13, 84.96, 0.5)
femm.mi_addsegment(45, 28.13, 45, 25.63)
femm.mi_addarc(45, 25.63, 60, 25.63, 77.36, 0.5)

# Boundary
femm.mi_addnode(-70, 35)
femm.mi_addnode(130, 35)
femm.mi_addarc(-70, 35, 130, 35, 180, 0.5)
femm.mi_addarc(130, 35, -70, 35, 180, 0.5)

femm.mi_addboundprop('Zero_Flux', 0, 0, 0, 0, 0, 0, 0, 0, 0)

femm.mi_selectarcsegment(-70, 35)
femm.mi_selectarcsegment(130, 35)

femm.mi_setarcsegmentprop(2, 'Zero_Flux', 0, 0)

femm.mi_clearselected()

# Part Labels
# Air
femm.mi_addblocklabel(-30, -30)
femm.mi_selectlabel(-30, -30)
femm.mi_setblockprop('Air', 1, 0, '<None>', 0, 0, 0)
femm.mi_clearselected()

# Stator
femm.mi_addblocklabel(8, 8)
femm.mi_selectlabel(8, 8)
femm.mi_setblockprop('M19 Steel', 1, 0, '<None>', 0, 0, 0)
femm.mi_clearselected()

# Rotor
femm.mi_addblocklabel(52.5, 35)
femm.mi_selectlabel(52.5, 35)
femm.mi_setblockprop('M19 Steel', 1, 0, '<None>', 0, 0, 0)
femm.mi_clearselected()

# Left Coil
femm.mi_addblocklabel(-5, 30)
femm.mi_selectlabel(-5, 30)
femm.mi_setblockprop('Copper', 1, 0, 'Coil', 0, 0, 300)
femm.mi_clearselected()

# Right Coil
femm.mi_addblocklabel(20, 30)
femm.mi_selectlabel(20, 30)
femm.mi_setblockprop('Copper', 1, 0, 'Coil', 0, 0, -300)
femm.mi_clearselected()

"""
# Rotating Rotor
femm.mi_selectcircle(52.5, 35, 12.2, 4)
femm.mi_moverotate(52.5, 35, 90)
femm.mi_clearselected()
"""




print("Cleaning old image files...")
for angle in range(-90, 95, 5):
    filename = f"frame_{angle}.bmp"
    if os.path.exists(filename):
        os.remove(filename)

# --- AUTOMATED TORQUE & INDUCTANCE CALCULATION (-90 to +90) ---
print("Calculating Torque and Inductance. Please wait...\n")

cx = 52.5
cy = 35
current = 2.5 # The current you defined in your circuit

# 1. Create empty lists for our data
calculated_angles = []
calculated_torques = []
calculated_inductances = [] # New list for FEA Inductance

femm.mi_saveas('motor_temp2.fem')

for angle in range(-90, 95, 5): # Increased to 95 to include exactly 90 degrees

    # Select the perfectly 0-degree rotor
    femm.mi_selectcircle(cx, cy, 12.2, 0)
    femm.mi_selectcircle(cx, cy, 12.2, 1)
    femm.mi_selectcircle(cx, cy, 12.2, 2)
    femm.mi_selectcircle(cx, cy, 12.2, 3)

    # Rotate to our test angle
    femm.mi_moverotate(cx, cy, angle)
    femm.mi_clearselected()

    # Save, solve, and load results
    femm.mi_saveas('motor_temp2.fem')
    femm.mi_analyze(1)
    femm.mi_loadsolution()

    # --- NEW: TAKE A PICTURE FOR THE GIF ---
    # Turn on the color map (0 to 2.0 Tesla)
    femm.main_resize(1360, 800)
    femm.mo_showdensityplot(1, 0, 1.8, 0, 'bmag')
    femm.mo_zoom(-20, -15, 80, 85)
    # Save the frame as a bitmap image
    femm.mo_savebitmap(f"frame_{angle}.bmp")
    # ---------------------------------------

    # Calculate FEA Torque
    femm.mo_clearblock()
    femm.mo_selectblock(cx, cy)
    torque = femm.mo_blockintegral(22)

    # --- PYFEMM BUG FIX ---
    # If the mesh splits exactly down the middle and returns a list, force it back to a float
    if isinstance(torque, (list, tuple)):
        torque = torque[0] if len(torque) > 0 else 0.0
    # ----------------------

    # Calculate FEA Inductance (L = Flux Linkage / Current)
    # mo_getcircuitproperties returns [current, voltage, flux_linkage]
    circ_props = femm.mo_getcircuitproperties('Coil')
    flux_linkage = circ_props[2]
    inductance_H = flux_linkage / current
    inductance_mH = inductance_H * 1000 # Convert Henrys to milliHenrys

    print(f"Angle: {angle:>3} degrees | Torque: {torque:6.3f} N.m | Inductance: {inductance_mH:6.2f} mH")

    # Store the calculated numbers!
    calculated_angles.append(angle)
    calculated_torques.append(torque)
    calculated_inductances.append(inductance_mH)

    femm.mo_close()

    # Restore the rotor to exactly 0 degrees for the next loop
    femm.mi_selectcircle(cx, cy, 12.2, 0)
    femm.mi_selectcircle(cx, cy, 12.2, 1)
    femm.mi_selectcircle(cx, cy, 12.2, 2)
    femm.mi_selectcircle(cx, cy, 12.2, 3)
    femm.mi_moverotate(cx, cy, -angle)
    femm.mi_clearselected()

print("\nSweep Complete! Generating Graphs...")

# --- AUTOMATIC GRAPH GENERATION ---
# Calculate the analytical arrays to match the FEA angles
calc_ana_torque = []
calc_ana_inductance = []

for a in calculated_angles:
    rad = math.radians(a)
    # T = -0.114 * sin(2*theta)
    calc_ana_torque.append(-0.114 * math.sin(2 * rad))
    # L = 27.5 + 18.3 * cos(2*theta)
    calc_ana_inductance.append(27.5 + 18.3 * math.cos(2 * rad))

# Create a figure with 2 stacked subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

# Top Subplot: Torque
ax1.plot(calculated_angles, calculated_torques, marker='o', linestyle='-', color='b', label='FEA Torque')
ax1.plot(calculated_angles, calc_ana_torque, marker='', linestyle='--', color='r', linewidth=2, label='Analytical Torque')
ax1.set_title("Motor Torque vs. Rotor Angle")
ax1.set_ylabel("Torque (N·m)")
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.axhline(0, color='black', linewidth=1)
ax1.axvline(0, color='black', linewidth=1)
ax1.legend()

# Bottom Subplot: Inductance
ax2.plot(calculated_angles, calculated_inductances, marker='o', linestyle='-', color='g', label='FEA Inductance')
ax2.plot(calculated_angles, calc_ana_inductance, marker='', linestyle='--', color='orange', linewidth=2, label='Analytical Inductance')
ax2.set_title("Phase Inductance vs. Rotor Angle")
ax2.set_xlabel("Rotor Angle (Degrees)")
ax2.set_ylabel("Inductance (mH)")
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.axvline(0, color='black', linewidth=1)
ax2.legend()

plt.tight_layout()
plt.show()


print("\nStitching images into an animated GIF...")

frames = []
# Loop through the exact same angles you used to calculate
for angle in range(-90, 95, 5):
    filename = f"frame_{angle}.bmp"
    # If the file exists, open it and add it to our frame list
    if os.path.exists(filename):
        frames.append(Image.open(filename))

# Save the frames as a looping GIF
if len(frames) > 0:
    # duration=150 means 150 milliseconds per frame. Lower = faster spin!
    frames[0].save('motor_rotation.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=150,
                   loop=0)
    print("Success! 'motor_rotation.gif' has been saved to your folder.")

# Clean up: Delete all the temporary .bmp images
for angle in range(-90, 95, 5):
    filename = f"frame_{angle}.bmp"
    if os.path.exists(filename):
        os.remove(filename)
