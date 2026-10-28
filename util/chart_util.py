# Módulo chart_util.py

"""

Funciones recurrentes para crear gráficos.

"""

import matplotlib.pyplot as plt
import pandas as pd

def show_simple(dataset, x, y, y_lines=None, title=None, x_label=None, y_label=None):
    df = pd.DataFrame(dataset)

    # Crea el gráfico.
    ax = df.plot.bar(x=x, y=y, title=title)
    add_info(ax, y_lines, x_label, y_label)
    plt.tight_layout()
    plt.show()

def show_multiple(datasets, x, y, y_lines=None, main_title=None, titles=None, x_label=None, y_label=None):
    dfs = [pd.DataFrame(dataset) for dataset in datasets]
    n_cols = len(dfs)

    if n_cols < 2:
        raise ValueError('There must be data for at least two charts.')

    # Crea marco para los gráficos.
    fig, axes = plt.subplots(1, n_cols, figsize=(6*n_cols, 5))

    # Añade los gráficos por orden.
    for i, df in enumerate(dfs):
        ax = axes[i]
        # Crea el gráfico.
        df.plot.bar(x=x, y=y, ax=ax, title=(titles[i] if titles and i < len(titles) else None))
        add_info(ax, y_lines, x_label, y_label)

    # Añade título al marco.
    if main_title is not None:
        fig.suptitle(main_title, fontweight='bold')

    plt.tight_layout()
    plt.show()

def add_info(ax, y_lines=None, x_label=None, y_label=None):
    colors = ['green', 'red']

    if y_lines is not None:
        # Añade líneas horizontales.
        for i, y_line in enumerate(y_lines):
            ax.axhline(y=y_line, color=colors[i%2], linestyle='--', linewidth=1.5)
        ax.legend()

    # Añade etiquetas horizontales y verticales.
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.margins(y=0.15)
    ax.tick_params(axis='x', rotation=0)