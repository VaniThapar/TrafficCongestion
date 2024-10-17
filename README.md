# Traffic Signal Optimization Using Quantum Annealing

This project optimizes traffic signals at intersections using the D-Wave quantum annealer. The approach prioritizes clearing intersections with more cars while ensuring no conflicting signals are green at connected intersections.

## Steps to Set Up D-Wave Annealer:

### 1. Install Required Libraries:
First, ensure the required packages are installed:
```bash
pip install dwave-ocean-sdk 
```

### 2. Set Up API Token:
- Sign up at [D-Wave Leap](https://cloud.dwavesys.com/leap/) to get an API token.
- Set up the API token for your environment:
  ```bash
  dwave config create
  ```
  You'll be prompted to enter your **API token**, solver region, and other information.

Alternatively, you can create a `dwave_config` file:
- Create the file `.dwave_config` in your home directory:
  ```plaintext
  [defaults]
  endpoint = https://cloud.dwavesys.com/sapi
  token = YOUR_API_TOKEN_HERE
  solver = DW_2000Q_6
  ```

### 3. Running the Code:
Once the D-Wave environment is set up, run the provided Python script for traffic signal optimization


## Input/Output Format:

### Input:
1. **Directed Graph (Traffic Network)**: Represents intersections (nodes) and roads (edges). Each node is an intersection, and edges represent the roads between intersections.
2. **Cars Vector**: A dictionary with the number of cars at each intersection, e.g., `{0: 20, 1: 15, 2: 30, 3: 10}`.

### Output:
1. **Green Signals and Modes**: The output will provide which intersections have green signals and in what mode they are operating. For example:
   ```
   Intersection 0 is in mode 0 (green signal)
   Intersection 1 is in mode 3 (green signal)
   ```
2. **Energy**: The energy value represents the optimization score, where lower energy means better optimization and fewer conflicts.

## Code Description:
This code uses the D-Wave quantum annealer to minimize traffic congestion by optimizing traffic light modes at intersections. The key considerations include:
1. **Number of Cars**: Intersections with more cars are prioritized for green signals.
2. **Conflict Avoidance**: Conflicting signals between connected intersections are penalized to avoid simultaneous green lights at conflicting directions.
3. **QUBO Model**: The traffic control problem is modeled as a Quadratic Unconstrained Binary Optimization (QUBO) problem, solved using the D-Wave quantum annealer.

The code uses a conflict matrix to define which modes cannot be active simultaneously between connected intersections.

## Future Expansion:
This solution can be scaled to handle real-world traffic problems by:
1. **Real-life Traffic Networks**: Expanding the input to include actual traffic networks (graph representation) of cities.
2. **Real-time Traffic Updates**: Solving the problem at regular intervals (e.g., every few minutes) for real-time optimization based on traffic data (number of cars at intersections).
3. **Hybrid Approach**: Using a hybrid quantum-classical approach for cities with dense traffic networks to handle large datasets and improve traffic flow efficiency.


