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

## Code Description:
This code uses the D-Wave quantum annealer to minimize traffic congestion by optimizing traffic light modes at intersections. The key considerations include:
1. **Number of Cars**: Intersections with more cars are prioritized for green signals.
2. **Conflict Avoidance**: Conflicting signals between connected intersections are penalized to avoid simultaneous green lights at conflicting directions.
3. **QUBO Model**: The traffic control problem is modeled as a Quadratic Unconstrained Binary Optimization (QUBO) problem, solved using the D-Wave quantum annealer.

The code uses a conflict matrix to define which modes cannot be active simultaneously between connected intersections.
