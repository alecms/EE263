import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

# This defines 20 discrete wavelengths
# wavelength =3D 380:20:760; #(nm)
wavelength = np.arange(380, 780, 20)




# Define the vectors of cone responsiveness
# Cone sensitivies for wavelengths in the visible range.  This data is=20
#  based on a graph on page 93 in Wandell's "Foundations of Vision"=20

L_cone_log = np.array([-.9, -1.1, -1, -.8, -.7, -.6, -.5, -.4, -.3, -.25, -.3,
                       -.4, -.8, -1.2, -1.6, -1.9, -2.4, -2.8, -3.6, -4], dtype = float)

M_cone_log = np.array([-.8, -.85, -.85, -.6, -.5, -.4, -.3, -.2, -.1, -.15,
    -.3 , -.7, -1.2, -1.7, -2.2, -2.9, -3.5, -4.2, -4.8, -5.5], dtype = float)

S_cone_log = np.array([-.4, -.3, -.2, -.1, -.3, -.6, -1.2, -1.8, -2.5, -3.2 , -4.1, 
    -5, -6, -7, -8, -9, -10, -10.5, -11, -11.5], dtype = float)

# Raise everything to the 10 power to get the actual responsitivies.
# These vectors contain the coefficients l_i, m_i, and s_i described in
# the problem statement from shortest to longest wavelength.
L_coefficients = 10. ** L_cone_log
M_coefficients = 10. ** M_cone_log
S_coefficients = 10. ** S_cone_log


# Plot the cone responsiveness.
fig = plt.figure(figsize=(17,8))
ax = fig.add_subplot(111)

ax.plot(wavelength, L_cone_log, label='L cones', linestyle = '-', marker='*')
ax.plot(wavelength, M_cone_log, label='M cones', linestyle = '--', marker = 'x')
ax.plot(wavelength, S_cone_log, label='S cones', linestyle = '-', marker = 'o')
ax.set_xlabel('Light Wavelength (nm)');
ax.set_ylabel('Log Relative Sensitivity');
ax.legend(loc=3)
ax.set_title('Approximate Human Cone Sensitivities')
plt.show()

# Spectral Power Distribution of phosphors from shortest to longest wavelength
B_phosphor = np.array([30, 35, 45, 75, 90, 100, 90, 75, 45, 35, 30, 26, 23, 21, 20, 19, 18, 17, 16, 15], dtype = float)
G_phosphor = np.array([21, 23, 26, 30, 35, 45, 75, 90, 100, 90, 75, 45, 35, 30, 26, 23, 21, 20, 19, 18], dtype = float)
R_phosphor = np.array([15, 16, 17, 18, 19, 21, 23, 26, 30, 35, 45, 75, 90, 100, 90, 75, 45, 35, 30, 26], dtype = float)


#Plot the phosphors
fig = plt.figure(figsize=(17,8))
ax = fig.add_subplot(111)

ax.plot(wavelength, B_phosphor, label='B phosphor', linestyle = '-', marker='*')
ax.plot(wavelength, G_phosphor, label='G phosphor', linestyle = '-', marker = 'o')
ax.plot(wavelength, R_phosphor, label='R phosphor', linestyle = '--', marker = 'x')

ax.set_xlabel('Light Wavelength (nm)');
ax.set_ylabel('Log Relative Sensitivity');
ax.legend(loc=3)
ax.set_title('Spectral Power Distribution of Phosphors')
plt.show()

# This is the spectral power distribution of the test light from the=20
# shortest wavelength to the longest.=20
test_light = np.array([58.2792, 42.3496, 51.5512, 33.3951, 43.2907, 22.5950, 
57.9807, 76.0365,  52.9823, 64.0526, 20.9069,  37.9818,  78.3329,  68.0846, 
46.1095, 56.7829, 79.4211, 5.9183,  60.2869,  5.0269], dtype = float)

#Plot the test light
fig = plt.figure(figsize=(17,8))
ax = fig.add_subplot(111)
ax.plot(wavelength, test_light, linestyle = '-', marker='*')
ax.set_xlabel('Light Wavelength (nm)');
ax.set_ylabel('Spectral Power Distribution of Test Light');
ax.set_title('Test light')
plt.show()

# Define approximate spectrums for sunlight and a tungsten bulb. =20
# The [powers are in order of increasing wavelength
tungsten = np.array([ 20, 30, 40, 50, 60, 70,  80,  90, 100, 110, 120, 130, 
    140, 150, 160, 170, 180, 190, 200, 210], dtype = float)
sunlight = np.array([40, 70, 100, 160, 240, 220,  180, 160, 180, 180, 160, 
    140, 140, 140, 140, 130, 120, 116, 110, 110], dtype = float)

fig = plt.figure(figsize=(17,8))
ax = fig.add_subplot(111)

ax.plot(wavelength, tungsten, label='Tungsten', linestyle = '-', marker='*')
ax.plot(wavelength, sunlight, label='Sunlight', linestyle = '-', marker = 'o')

ax.set_xlabel('Light Wavelength (nm)');
ax.set_ylabel('Spectral Power Distributions');
ax.legend(loc=3)
ax.set_title('Spectral Power Distribution of Light Sources')
plt.show()


# Problem 3.2 c)

t = test_light
C = np.vstack((L_coefficients, M_coefficients, S_coefficients))
P = np.transpose(np.vstack((R_phosphor, G_phosphor, B_phosphor)))
x = np.dot(np.dot(np.linalg.inv(np.dot(C, P)), C), t)
print x 

        

