# Chaotic-N-Body

An application of Newton's Universal Law of Gravitation and evaluations of chaotic properties.

![Image should be here](https://raw.githubusercontent.com/51037/chaotic-n-body/main/graphics/overlayed%20data.png)



## Introduction

The picture above is a depiction of three overlaid outputs from `nbody.py`. Each colored point (red, cyan, purple) depicts point particle with *m* mass, *<x, y>* position, and *<x, y>* velocity.
On the left is the initial state of the system, and on the right is the system after 2,500 time steps.

In this system, every particle feels the force as defined by Newton's Law of Universal Gravitation (vector unit vector notation) where $\vec r = {<\Delta x, \Delta y>}$ (the distance between two points):
$$
F=G(m_1*m_2/|r|^2) * (\vec r/{|r|}^2)
$$

While this force is applied to every particle in the system, the above image demonstrates that small, seemingly insignificant changes to the initial conditions of the system drastically impact the system in the future.

Why does a simulation like this matter? In the words of famous mathematician [Pierre Simon Laplace](https://en.wikipedia.org/wiki/Laplace%27s_demon),
> We may regard the present state of the universe as the effect of its past and the cause of its future. An intellect which at a certain moment would know all forces that set nature in motion, and all positions of all items of which nature is composed, if this intellect were also vast enough to submit these data to analysis, it would embrace in a single formula the movements of the greatest bodies of the universe and those of the tiniest atom; for such an intellect nothing would be uncertain and the future just like the past would be present before its eyes.

Namely, this simulation demonstrates a principle fundamental to our universe: deterministic chaos. This universal law of gravitation applies on scales as small as individual atoms, to our solar system, galaxy, and galaxy superclusters. Given an input as shown below, it would be nearly impossible to predict the future state of the system after any amount of time that isn't in the immediate-future! Even then, certain applications (like quantum states) demonstrate an impossibility to attain certainty!

Laplace believed that the only way to know, to 100% precision, a future state was to have complete knowledge of the system at hand. Of course, in our universe, this is impossible. The act of measuring any parameter of any energy-matter in our universe changes it, as dictated by the quantum [uncertainty principle](https://en.wikipedia.org/wiki/Uncertainty_principle) and the [observer effect](https://en.wikipedia.org/wiki/Observer_effect_%28physics%29).

## Outputs
The following are video outputs from the program, showing several different initial states and their vastly different outputs.

**Pretty particle simulation videos**
| ![video0](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-animation-0.webp =400x) | ![video1](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-animation-1.webp =400x)|
|-------------------------|-------------------------|
| ![video2](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-animation-2.webp =400x)| ![video3](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-animation-3.webp =400x)|

**Demonstration of slight variation causing chaos**
 | Before | After |
|----- |--------|
| ![0b](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-0-time-0.png =400x)| ![0a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-0-time-2500.png =400x) |
| ![1b](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-1-time-0.png =400x)| ![1a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-1-time-2500.png =400x)|
| ![1a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-2-time-0.png =400x) | ![1a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-2-time-2500.png =400x) |
| ![1a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-3-time-0.png =400x) | ![1a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-3-time-2500.png =400x) |
| ![1a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-4-time-0.png =400x) | ![1a](https://raw.githubusercontent.com/51037/chaotic-n-body/main/plots/plot-4-time-2500.png =400x) |

# Conclusions
As intellectuals seeking to further our understanding of the universe and all of its mysteries, we often try to reduce the "unpredictability" of nature. We predict the weather (though only within a couple of days accuracy, if that), but we can never know whether it will be raining in Colorado Springs on July 25th, 2050 at 2:00 pm until that time is very near in the future.

Such the contrast between such ignorance and the absolute certainty that we have evaluated universal constants down to, or the insane precision we have access to (technologies like photo-lithography for creating microprocessors on scales of single digit nanometers) is astounding. But, thus is the nature of our universe. We live with the seemingly massive contradiction every day.

# Try it yourself
To run this program, clone this repo or download the source (if downloaded as zip, extract).
In the main directory, run the command `pip install -r requirements.txt` (Requires python, you can just type python in command prompt on windows if you don't have it).
Then run `python nbody.py` and a window will appear with the simulation in action!
