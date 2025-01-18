# Analysis of DDoS Attack on Connected Autonomous Vehicular Network

## Overview
This project analysis a Distributed Denial of Service (DDoS) attack on Connected Autonomous Vehicles (CAVs) using the **SUMO (Simulation of Urban MObility)** simulator and Python's **TraCI** library. The primary objective is to analyze the impact of a DDoS attack on vehicular networks and visualize the results through graphs.

## Features
- Integration of Python with SUMO using TraCI.
- Analysis of a DDoS attack by sending malicious packets to vehicles.
- Logging of active vehicle count and packet load at each simulation step.
- Visualization of the simulation results using Matplotlib.

---

## Prerequisites
1. **SUMO Simulator**
   - Download and install from [SUMO Official Website](https://sumo.dlr.de/docs/Downloads.html).

2. **Python (3.6 or later)**
   - Install Python from [Python.org](https://www.python.org/).

3. **Required Python Libraries**
   ```bash
   pip install matplotlib sumolib traci
   ```

---

## File Structure
```
.
├── map.osm                # Downloaded OpenStreetMap file
├── map.net.xml            # SUMO network file
├── map.trips.xml          # Randomly generated trips file
├── map.rou.xml            # Vehicle routes file
├── map.sumocfg            # SUMO configuration file
├── ddos_simulation.py     # Python script for running the simulation
├── results/               # Directory to store logs and output
│   ├── ddos_log.txt       # Log file of simulation results
│   └── plot.png           # Graph of active vehicles vs simulation steps
```

---

## Getting Started

### 1. Generate SUMO Network Files
- Download a map area from [OpenStreetMap](https://www.openstreetmap.org/) and save it as `map.osm`.
- Convert the map to SUMO network format:
  ```bash
  netconvert --osm-files map.osm --output-file map.net.xml
  ```
- Generate random trips for vehicles:
  ```bash
  python randomTrips.py -n map.net.xml -e 1000 -o map.trips.xml
  ```
- Create vehicle routes:
  ```bash
  duarouter -n map.net.xml --route-files map.trips.xml -o map.rou.xml --ignore-errors
  ```

### 2. Configure SUMO Simulation
- Use the following structure for `map.sumocfg`:
  ```xml
  <configuration>
      <input>
          <net-file value="map.net.xml"/>
          <route-files value="map.rou.xml"/>
      </input>
  </configuration>
  ```

### 3. Run the Python Script
- Execute the Python script:
  ```bash
  python ddos_simulation.py
  ```
- The simulation will:
  - Start the SUMO GUI.
  - Log the active vehicles and packet load to `results/ddos_log.txt`.
  - Save a graph of active vehicles vs simulation steps to `results/plot.png`.

---

## Output
1. **Log File**: Details of active vehicles and packets sent at each simulation step.
2. **Graph**: Visualization of active vehicles over time under the impact of a DDoS attack.

---

## Results
The simulation demonstrates:
- A decrease in the number of active vehicles as the packet load increases.
- The vulnerability of connected autonomous vehicular networks to cyber-attacks like DDoS.

---

## References
1. [SUMO Official Documentation](https://sumo.dlr.de/docs/)
2. [TraCI Python API](https://sumo.dlr.de/docs/TraCI.html)
3. [OpenStreetMap](https://www.openstreetmap.org/)

---
