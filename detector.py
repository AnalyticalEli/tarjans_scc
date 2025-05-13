import networkx as nx
import matplotlib.pyplot as plt

class ThreatDetector:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.threat_keywords = ["brainrot", "evil", "hacker", "brandon"]  # Custom threats
    
    def add_device(self, src, dst):
        """Auto-convert to lowercase for case-insensitive checks"""
        self.graph.add_edge(str(src).lower(), str(dst).lower())
    
    def find_threats(self):
        """Check for custom keywords in device names"""
        threats = []
        for node in self.graph.nodes:
            for keyword in self.threat_keywords:
                if keyword in node:
                    threats.append(f"🚨 THREAT: {node} (contains '{keyword}')")
                    break
        return threats if threats else ["✅ No threats detected"]
    
    def visualize(self):
        """Hybrid visualization (popup or saved image)"""
        try:
            plt.switch_backend('TkAgg')  # Try interactive
            self._draw_graph()
            plt.show(block=True)
        except:
            self._draw_graph()
            plt.savefig('threat_map.png')
            print("Saved visualization to threat_map.png")
    
    def _draw_graph(self):
        """Shared drawing logic"""
        node_colors = [
            "red" if any(kw in node for kw in self.threat_keywords)
            else "blue" 
            for node in self.graph.nodes
        ]
        
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(
            self.graph, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=2000,
            font_size=10,
            arrows=True
        )
        plt.title("Network Threat Map (Red = Keyword Detected)")
