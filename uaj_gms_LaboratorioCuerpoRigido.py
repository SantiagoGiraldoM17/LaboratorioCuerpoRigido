import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# Load the angle data
angle_data_path = 'Datos/06_jntAng_240318_ACT_time_jntAngles_75.txt'
angle_data = pd.read_csv(angle_data_path, header=None, usecols=[0, 5], names=['time', 'angle'])

# Load the x, y, z data
xyz_data_path = 'Datos/06_jntAng_240318_ACT_time_x_y_z_75.txt'
xyz_data = pd.read_csv(xyz_data_path, header=None, names=['time', 'x', 'y', 'z'])

# Calculate angular velocity and acceleration
angle_data['angular_velocity'] = np.deg2rad(angle_data['angle'].diff().fillna(0)) / angle_data['time'].diff()
angle_data['angular_acceleration'] = angle_data['angular_velocity'].diff() / angle_data['time'].diff()

# Calculate velocities Vx, Vy, Vz 
xyz_data['Vx'] = xyz_data['x'].diff() / xyz_data['time'].diff()
xyz_data['Vy'] = xyz_data['y'].diff() / xyz_data['time'].diff()
xyz_data['Vz'] = xyz_data['z'].diff() / xyz_data['time'].diff()

# Fixed point
fixed_x = 930
fixed_z = 1320

# Calculate radius
xyz_data['radius_x'] = xyz_data['x'] - fixed_x
xyz_data['radius_z'] = xyz_data['z'] - fixed_z



# Calculate velocities using angular velocity * radius
xyz_data['Vx_radius'] = angle_data['angular_velocity'] * xyz_data['radius_z']
xyz_data['Vz_radius'] = angle_data['angular_velocity'] * -xyz_data['radius_x']

# Calculate accelerations for both methods
xyz_data['Ax'] = xyz_data['Vx'].diff() / xyz_data['time'].diff()
xyz_data['Az'] = xyz_data['Vz'].diff() / xyz_data['time'].diff()
xyz_data['Ax_radius'] = xyz_data['Vx_radius'].diff() / xyz_data['time'].diff()
xyz_data['Az_radius'] = xyz_data['Vz_radius'].diff() / xyz_data['time'].diff()

# Plotting

# Plotting the 3D and 2D Trajectories
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(xyz_data['x'], xyz_data['y'], xyz_data['z'], label='Trajectory', color='b')
ax1.set_title('Trayectoria 3D')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend()
ax2 = fig.add_subplot(122)
ax2.plot(xyz_data['x'], xyz_data['z'], label='Trajectory', color='r')
ax2.set_title('Trayectoria 2D (Plano X-Z)')
ax2.set_xlabel('X')
ax2.set_ylabel('Z')
ax2.legend()
plt.tight_layout()
plt.savefig('Graficas/Trayectorias.png')
#plt.show()

# Plotting Angular Velocity and Acceleration
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
ax[0].plot(angle_data['time'], angle_data['angular_velocity'], label='Velocidad Angular', color='green')
ax[0].set_title('Velocidad Angular')
ax[0].set_xlabel('Tiempo (s)')
ax[0].set_ylabel('Velocidad Angular (rad/s)')
ax[0].legend()
ax[1].plot(angle_data['time'], angle_data['angular_acceleration'], label='Aceleracion Angular', color='purple')
ax[1].set_title('Aceleracion Angular')
ax[1].set_xlabel('Tiempo (s)')
ax[1].set_ylabel('Aceleracion Angular (rad/s^2)')
ax[1].legend()
plt.tight_layout()
plt.savefig("Graficas/Angular.png")
#plt.show()

# Plotting Comparison of Velocities (Vx and Vz)
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
ax[0].plot(xyz_data['time'], xyz_data['Vx'], label='Vx Numerica', color='blue', linestyle='--')
ax[0].plot(xyz_data['time'], xyz_data['Vx_radius'], label='Vx Radio', color='green', linestyle='-')
ax[0].set_title('Comparacion de Velocidad en X (Vx)')
ax[0].set_xlabel('Tiempo (s)')
ax[0].set_ylabel('Velocidad (unidades/s)')
ax[0].legend()
ax[1].plot(xyz_data['time'], xyz_data['Vz'], label='Vz Numerica', color='red', linestyle='--')
ax[1].plot(xyz_data['time'], xyz_data['Vz_radius'], label='Vz Radio', color='purple', linestyle='-')
ax[1].set_title('Comparacion de Velocidad en Z (Vz)')
ax[1].set_xlabel('Tiempo (s)')
ax[1].set_ylabel('Velocidad (unidades/s)')
ax[1].legend()
plt.tight_layout()
plt.savefig("Graficas/Velocidades.png")
#plt.show()

# Plotting Comparison of Accelerations (Ax and Az)
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
ax[0].plot(xyz_data['time'], xyz_data['Ax'], label='Ax Numerica', color='blue', linestyle='--')
ax[0].plot(xyz_data['time'], xyz_data['Ax_radius'], label='Ax Radio', color='green', linestyle='-')
ax[0].set_title('Comparacion de Aceleracion en X (Ax)')
ax[0].set_xlabel('Tiempo (s)')
ax[0].set_ylabel('Aceleracion (unidades/s^2)')
ax[0].legend()
ax[1].plot(xyz_data['time'], xyz_data['Az'], label='Az Numerica', color='red', linestyle='--')
ax[1].plot(xyz_data['time'], xyz_data['Az_radius'], label='Az Radio', color='purple', linestyle='-')
ax[1].set_title('Comparison of Acceleration in Z direction (Az)')
ax[1].set_xlabel('Tiempo (s)')
ax[1].set_ylabel('Aceleracion (unidades/s^2)')
ax[1].legend()
plt.tight_layout()
plt.savefig("Graficas/Aceleraciones.png")
#plt.show()

specific_time = 0.408
specific_data_xyz = xyz_data.loc[xyz_data['time'] == specific_time]
specific_data_angle = angle_data.loc[angle_data['time'] == specific_time]

# Convert the queried data to a string with a descriptive header
data_string = "Data at time = {} seconds\n\nXYZ Data:\n{}\n\nAngle Data:\n{}".format(
    specific_time, specific_data_xyz.to_string(index=False), specific_data_angle.to_string(index=False))

# Define the filename
filename = "Graficas/data_at_time_{}.txt".format(specific_time)

# Write to a text file
with open(filename, 'w') as file:
    file.write(data_string)

# Extract data for the specific time
specific_row = xyz_data.loc[xyz_data['time'] == specific_time].iloc[0]

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the entire trajectory with dotted lines
ax.plot(xyz_data['x'], xyz_data['z'], linestyle=':', color='gray', label='Trayectoria')

# Mark the position of the end effector at the specific time
ax.scatter(specific_row['x'], specific_row['z'], color='blue', label='Posicion en t={}s'.format(specific_time))

# Plot velocity vector at the specific time
ax.quiver(specific_row['x'], specific_row['z'], specific_row['Vx_radius'], specific_row['Vz_radius'], color='green', scale=2000, width=0.004, label='Velocidad')

# Plot acceleration vector at the specific time
ax.quiver(specific_row['x'], specific_row['z'], specific_row['Ax_radius'], specific_row['Az_radius'], color='red', scale=5000, width=0.004, label='Aceleracion')

# Setting the plot
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_title('Trayectoria con Vectores de Velocidad y Aceleracion cuando t = {}s'.format(specific_time))
ax.legend()

plt.grid(True)
plt.axis('equal')
plt.savefig("Graficas/Vectores.png")
plt.show()


# Prepare the figure and axis for the animation
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(xyz_data['x'], xyz_data['z'], linestyle=':', color='gray', label='Trayectoria')
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.grid(True)
ax.axis('equal')

# Initial placeholders for the position, velocity, and acceleration vectors
point, = ax.plot([], [], 'bo', label='Posicion')
velocity = ax.quiver([], [], [], [], color='green', scale=2000, width=0.004, label='Velocidad')
acceleration = ax.quiver([], [], [], [], color='red', scale=5000, width=0.004, label='Acceleracion')

# Initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    velocity.set_UVC([], [])
    acceleration.set_UVC([], [])
    return point, velocity, acceleration

# Animation function: this is called sequentially
def animate(i):
    x = xyz_data.iloc[i]['x']
    z = xyz_data.iloc[i]['z']
    vx = xyz_data.iloc[i]['Vx_radius']
    vz = xyz_data.iloc[i]['Vz_radius']
    ax = xyz_data.iloc[i]['Ax_radius']
    az = xyz_data.iloc[i]['Az_radius']
    
    point.set_data(x, z)
    velocity.set_offsets([x, z])
    velocity.set_UVC(vx, vz)
    acceleration.set_offsets([x, z])
    acceleration.set_UVC(ax, az)
    
    return point, velocity, acceleration

# Create animation
ani = FuncAnimation(fig, animate, frames=len(xyz_data), init_func=init, blit=True, interval=50)


# To save the animation as an mp4 file
ani.save('Graficas/Animacion_Vectores.gif', fps=20, writer="pillow")

plt.legend()
plt.show()
