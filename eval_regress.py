import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
np.set_printoptions(suppress=True, precision=3)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

def residual_plot(measured,
                  predicted,
                  width=5,
                  height=5,
                  line_color='k',
                  scatter_color='r'):
    '''
    measured : target continuous variable from test/validation data (1D array)
    predicted: model predictions based    on   test/validation data (1D array)
    returns: 2d plot of measured vs predicted vales of size width, height
    '''
    fig, ax = plt.subplots(figsize=(width, height))
    ax.scatter(measured, predicted, edgecolors=(0, 0, 0), color='r')
    ax.plot([measured.min(), measured.max()],
            [measured.min(), measured.max()],
            'k',
            lw=4
            )
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()
