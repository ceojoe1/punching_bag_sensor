values = []
names = []
def addLog(name, value):
    names.append(name)
    values.append(value)
    # logs.append({name:name, value:value})
    # print(' '.join('{:^12}'.format(*n) for n in enumerate(names)))
    # print(' '.join('{:^12}'.format(*v) for v in enumerate(values)))
 
        # print("{:^12} {:^12} {:^12} {:^12}".format(l = logs))
        # print("{:^12.3f} {:^12.3f} {:^12.3f}".format(a_center_mass, mass_of_bag, sigma_y))
def formattedPrint():
        print(' '.join('{1:^20}'.format(*n) for n in enumerate(names)))
        print(' '.join('{1:^20.2f}'.format(*v) for v in enumerate(values)))




# The general mathematical model of the dynamometric punching bag
# Fr + Q + Fh + m * a = 0
# Fr * r + (sigma) * J = 0

"""
Fr - punching bag's impact reaction force,
Fh - reaction force of suspension ropes,
Q - punching bag's weight force,
Mh - ropes reaction moment,
r - distance of the bag's reaction force from the bag's center mass
m - mass of the bag,
J - moments of inertia against the bag's center mass
a - acceleration of the pupnching bag's center mass
(sigma) - angular acceleration of the punching bag's body against the bag's center of mass
-------
"""

#The method of measuring strike force delivered to a punching bag with an accelerometer
# Fr * r + sigma(y) * J(y) = 0
# Fr + m * a = 0

"""
Fr - punching bag's strike force reaction force,
r - distance of the punching bag's reaction force from the punching bag's center of mass, // Measure the width of the bag / 2
sigma(y) - angular acceleration of the punching bag's body against the punching bag's center of mass in the y-axis
J(y) - moments of inertia against the punching bag's center of mass
m - the mass of the punching bag
a - accerleration of the punching bag's center of mass
"""
weight_of_bag = float(input("Weight of the bag [default: 80] (LBS):") or 80.00) # LBS
height_of_bag = float(input("Height of the bag [default: 6] (Feet):") or 6.00) 
gravity = 9.8 # m/s^2
newtons_per_lb = 4.44822162
# m
mass_of_bag = (weight_of_bag * newtons_per_lb)/gravity # kg
a_t = float(input("Acceleration for top accelerometer [default: 1]:") or 1.00 ) 
a_b = float(input("Acceleration for bottom accelerometer [default: 1]:") or 1.00) 
# a
a_center_mass = float(0.5 * (a_t + a_b))

sigma_y = (a_b - a_t) / height_of_bag

#Strike force
Fr = 0.5 * mass_of_bag * (a_t + a_b) # N

addLog('Acceleration (m/s^2)', a_center_mass)
addLog('Mass (kg)', mass_of_bag)
addLog('Mass (lb)', mass_of_bag * 2.20462262)
addLog('Angular Acceleration', sigma_y)
addLog('Strike Force (N)', Fr)
addLog('Strike Force (LBS)', Fr * 2.20462262)
formattedPrint()
# print("{:^12} {:^12} {:^12} {:^12}".format("Acceleration", "Mass", "Angular Acceleration", "Strike Force"))
# print("{:^12.3f} {:^12.3f} {:^12.3f}".format(a_center_mass, mass_of_bag, sigma_y))