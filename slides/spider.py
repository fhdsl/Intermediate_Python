import matplotlib.pyplot as plt
import numpy as np

def create_spider_plot(skill_values, title):
    """
    Create a spiderweb plot for 5 skill categories.
    
    Parameters:
    -----------
    skill_values : list
        List of 5 integers representing skill levels
    title : str
        Title for the plot
    """
    # Define categories
    categories = ['Machine Learning', 'Ethics/Bias', 'Prompting', 'Critical Thinking', 'Communication']
    
    # Number of variables
    num_vars = len(categories)
    
    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop by appending the first value to the end
    values = skill_values + skill_values[:1]
    angles += angles[:1]
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    ax.plot(angles, values, 'o-', linewidth=2, label='Profile')
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 5)
    ax.set_title(title, y=1.08)
    plt.show()


create_spider_plot([1, 4, 1, 3, 4], "Executives")

create_spider_plot([1,5,2,4,2], "Nurses")