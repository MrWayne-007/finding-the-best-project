import numpy as np
import matplotlib.pyplot as plt # type: ignore
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv(r'XXXXX(your file location)')

# Assuming your CSV has columns 'Project', 'Cost', and 'Impact'
projects = data['Projects']
cost = data['Cost']
impact = data['Impact']

data['Score'] = impact / cost

# Sort the data by Score in descending order and select the top 3 projects
best_projects = data.sort_values(by='Score', ascending=False).head(3)

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(cost, impact, color='blue', label='Other Projects')

# Highlight the top 3 projects
plt.scatter(best_projects['Cost'], best_projects['Impact'], color='red', s=100, label='Top 3 Projects')

# Annotate each point with the project number
for i in range(len(projects)):
    plt.text(cost[i], impact[i], str(projects[i]), fontsize=9, ha='right')

# Highlight the top 3 projects with bigger and red points, and annotate them
for i in range(len(best_projects)):
    plt.text(best_projects['Cost'].iloc[i], best_projects['Impact'].iloc[i], 
             str(best_projects['Projects'].iloc[i]), fontsize=10, fontweight='bold', ha='right')

# Label the axes
plt.xlabel('Cost')
plt.ylabel('Impact')

# Title of the plot
plt.title('Project Selection: Cost vs Impact (Highlighting Top 3 Projects)')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
plt.show()