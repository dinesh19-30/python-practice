
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
import matplotlib

plt.figure(figsize=(10,5))
ax = plt.gca()
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

def box(x, y, w, h, text):
    rect = Rectangle((x,y), w, h, fill=False)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=10)

def arrow(x1, y1, x2, y2):
    arr = FancyArrowPatch((x1,y1), (x2,y2), arrowstyle='->', mutation_scale=15, linewidth=1)
    ax.add_patch(arr)

# Draw components
box(0.5, 3.0, 1.5, 0.8, "Browser\n(Client)")
box(2.5, 3.0, 1.5, 0.8, "CDN\n(Optional)")
box(4.5, 3.0, 1.5, 0.8, "Load\nBalancer")
box(6.8, 3.0, 1.0, 0.8, "App\nServer 1")
box(6.8, 1.9, 1.0, 0.8, "App\nServer 2")
box(6.8, 0.8, 1.0, 0.8, "App\nServer 3")
box(4.5, 0.8, 1.8, 0.8, "Database\n(Primary)")

# Arrows between components
arrow(2.0, 3.4, 2.5, 3.4)  # Browser -> CDN
arrow(4.0, 3.4, 4.5, 3.4)  # CDN -> LB
arrow(6.0, 3.4, 6.8, 3.6)  # LB -> App1
arrow(6.0, 3.4, 6.8, 2.3)  # LB -> App2
arrow(6.0, 3.4, 6.8, 1.2)  # LB -> App3
arrow(6.3, 1.8, 5.8, 1.2)  # App cluster -> DB

# Group label for app servers
ax.text(7.3, 3.9, "Application\nCluster", ha='left', va='center', fontsize=9)

plt.tight_layout()
output_path = "/mnt/data/tech_diagram.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight')
plt.show()

print(f"Saved diagram to: {output_path}")
