import math
import matplotlib.pyplot as plt

f = open('data.txt').readlines()
hh = []
for i in f:
    h = float(i.split(': ')[1].strip())
    hh.append(h)
    if h > 60000:
        break

g = 9.81
theta_0 = 90
tau = 87
t_end = 360
dt = 1


def F(t):
    if t <= 101:
        return 6075 * 1000
    else:
        return 2025 * 1000


def theta(t, h=-1):
    if h < 1000:
        return math.radians(90)
    return math.radians(theta_0 * math.exp(-t / tau))


def m(t):
    m0 = 403000
    m1 = 155000
    if t <= 100:
        return m0 - 1960 * t
    else:
        return m1 - 653 * (t - 100)


h = 0
v_y = 0
v_x = 0
x = 0

# Симуляция
heights = [h]
for t in range(0, t_end, dt):
    thrust = F(t)
    angle = theta(t, h)
    mass = m(t)
    a_y = (thrust * math.sin(angle) - mass * g) / mass
    v_y += a_y * dt
    h += v_y * dt

    heights.append(h)
    if h > 60000:
        break

while len(heights) < len(hh):
    heights.append(heights[-1])

print(sum([abs(heights[i] - hh[i]) / hh[i] for i in range(len(hh))]) / len(hh))
plt.plot(heights)
plt.plot(hh)
plt.legend(('Моделирование', 'KSP сиимуляция'))
plt.show()
