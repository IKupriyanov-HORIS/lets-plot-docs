.. _index

.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Lets-Plot for Python |official JetBrains project|
=================================================

.. raw:: html

   <table class="table table-striped table-bordered">
       <tr>
           <td>Latest Release</td>
           <td>
               <a href="https://pypi.org/project/lets-plot/"/>
               <img src="https://badge.fury.io/py/lets-plot.svg"/>
           </td>
       </tr>
       <tr>
           <td>License</td>
           <td>
               <a href="https://opensource.org/licenses/MIT"/>
               <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>
           </td>
       </tr>
       <tr>
           <td>OS</td>
           <td>Linux, MacOS, Windows</td>
       </tr>
       <tr>
           <td>Python versions</td>
           <td>3.6, 3.7, 3.8, 3.9</td>
       </tr>
   </table>

.. panels::
    :container: previews-container
    :column:

    .. image:: _static/images/previews/visualization-of-the-titanic-s-voyage.png
        :target: https://www.kaggle.com/alshan/visualization-of-the-titanic-s-voyage
    ---
    .. image:: _static/images/previews/visualization-of-airport-data-on-map.png
        :target: https://www.kaggle.com/alshan/visualization-of-airport-data-on-map
    ---
    .. image:: _static/images/previews/the-gallery-of-basemaps.png
        :target: https://www.kaggle.com/alshan/the-gallery-of-basemaps
    ---
    .. image:: _static/images/previews/mapping-us-household-income.png
        :target: https://www.kaggle.com/alshan/mapping-us-household-income
    ---
    .. image:: _static/images/previews/plotting-airbnb-prices-boston.png
        :target: https://datalore.jetbrains.com/view/notebook/eifzdh96VYuNrcjuOpYPYr
    ---
    .. image:: _static/images/previews/beijing-housing-prices-on-a-map-with-spatial-join.png
        :target: https://www.kaggle.com/alshan/beijing-housing-prices-on-a-map-with-spatial-join
    ---
    .. image:: _static/images/previews/map_california_housing.png
        :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/map-california-housing/map_california_housing.ipynb
    ---
    .. image:: _static/images/previews/geocoding_examples.png
        :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geocoding_examples.ipynb
    ---
    .. image:: _static/images/previews/map_US_household_income.png
        :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/map_US_household_income.ipynb
    ---
    .. image:: _static/images/previews/geocoding_reference.png
        :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geocoding_reference.ipynb
    ---
    .. image:: _static/images/previews/geopandas_naturalearth.png
        :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_naturalearth.ipynb
    ---
    .. image:: _static/images/previews/geopandas_kotlin_isl.png
        :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geopandas_kotlin_isl.ipynb

Overview
~~~~~~~~

The ``Lets-Plot for Python`` library includes a native backend and a
Python API, which was mostly based on the
`ggplot2 <https://ggplot2.tidyverse.org>`__ package well-known to data
scientists who use R.

R ggplot2 has extensive documentation and a multitude of examples and
therefore is an excellent resource for those who want to learn the
grammar of graphics.

Note that the Python API being very similar yet is different in detail
from R. Although we have not implemented the entire ggplot2 API in our
Python package, we have added a few new features to our Python API.

You can try the Lets-Plot library in
`Datalore <https://datalore.jetbrains.com>`__. Lets-Plot is available in
Datalore out-of-the-box (i.e. you can ignore the
`Installation <#installation>`__ chapter below).

The advantage of `Datalore <https://datalore.jetbrains.com>`__ as a
learning tool in comparison to Jupyter is that it is equipped with very
friendly Python editor which comes with auto-completion, intentions, and
other useful coding assistance features.

Begin with the `quickstart in
Datalore <https://view.datalore.io/notebook/Zzg9EVS6i16ELQo3arzWsP>`__
notebook to learn more about Datalore notebooks.

Watch the `Datalore Getting Started
Tutorial <https://youtu.be/MjvFQxqNSe0>`__ video for a quick
introduction to Datalore.

Installation
~~~~~~~~~~~~

.. _1-for-linux-and-mac-users:

1. For Linux and Mac users:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the Lets-Plot library, run the following command:

.. code:: shell

   pip install lets-plot

.. _2-for-windows-users:

2. For Windows users:
^^^^^^^^^^^^^^^^^^^^^

Install Anaconda3 (or Miniconda3), then install MinGW toolchain to
Conda:

.. code:: shell

   conda install m2w64-toolchain

Install the Lets-Plot library:

.. code:: shell

   pip install lets-plot

.. |official JetBrains project| image:: http://jb.gg/badges/official-flat-square.svg
   :target: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub

Quick start with Jupyter
~~~~~~~~~~~~~~~~~~~~~~~~

You can use Lets-Plot in Jupyter notebook or other notebook of your choice, like Datalore, Kaggle or Colab.

To evaluate the plotting capabilities of Lets-Plot, add the following code to a Jupyter notebook:

.. jupyter-execute::
    :linenos:

    import numpy as np
    from lets_plot import *
    LetsPlot.setup_html()        

    np.random.seed(12)
    data = dict(
        cond=np.repeat(['A','B'], 200),
        rating=np.concatenate((np.random.normal(0, 1, 200), np.random.normal(1, 1.5, 200)))
    )

    ggplot(data, aes(x='rating', fill='cond')) + ggsize(500, 250) + \
        geom_density(color='dark_green', alpha=.7) + scale_fill_brewer(type='seq') + \
        theme(axis_line_y='blank')

.. raw:: html

   <br/>
   <a href="https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/quickstart.ipynb"> 
       <img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png" width="109" height="20" align="left">
   </a>
   <span>&nbsp;&nbsp;</span>
   <a href="https://view.datalore.io/notebook/Zzg9EVS6i16ELQo3arzWsP" title="View in Datalore"> 
       <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg" width="20" height="20">
   </a>
   <span>&nbsp;&nbsp;</span>
   <a href="https://www.kaggle.com/alshan/lets-plot-quickstart" title="View at Kaggle"> 
       <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg" width="20" height="20">
   </a>
   <span>&nbsp;&nbsp;</span>
   <a href="https://colab.research.google.com/drive/1uYYZcG0g0kP4lJdPkpWB8aBS96ioDii2?usp=sharing" title="View at Colab"> 
       <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_colab.svg" width="20" height="20">
   </a>
   <span>&nbsp;&nbsp;</span>
   <a href="https://deepnote.com/project/673ea421-638e-469d-8d04-5cc4c6e0258f#%2Fnotebook.ipynb" title="View at Deepnote"> 
       <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_deepnote.svg" width="20" height="20">
   </a>

Change Log
~~~~~~~~~~

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.