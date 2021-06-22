.. _features:

.. include:: ../_shared/previews.rst

Features
########


Interactive Maps
----------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |titanic-kaggle|

    ---
    |airport-kaggle|

    ---
    |basemaps-kaggle|

    ---
    |mapping_US_household-kaggle|

    ---
    |airbnb_boston-datalore|

    ---
    |beijing-kaggle|

    ---
    |california_housing-nbviewer|

**Lets-Plot** supports interactive maps via the ``geom_livemap()`` geom layer which enables a researcher to visualize geospatial information on a zoomable and paneble map.

When building interactive geospatial visualizations with **Lets-Plot** the visualisation workflow remains the same as when building a regular ggplot2 plot.


Geocoding
---------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geocoding_examples-nbviewer|

    ---
    |mapping_US_household-kaggle|

    ---
    |map_US_household-nbviewer|

    ---
    |titanic-kaggle|

Geocoding is the process of converting names of places into geographic coordinates.

The **Lets-Plot** has built-in geocoding capabilities covering the folloing administrative levels: *countries*, *states* (US and non-US equivalents), *counties* (and equivalents), *cities* (and towns).

Learn more: :ref:`Geocoding <geocoding>`.


GeoPandas Support
-----------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |geopandas_naturalearth-nbviewer|

    ---
    |airbnb_boston-datalore|

    ---
    |kotlin_isl-nbviewer|

GeoPandas GeoDataFrame is a tabular data structure that contains a set of shapes (geometry) per each observation.

GeoDataFrame extends pandas DataFrame and as such, aside from the geometry, can contain other data.

GeoPandas supports the following three basic classes of geometric objects (shapes):

- Points / Multi-Points
- Lines / Multi-Lines
- Polygons / Multi-Polygons

All GeoPandas shapes are "undersood" by **Lets-Plot** and can be plotted using various geometry layers, depending on the type of the shape.


GGBunch
-------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |ggbunch-nbviewer|

    ---
    |geom_smooth-nbviewer|

    ---
    |scatter_matrix-nbviewer|

GGBunch allows to show a collection of plots on one figure. Each plot in the collection can have arbitrary location and size. There is no automatic layout inside the bunch.


Correlation Plot
----------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |correlation_plot-nbviewer|

The ``corr_plot()`` function creates a fluent builder object offering a set of methods for configuring of beautiful correlation plots. A call to the terminal ``build()`` method in the end will create a resulting plot object.


Image Matrix
------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |image_matrix-nbviewer|

The ``image_matrix()`` function arranges a set of images in a grid.

The ``image_matrix()`` function uses geom_image under the hood, so you might want to check out these demos as well:

- `image_101.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_101.ipynb>`__
- `image_fisher_boat.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_fisher_boat.ipynb>`__


Formatting
----------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |formatting_axes-nbviewer|

    ---
    |label_format-nbviewer|

    ---
    |facets-nbviewer|

    ---
    |airport-kaggle|

**Lets-Plot** supports formatting of values of numeric and date-time types.

Complementary to the value formatting, a *string template* is also supported.

Learn more: :ref:`Formatting <formats>`.


Tooltip Customization
---------------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |tooltip-nbviewer|

    ---
    |airport-kaggle|

You can customize the content of tooltips for the layer by using the parameter ``tooltips`` of ``geom`` functions.

Learn more: :ref:`Tooltip Customization <tooltips>`.


Data Sampling
-------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |sampling_random-nbviewer|

    ---
    |sampling_pick-nbviewer|

    ---
    |sampling_systematic-nbviewer|

    ---
    |sampling_stratified-nbviewer|

    ---
    |sampling_groups-nbviewer|

    ---
    |sampling_vertex-nbviewer|

Sampling is a special technique of data transformation, which is built into **Lets-Plot** and is applied after ``stat`` transformation.

Sampling helps dealing with large datasets when unintentional attempt to plot an excessively large number of geometries can lead to UI freezes and even to out-of-memory crashes.

Sampling is also one of the ways of handling over-plotting.

Learn more: :ref:`Sampling in Lets-Plot <sampling>`.


'No Javascript' Mode
--------------------

In the 'no javascript' mode **Lets-Plot** genetares plots as bare-bones SVG images.

This mode is helpful when there is a requirement to render notebooks in an 'ipnb' renderer which does not suppopt javascript (like GitHub's built-in renderer).

Activate 'no javascript' mode using the ``LetsPlot.setup_html()`` method call:

.. code:: python

    from lets_plot import *
    LetsPlot.setup_html(no_js=True)

Alternativaly, you can set up the environment variable:

.. code:: bash

    LETS_PLOT_NO_JS = true   (other accepted values are: 1, t, y, yes)

.. note::

    Interactive maps do not support the 'no javascript' mode.


Offline Mode
------------

In classic Jupyter notebook the ``LetsPlot.setup_html()`` statement by default pre-loads **Lets-Plot** JS library from CDN. Alternatively, option ``offline=True`` will force **Lets-Plot** adding the full JS bundle to the notebook. In this case, plots in the notebook will be working without an Internet connection.

.. code:: python

   from lets_plot import *
   LetsPlot.setup_html(offline=True)

.. note::

    Internet connection is still required for interactive maps and geocoding API.