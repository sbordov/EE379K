import sys

first_arg = sys.argv[1]

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~Loss plotting code~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def plot_loss(category=first_arg):
    if category != "":
        category = "_" + category
    path_header = "/Users/Stefan/Documents/Fall_2017/EE379K/FinalProject/loss_plots/"
    path = path_header + 'loss_values' + category + ".txt"

    loss_values = open(path, "r")
    
    steps = []
    loss = []
    for line in loss_values:
        steps.append(int(line.split()[1]))
        loss.append(float(line.split()[3]))

    loss_values.close()

    #print(steps)

    if category == "_piano":
        title_category = ": Jazz Piano"
    elif category == "_bossa":
        title_category = ": Bossa Nova"
    else:
        title_category = ""
    plt.plot(steps, loss)
    plt.xlabel('Step No.')
    plt.ylabel('Loss')
    plt.title('WaveNet Loss Value Convergence' + title_category)
    plt.savefig('loss_plot' + category + '.png', bbox_inches="tight")
    print('Plot saved to ' + 'loss_plot' + category + '.png')

if __name__ == '__main__':
    plot_loss()
