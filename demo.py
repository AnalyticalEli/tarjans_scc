#Demo script for the Threat Detector (FNL) 
from detector import ThreatDetector

def main():
    print("=== CUSTOM THREAT DETECTOR ===")
    net = ThreatDetector()
    
    # Build network (using your keywords)
    net.add_device("Router", "SmartTV")
    net.add_device("evil_laptop", "Router")  # 🚨
    net.add_device("hacker_pc", "Webcam")  # 🚨
    net.add_device("BrainRot_Stories", "SmartTV")  # 🚨 (case-insensitive)
    net.add_device("brandon_Rant", "Dillion_Sanity")  # 🚨 (case-insensitive) //Remove
    
    # Show results
    print("\n=== THREAT SCAN ===")
    print('\n'.join(net.find_threats()))
    
    print("\n=== NETWORK SUMMARY ===")
    print(f"Devices: {list(net.graph.nodes)}")
    print(f"Connections: {list(net.graph.edges)}")
    
    # Visualize
    print("\nLaunching threat map...")
    net.visualize()

if __name__ == "__main__":
    main()

