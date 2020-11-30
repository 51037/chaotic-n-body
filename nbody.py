import random as rand
import matplotlib.pyplot as plt
import matplotlib.animation as animation

p_pos = []
p_mass = []
particles = []

def main(n_particles):

    p_x_positions = []
    p_y_positions = []

    rand.seed(0)
    global particles
    for i in range(n_particles):
        _pos = [rand.random()*1, rand.random()*1] # -> float between 0 and 100 for x and y respectively
        _mass = 0.25 # -> mass between 1-5 float
        _vel = [0.0, 0.0]
        particles.append(p(_pos, _mass, _vel))

    # lets get things moving by stepping the shit outta it
    #for i in range(1000):
    #    print(i)
    #    step(particles, 0.1)

def animate(i):
    global count
    data = step(particles, 0.001)

    ax1.clear()
    ax1.scatter(x=data[0], y=data[1], cmap=plt.get_cmap("winter"), c=range(count))
    print("step",i,"pos:",data[0][0],':',data[0][1])


# F = ma
# a = F/m
# v = integral a dt -> F/m * t
# x = integral v dt -> 1/2 * F/m * t^2
# half step kick from medium:
# v = v + delta_t / 2 * a
# x = x + delta_t * v -> full step drift for position change

def kick(vals, del_t, kick_amt):
    return vals[0] + del_t * kick_amt * vals[1]

def compute_acceleration(p_index, particles):
    G = 1.0
    #soft = 0.000000000000000000001
    soft  = 0.1
    x_sum = 0.0
    y_sum = 0.0
    for i in range(len(particles)):
        mass = particles[i][1]
        dist = ( pow( pow(particles[i][0][0] - particles[p_index][0][0], 2) + pow(particles[i][0][1] - particles[p_index][0][1], 2) + pow(soft, 2), 0.5) )

        unit_dist = [ particles[i][0][0] - particles[p_index][0][0] / dist, particles[i][0][1] - particles[p_index][0][1] / dist ]
        #G   *   mass  *
        x_sum += G*(mass)*(unit_dist[0])/pow(dist,2)
        y_sum += G*(mass)*(unit_dist[1])/pow(dist,2)

    return (x_sum, y_sum)

def step(particles, amt):
  for i in range(len(particles)):
      p = particles[i]
      _acc = compute_acceleration(i, particles)

      p[2][0] = kick((p[2][0], _acc[0]), amt, 0.5)
      p[2][1] = kick((p[2][1], _acc[1]), amt, 0.5)

  for p in particles:
      p[0][0] = kick((p[0][0], p[2][0]), amt, 1)
      p[0][1] = kick((p[0][1], p[2][1]), amt, 1)

  x_arr = []
  y_arr = []
  for p in particles:
      x_arr.append(p[0][0])
      y_arr.append(p[0][1])
  return (x_arr, y_arr)

def p(pos, mass, vel):
  global p_pos
  global p_mass
  p_pos.append(pos)
  p_mass.append(mass)

  return [pos, mass, vel]

count = 9
main(count)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ani = animation.FuncAnimation(fig, animate, interval = 17, frames=100000)
plt.show()
