# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.19.9",
# ]
# ///
import marimo

__generated_with = "0.19.9"
app = marimo.App()


@app.cell
def _():
    import marimo as moc

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Exploratory Spatial Data Analysis for Hilden city
    """)
    return


@app.cell
def _():
    import geopandas as gpd
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings("ignore")
    return plt, sns


@app.cell
def _():
    import geopandas as gpd

    # Base URL
    url = "https://raw.githubusercontent.com/ssujit/public_transit_germany/main/data/"

    # File names
    wkam = "wkamo_hdn.gpkg"   # weekdays morning peak (06:00–08:59)
    wkpm = "wkpmo_hdn.gpkg"   # weekdays afternoon peak (14:00–16:59)
    satam = "satamo_hdn.gpkg" # Saturday morning peak (06:00–08:59)
    satpm = "satpmo_hdn.gpkg" # Saturday afternoon peak (14:00–16:59)
    sunam = "sunamo_hdn.gpkg" # Sunday morning peak (06:00–08:59)
    sunpm = "sanpmo_hdn.gpkg" # Sunday afternoon peak (14:00–16:59) — corrected

    # Read files
    wk_am  = gpd.read_file(f"{url}{wkam}")
    wk_pm  = gpd.read_file(f"{url}{wkpm}")
    sat_am = gpd.read_file(f"{url}{satam}")
    sat_pm = gpd.read_file(f"{url}{satpm}")
    sun_am = gpd.read_file(f"{url}{sunam}")
    sun_pm = gpd.read_file(f"{url}{sunpm}")
    return sat_am, sat_pm, sun_am, sun_pm, wk_am, wk_pm


@app.cell
def _(wk_am):
    wk_am.head()
    return


@app.cell
def _(wk_am):
    wk_am.shape
    return


@app.cell
def _(wk_am):
    wk_am.explore()
    return


@app.cell
def _(wk_am):
    wk_am.plot("pti", cmap="RdYlGn_r", legend=True)
    return


@app.cell
def _(plt, sat_am, sat_pm, sun_am, sun_pm, wk_am, wk_pm):
    # Set up subplots
    _fig, _axes = plt.subplots(3, 2, figsize=(12, 18))
    wk_am.plot('pti', cmap='Blues', legend=True, ax=_axes[0, 0])
    _axes[0, 0].set_title('Weekday AM')
    wk_pm.plot('pti', cmap='Reds', legend=True, ax=_axes[0, 1])
    _axes[0, 1].set_title('Weekday PM')
    sat_am.plot('pti', cmap='Greens', legend=True, ax=_axes[1, 0])
    _axes[1, 0].set_title('Saturday AM')
    sat_pm.plot('pti', cmap='Purples', legend=True, ax=_axes[1, 1])
    _axes[1, 1].set_title('Saturday PM')
    sun_am.plot('pti', cmap='Oranges', legend=True, ax=_axes[2, 0])
    _axes[2, 0].set_title('Sunday AM')
    sun_pm.plot('pti', cmap='RdYlGn_r', legend=True, ax=_axes[2, 1])
    _axes[2, 1].set_title('Sunday PM')
    plt.tight_layout()
    # Adjust layout
    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, sat_am, sat_pm, sun_am, sun_pm, wk_am, wk_pm):
    # Set up subplots
    _fig, _axes = plt.subplots(3, 2, figsize=(12, 18), subplot_kw=dict(aspect='equal'))
    wk_am.plot('pti', cmap='Blues', scheme='Quantiles', k=4, edgecolor='k', legend=True, ax=_axes[0, 0])
    _axes[0, 0].set_title('Weekday AM')
    wk_pm.plot('pti', cmap='Reds', scheme='Quantiles', k=4, edgecolor='k', legend=True, ax=_axes[0, 1])
    _axes[0, 1].set_title('Weekday PM')
    sat_am.plot('pti', cmap='Greens', scheme='Quantiles', k=4, edgecolor='k', legend=True, ax=_axes[1, 0])
    _axes[1, 0].set_title('Saturday AM')
    sat_pm.plot('pti', cmap='Purples', scheme='Quantiles', k=4, edgecolor='k', legend=True, ax=_axes[1, 1])
    _axes[1, 1].set_title('Saturday PM')
    sun_am.plot('pti', cmap='Oranges', scheme='Quantiles', k=4, edgecolor='k', legend=True, ax=_axes[2, 0])
    _axes[2, 0].set_title('Sunday AM')
    sun_pm.plot('pti', cmap='RdYlGn_r', scheme='Quantiles', k=4, edgecolor='k', legend=True, ax=_axes[2, 1])
    _axes[2, 1].set_title('Sunday PM')
    plt.tight_layout()
    # Adjust layout
    # Show the plot
    plt.show()
    return


@app.cell
def _(wk_pm):
    wk_pm.hist("pti", color = 'blue', edgecolor = 'None', density = True, legend=True)
    return


@app.cell
def _(plt, sat_am, sat_pm, sun_am, sun_pm, wk_am, wk_pm):
    # Set up histogram subplots
    _fig, _axes = plt.subplots(3, 2, figsize=(12, 18))
    wk_am.hist('pti', color='#1f78b4', ax=_axes[0, 0])
    _axes[0, 0].set_title('Weekday AM')
    _axes[0, 0].set_xlabel('PTI')
    _axes[0, 0].set_ylabel('Frequency')
    wk_pm.hist('pti', color='#e41a1c', ax=_axes[0, 1])
    _axes[0, 1].set_title('Weekday PM')
    _axes[0, 1].set_xlabel('PTI')
    _axes[0, 1].set_ylabel('Frequency')
    sat_am.hist('pti', color='#4daf4a', ax=_axes[1, 0])
    _axes[1, 0].set_title('Saturday AM')
    _axes[1, 0].set_xlabel('PTI')
    _axes[1, 0].set_ylabel('Frequency')
    sat_pm.hist('pti', color='#984ea3', ax=_axes[1, 1])
    _axes[1, 1].set_title('Saturday PM')
    _axes[1, 1].set_xlabel('PTI')
    _axes[1, 1].set_ylabel('Frequency')
    sun_am.hist('pti', color='#ff7f00', ax=_axes[2, 0])
    _axes[2, 0].set_title('Sunday AM')
    _axes[2, 0].set_xlabel('PTI')
    _axes[2, 0].set_ylabel('Frequency')
    sun_pm.hist('pti', color='#a65628', ax=_axes[2, 1])
    _axes[2, 1].set_title('Sunday PM')
    _axes[2, 1].set_xlabel('PTI')
    _axes[2, 1].set_ylabel('Frequency')
    plt.tight_layout()
    # Adjust layout
    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, wk_am):
    plt.boxplot(wk_am['pti'].dropna(), vert =False)
    # Add labels and title
    plt.xlabel('values')
    plt.ylabel('pti')
    plt.title('Boxplot for wk_am')

    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, sat_am, sat_pm, sun_am, sun_pm, wk_am, wk_pm):
    _pti_values = [df['pti'].dropna() for df in [wk_am, wk_pm, sat_am, sat_pm, sun_am, sun_pm]]
    plt.boxplot(_pti_values, labels=['wk_am', 'wk_pm', 'sat_am', 'sat_pm', 'sun_am', 'sun_pm'], vert=False)
    plt.xlabel('pti Values')
    # Add labels and title
    plt.ylabel('time')
    plt.title('Boxplot for all')
    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, wk_am, wk_pm):
    _pti_values = [df['pti'].dropna() for df in [wk_am, wk_pm]]
    plt.boxplot(_pti_values, labels=['wk_am', 'wk_pm'], vert=False)
    plt.xlabel('pti Values')
    # Add labels and title
    plt.ylabel('time')
    plt.title('Boxplot for weekdays')
    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, sat_am, sat_pm, sun_am, sun_pm):
    _pti_values = [df['pti'].dropna() for df in [sat_am, sat_pm, sun_am, sun_pm]]
    plt.boxplot(_pti_values, labels=['sat_am', 'sat_pm', 'sun_am', 'sun_pm'], vert=False)
    # Create a boxplot for all 'pti' values
    plt.xlabel('pti Values')
    plt.ylabel('time')
    # Add labels and title
    plt.title('Boxplot for weekend')
    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, sat_am, sat_pm):
    _pti_values = [df['pti'].dropna() for df in [sat_am, sat_pm]]
    plt.boxplot(_pti_values, labels=['sat_am', 'sat_pm'], vert=False)
    # Create a boxplot for all 'pti' values
    plt.xlabel('pti Values')
    plt.ylabel('time')
    # Add labels and title
    plt.title('Boxplot for Saturday')
    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, sun_am, sun_pm):
    _pti_values = [df['pti'].dropna() for df in [sun_am, sun_pm]]
    plt.boxplot(_pti_values, labels=['sun_am', 'sun_pm'], vert=False)
    # Create a boxplot for all 'pti' values
    plt.xlabel('pti Values')
    plt.ylabel('time')
    # Add labels and title
    plt.title('Boxplot for Sunday')
    # Show the plot
    plt.show()
    return


@app.cell
def _(sns, wk_am):
    sns.kdeplot(wk_am["pti"], color="blue")
    return


@app.cell
def _(plt, sat_am, sat_pm, sns, sun_am, sun_pm, wk_am, wk_pm):
    # Set up density plot subplots
    _fig, _axes = plt.subplots(3, 2, figsize=(10, 8))
    sns.kdeplot(wk_am['pti'], color='blue', ax=_axes[0, 0])
    # Weekday AM
    _axes[0, 0].set_title('Weekday AM')
    _axes[0, 0].set_xlabel('PTI')
    _axes[0, 0].set_ylabel('Density')
    sns.kdeplot(wk_pm['pti'], color='red', ax=_axes[0, 1])
    _axes[0, 1].set_title('Weekday PM')
    # Weekday PM
    _axes[0, 1].set_xlabel('PTI')
    _axes[0, 1].set_ylabel('Density')
    sns.kdeplot(sat_am['pti'], color='green', ax=_axes[1, 0])
    _axes[1, 0].set_title('Saturday AM')
    _axes[1, 0].set_xlabel('PTI')
    # Saturday AM
    _axes[1, 0].set_ylabel('Density')
    sns.kdeplot(sat_pm['pti'], color='purple', ax=_axes[1, 1])
    _axes[1, 1].set_title('Saturday PM')
    _axes[1, 1].set_xlabel('PTI')
    _axes[1, 1].set_ylabel('Density')
    # Saturday PM
    sns.kdeplot(sun_am['pti'], color='orange', ax=_axes[2, 0])
    _axes[2, 0].set_title('Sunday AM')
    _axes[2, 0].set_xlabel('PTI')
    _axes[2, 0].set_ylabel('Density')
    sns.kdeplot(sun_pm['pti'], color='brown', ax=_axes[2, 1])
    # Sunday AM
    _axes[2, 1].set_title('Sunday PM')
    _axes[2, 1].set_xlabel('PTI')
    _axes[2, 1].set_ylabel('Density')
    plt.tight_layout()
    # Sunday PM
    # Adjust layout
    # Show the plot
    plt.show()
    return


@app.cell
def _(plt, sns, wk_am, wk_pm):
    # Set up density plot subplots
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.kdeplot(wk_am['pti'], color='blue', ax=_axes[0])
    # Weekday AM
    _axes[0].set_title('Weekday AM')
    _axes[0].set_xlabel('PTI')
    _axes[0].set_ylabel('Density')
    sns.kdeplot(wk_pm['pti'], color='red', ax=_axes[1])
    _axes[1].set_title('Weekday PM')
    # Weekday PM
    _axes[1].set_xlabel('PTI')
    _axes[1].set_ylabel('Density')
    return


@app.cell
def _(plt, sat_am, sat_pm, sns):
    # Set up density plot subplots
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.kdeplot(sat_am['pti'], color='blue', ax=_axes[0])
    # Saturday AM
    _axes[0].set_title('Saturday AM')
    _axes[0].set_xlabel('PTI')
    _axes[0].set_ylabel('Density')
    sns.kdeplot(sat_pm['pti'], color='red', ax=_axes[1])
    _axes[1].set_title('Saturday PM')
    # Saturday PM
    _axes[1].set_xlabel('PTI')
    _axes[1].set_ylabel('Density')
    return


@app.cell
def _(plt, sns, sun_am, sun_pm):
    # Set up density plot subplots
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.kdeplot(sun_am['pti'], color='blue', ax=_axes[0])
    # Sunday AM
    _axes[0].set_title('Sunday AM')
    _axes[0].set_xlabel('PTI')
    _axes[0].set_ylabel('Density')
    sns.kdeplot(sun_pm['pti'], color='red', ax=_axes[1])
    _axes[1].set_title('Sunday PM')
    # Sunday PM
    _axes[1].set_xlabel('PTI')
    _axes[1].set_ylabel('Density')
    return


if __name__ == "__main__":
    app.run()
