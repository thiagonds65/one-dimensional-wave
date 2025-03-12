## One-dimensional wave simulation

This python code uses Finite Volume Method to obtain a simulation of a wave propagation. Plot in end of the program shows the motion of a wave in a string with fixed extremities

## finvol-trap-gif.py

This program can create a gif of the wave propagating in a string, as seen below:

![Alt Text](wave_propagation_1d.gif)

For this example, the following conditions are considered:

### Boundary Conditions
<p>
$$u(0,t) = 0$$
</p>
<p>
$$u(L,t) = 0$$
</p>

### Initial Conditions

<p>
$$u(x,0) = sin(x), 0\le x \le \pi$$
</p>
<p>
$$u(x,0) = 0, x > \pi$$
</p>
<p>
$$\left.\frac{\partial u}{\partial t}\right|_{t = 0} = 0$$
</p>

Changing boundary and initial conditions, allows to obtain waves with different shapes.
