import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
# Set the file path to save the chart
chart_filepath = "pie_chart.png"

# Save the chart as an image
plt.savefig(chart_filepath)
plt.show()
