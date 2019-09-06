from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from matminer.featurizers.composition import ElementFraction
from pymatgen import Composition
import numpy as np
import ternary
from ternary.heatmapping import heatmap

def ternary_from_data(data, elems=["Left", "Center", "Right"], scale=32):
    _, ax = plt.subplots()
    
    # Make the plot 
    fig, tax = ternary.figure(scale=scale, ax=ax)
    tax.gridlines(color="black", multiple=10)
    tax.boundary(linewidth=1)

    # Generate the heatmap
    sc = heatmap(data, scale, cmap=make_cmap(), ax=ax, vmin=0.5, vmax=1, colorbar=True)
    
    # Make it prettier
    plt.axis('off')
    ax.text(1.05 * scale, -0.05 * scale, elems[0], ha='right', fontsize=12) # 1st elem
    ax.text(.50 * scale, .90 * scale, elems[1], ha='center', fontsize=12) # 2nd elem
    ax.text(-.05 * scale, -.05 * scale, elems[2], ha='left', fontsize=12) # 3rd elem
    
def make_cmap(base='viridis_r', scale_factor=1.5, cutoff=0.9, adjust_factor=0.1):
    """Make a colormap that this scaled to emphasize the top of the range.
    
    Two kinds of emphasis:
        1) Scaling the colormap to have a stronger gradient at the top
        2) Making the colors below a treshold lighter
        
    Inputs:
        base - str, base color map name
        scale_factor - float, how much to exaggerate the range at the top (larger value -> larger scaling)
        cutoff - float, treshold below which to lighten colors (0-1)
        adjust_factor - float, how much to dampen colors (0-1)
    Returns:
        Colormap
    """
    
    # Get the base colormap
    v = cm.get_cmap('viridis_r')
    
    # Scale it
    new_list = v(np.linspace(0,1,300) ** scale_factor)

    # Apply cutoff
    new_list[:int(len(new_list)*cutoff),:3] += (1 - new_list[:int(len(new_list)*cutoff),:3]) * adjust_factor
    return ListedColormap(new_list, name='%s_scaled'%base)

