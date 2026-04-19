import femm
import math
import matplotlib.pyplot as plt

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








# --- AUTOMATED TORQUE CALCULATION (-50 to +45) ---
print("Calculating Torque. Please wait...\n")

cx = 52.5
cy = 35

# 1. Create empty lists to store our real-time calculated data
calculated_angles = []
calculated_torques = []

# Save the starting 0-degree model once so it has a file to write to
femm.mi_saveas('motor_temp2.fem')

for angle in range(-90, 90, 5):

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

    # Calculate Torque
    femm.mo_clearblock()
    femm.mo_selectblock(cx, cy)
    torque = femm.mo_blockintegral(22)

    print(f"Angle: {angle:>3} degrees | Torque: {torque:.3f} N.m")

    # 2. Store the calculated numbers into our lists!
    calculated_angles.append(angle)
    calculated_torques.append(torque)

    femm.mo_close()

    # Restore the rotor to exactly 0 degrees for the next loop
    femm.mi_selectcircle(cx, cy, 12.2, 0)
    femm.mi_selectcircle(cx, cy, 12.2, 1)
    femm.mi_selectcircle(cx, cy, 12.2, 2)
    femm.mi_selectcircle(cx, cy, 12.2, 3)
    femm.mi_moverotate(cx, cy, -angle)
    femm.mi_clearselected()

print("\nSweep Complete! Generating Graph...")

# --- AUTOMATIC GRAPH GENERATION ---
plt.figure(figsize=(8, 5))

# Plot the real data we just calculated
plt.plot(calculated_angles, calculated_torques, marker='o', linestyle='-', color='b', label='FEA Torque')

# Professional formatting
plt.title("Variable Reluctance Motor: Torque vs. Rotor Angle")
plt.xlabel("Rotor Angle (Degrees)")
plt.ylabel("Torque (N·m)")
plt.grid(True, linestyle='--', alpha=0.7)

# Draw bold lines for the X and Y zero-axes to highlight the exact center
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.legend()
plt.tight_layout()

# Instantly show the graph to the user
plt.show()







femm.mi_zoomnatural()
