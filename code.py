import math
import matplotlib.pyplot as plt


f = open('data.txt').readlines()
hh = []
for i in f:
    h = float(i.split(': ')[1].strip())
    hh.append(h)
    if h > 60000:
        break
print(hh)

g = 9.81
theta_0 = 90
tau = 900
t_end = 420
dt = 1



def F(t):
    if t <= 101:
        return 6075 * 1000
    else:
        return 2425 * 1000



def theta(t, h=-1):
    if h < 1000:
        return math.radians(90)
    return math.radians(theta_0 * math.exp(-t / tau))



def m(t):
    m0 = 403000  # начальная масса ракеты, кг
    if t <= 100:
        return m0 - 1.96 * t
    else:
        return m(100) - 0.653 * (t - 100)



# Начальные условия
h = 0
v_y = 0
v_x = 0
x = 0

# Симуляция
heights = [h]
xs = [x]
for t in range(0, t_end, dt):
    thrust = F(t)
    angle = theta(t, h)
    mass = m(t)
    a_y = (thrust * math.sin(angle) - mass * g) / mass
    a_x = (thrust * math.cos(angle)) / mass

    v_y += a_y * dt
    v_x += a_x * dt
    h += v_y * dt
    x += v_x * dt

    heights.append(h)
    xs.append(x)
    print(t, thrust, math.degrees(angle), mass, h, v_y)
    if h > 60000:
        break
print("Высота ракеты с течением времени:", heights)
plt.plot(heights)
plt.plot(hh)
plt.show()
