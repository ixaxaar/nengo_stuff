#!/usr/bin/env python

import nengo
from nengo.neurons import LIF

import matplotlib.pyplot as plt

model = nengo.Network(label="Scalar Representation")

with model:
  s = nengo.Ensemble(100, dimensions=1, radius=1, neuron_type=LIF())

  i = nengo.Node(output=0.6)

  nengo.Connection(i, s)

  i_probe = nengo.Probe(s, synapse=0.01)
  s_probe = nengo.Probe(i, synapse=0.01)

sim = nengo.Simulator(model)
sim.run(10)

t = sim.trange()
plt.plot(sim.trange(), sim.data[i_probe], label="Scalar Input")
plt.plot(sim.trange(), sim.data[s_probe], label="Decoded output")
plt.legend()
plt.ylim(0,3)
plt.show()

