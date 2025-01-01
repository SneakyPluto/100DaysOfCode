# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below: 
#Step 1, write a function f_to_c
def f_to_c(f_temp):
  temp_c = ((f_temp - 32) * 5/9)
  return temp_c

#Step 2, test function with value of 100F
f100_in_celsius = f_to_c(100)

#Step 3, write a function c_to_f
def c_to_f(c_temp):
   return c_temp * (9/5) + 32

#Step 4 test c_to_f
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#Step 5 define a function get force (AI generated assistance)
def get_force(mass, acceleration):
  if not isinstance(mass, (int, float)) or not isinstance(acceleration, (int, float)):
    raise ValueError("Mass and acceleration must be numbers.")
  return mass * acceleration

#Step 6 test get force
train_force = get_force(train_mass, train_acceleration)

#Step 7 string interpolation
print(f"The GE train supplies {train_force}.\n")

#Step 8 define get_energy
def get_energy(mass, c):
  return mass * c**2

#Step 9 Test get_enegry wwith bomb_mass
bomb_energy = get_energy(bomb_mass, c)

#Step 10 string interpolation
print(f"A 1kg bomb supplies {bomb_energy} Joules.\n")

#Step 11 final function get_work
def get_work(mass, acceleration, displacement):
  return get_force(mass, acceleration) * displacement

#Step 12 test get_work
train_work = get_work(train_mass, train_acceleration, train_distance)

#Step 13
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.\n")
