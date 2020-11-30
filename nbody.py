import threading
import math
import random as rand
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ran = False

def run_simulation(count, fig_index, target_frame, write_video, skip, frame_count=200):
    particles = []

    def main(n_particles, rand_dist):
        #global particles
        #particles = []

        if (rand_dist):
            rand.seed()
            for i in range(n_particles):
                _pos = [rand.random()*1, rand.random()*1] # -> float between 0 and 100 for x and y respectively
                _mass = 0.25 # -> mass between 1-5 float
                _vel = [0.0, 0.0]
                particles.append(p(_pos, _mass, _vel))
        else:
            for i in range(round(pow(n_particles, 0.5))):
                for j in range(round(pow(n_particles, 0.5))):
                    _pos = [(10 * i - 2 + rand.random()*4)/10, (10 * j - 2 + rand.random()*4)/10] # -> Grid spacing 0 - 100
                    _mass = 1 # -> mass between 1-5 float
                    _vel = [0, 0]
                    particles.append(p(_pos, _mass, _vel))

        # lets get things moving by stepping the shit outta it
        #for i in range(3000):
        #    print(i)
        #    step(particles, 0.001)

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
      return [pos, mass, vel]

    global ran
    ran = False

    def animate(i):
        global ran
        #global fig
        #global count
        #global fig_index
        #global target_frame
        if (skip):
            skip_steps = target_frame - 1
        else:
            skip_steps = 0
        data = step(particles, 0.001)

        ax1.clear()
        ax1.scatter(x=data[0], y=data[1], cmap=plt.get_cmap("winter"), c=range(count))
        ax1.set_xlim((-20,20))
        ax1.set_ylim((-20,20))

        ax1.set_title("Figure " + str(fig_index) + " Time " + str(skip_steps + i))

        def save_fig():
            print("Writing image" + 'plots/plot-' + str(fig_index) + '-time-' + str(target_frame) + '.png')
            fig.savefig('plots/plot-' + str(fig_index) + '-time-' + str(target_frame) + '.png')
        if (i==target_frame - skip_steps):
            save_fig()
        #print("step",i,"pos:",data[0][0],':',data[0][1])

    main(count, False)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    data = step(particles, 0.001)

    ax1.clear()
    ax1.scatter(x=data[0], y=data[1], cmap=plt.get_cmap("winter"), c=range(count))

    ax1.set_title("Figure " + str(fig_index) + " Time 0")
    fig.savefig('plots/plot-' + str(fig_index) + '-time-0.png')

    # skip n steps
    if (skip):
        for i in range(target_frame - 1):
            step(particles, 0.001)
            print("Skip " + str(i))

    if (write_video):
        ani = animation.FuncAnimation(fig, animate, interval = 9, frames=100, repeat=False)
    else:
        ani = animation.FuncAnimation(fig, animate, interval = 9, frames=100000, repeat=False)

    if (write_video):
        Writer = animation.writers['pillow']
        writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)
        print("Writing video")
        ani.save("plots/plot-animation-" + str(fig_index) + ".webp", writer=writer)
    else:
        plt.show()
    print("Fig " + str(fig_index) + " finished.")

    del fig
    del ax1


#run_simulation(count=100, fig_index=0, target_frame=2500, write_video = True, skip=True, frame_count = 450)

for i in range(5):
    run_simulation(count=100, fig_index=i, target_frame=2500, write_video = True, skip=True, frame_count = 100)
