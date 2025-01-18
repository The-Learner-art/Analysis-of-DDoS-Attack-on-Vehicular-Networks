import os
import traci  # SUMO Python library
import matplotlib.pyplot as plt

# Path to SUMO binaries
SUMO_BINARY = "sumo-gui"  # Use "sumo" for command-line interface

# Configuration file for SUMO simulation
SUMO_CONFIG = "map.sumocfg"

# Log file for results
LOG_FILE = "results/ddos_log.txt"


def ddos_simulation():
    step = 0
    active_vehicles = []
    total_packets = 0

    # Log file for saving simulations results
    with open(LOG_FILE, "w") as log_file:
        # Start SUMO simulation
        traci.start([SUMO_BINARY, "-c", SUMO_CONFIG])
        print("Simulation started...")

        try:
            while traci.simulation.getMinExpectedNumber() > 0:
                traci.simulationStep()

                # Active vehicles at each step
                vehicles = traci.vehicle.getIDList()
                active_vehicles.append(len(vehicles))

                # Simulate DDoS attack
                if step % 10 == 0:  # DDoS every 10 steps
                    for vehicle in vehicles:
                        # Sending dummy packets to each vehicle
                        packet_size = 1024
                        total_packets += packet_size

                # Simulation data written to log file
                log_file.write(f"Step {step}, Active Vehicles: {len(vehicles)}, Packets Sent: {total_packets}\n")
                step += 1

        finally:
            traci.close()

        print("Simulation completed.")
    
    return active_vehicles, total_packets


def plot_results(active_vehicles):
    plt.figure(figsize=(10, 6))
    plt.plot(active_vehicles, label="Active Vehicles", color="blue")
    plt.xlabel("Simulation Steps")
    plt.ylabel("Number of Active Vehicles")
    plt.title("DDoS Impact: Active Vehicles vs Time")
    plt.legend()
    plt.grid()
    plt.savefig("results/plot.png")
    plt.show()


if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)

    # Run simulation and log results
    active_vehicles, total_packets = ddos_simulation()

    # Generate and plotting log results
    plot_results(active_vehicles)

    print("Results logged and graph saved in the 'results' folder.")