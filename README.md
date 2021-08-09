## Multi-Level-Cache-Simulator

In this project, built a two level Cache simulator that simulated the behaviour of two level (L2 - L3) set associative Cache and reported number of L2, L3 Cache misses by passing in L1 Cache miss traces for six SPEC CPU 2006 applications through the simulator.

Implemented LRU Cache replacement policy and different Cache inclusion-exclusion policies.

### Working:
* Simulator is present in **Simulator directory**
* L1 Cache miss traces are available in binary format, the trace files should be converted to text foramt using **read_traces.c**
* trace files in text format should be placed in **traces** directory for the simulator to read them.
* To run the simulator, execute script.sh file followed by name of the L1 Cache miss trace file (saved in traces directory) to generate number of L2, L3 Cache misses.
