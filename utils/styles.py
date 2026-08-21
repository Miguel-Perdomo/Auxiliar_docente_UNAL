"""
styles.py

Common plotting styles used throughout the courses.
"""

import matplotlib.pyplot as plt

def paper_style():
    """
    Apply the default plotting style.
    
    The style is designed for scientific figures intended for
    publications, reports and characterization studies.
    """
    plt.style.use("default")

    # Font (Computer Modern, identical to LaTeX)
    plt.rcParams["text.usetex"] = True
    plt.rcParams["font.family"] = "serif"

    # Default font sizes
    plt.rcParams["font.size"] = 18
    plt.rcParams["axes.labelsize"] = 18
    plt.rcParams["axes.titlesize"] = 18
    plt.rcParams["xtick.labelsize"] = 18
    plt.rcParams["ytick.labelsize"] = 18
    plt.rcParams["legend.fontsize"] = 18
    plt.rcParams["legend.title_fontsize"] = 18

    # White background
    plt.rcParams["figure.facecolor"] = "white"
    plt.rcParams["axes.facecolor"] = "white"
    plt.rcParams["savefig.facecolor"] = "white"

    # Black text
    plt.rcParams["text.color"] = "black"
    plt.rcParams["axes.labelcolor"] = "black"
    plt.rcParams["axes.edgecolor"] = "black"

    # Black ticks
    plt.rcParams["xtick.color"] = "black"
    plt.rcParams["ytick.color"] = "black"
