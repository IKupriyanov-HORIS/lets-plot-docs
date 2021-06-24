.. _index

.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: _shared/previews.rst


Lets-Plot: Declarative Data Visualization Library
=================================================

.. panels::
    :container: + preview-window
    :column: col-lg-12 p-2

    |airport-full-kaggle|

.. panels::
    :container: + previews preview-picker
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |airport-kaggle|

    ---
    |geom_smooth-nbviewer|

    ---
    |kotlin_isl-nbviewer|

    ---
    |formatting_axes-nbviewer|

About Lets-Plot |official JetBrains project|
--------------------------------------------

.. |official JetBrains project| image:: http://jb.gg/badges/official-flat-square.svg
    :target: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub

.. panels::
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    |info_table_html|

    ---
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2
    :body: text-justify

    **Lets-Plot** is an open-source plotting library for statistical data. It is implemented using the Kotlin programming language.

    **Lets-Plot** supports geospatial data and has some convenient :ref:`features <features>` to help you explore it.

    ---
    :column: col-lg-8 col-md-4 col-sm-6 col-xs-12 p-2

    The **Lets-Plot** for Python library includes a native backend and a :ref:`Python API <api>`, which was mostly based on the `ggplot2 <https://ggplot2.tidyverse.org>`__ package well-known to data scientists who use R.

    To learn more about the grammar of graphics, we recommend an excellent book called "ggplot2: Elegant Graphics for Data Analysis". It will be a good prerequisite for further exploration of the **Lets-Plot** library.

    ---
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
    .. image:: _static/images/ggplot2-elegant-graphics-for-data-analysis.jpg
        :target: https://ggplot2-book.org/index.html

.. |info_table_html| raw:: html

   <table class="table table-striped table-bordered">
       <tr>
           <td>Latest release</td>
           <td>
               <a href="https://pypi.org/project/lets-plot/" target="_blank" />
               <img src="https://badge.fury.io/py/lets-plot.svg" />
           </td>
       </tr>
       <tr>
           <td>License</td>
           <td>
               <a href="https://opensource.org/licenses/MIT" target="_blank" />
               <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
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

Try it now with Datalore
------------------------

You can try the **Lets-Plot** library in `Datalore <https://datalore.jetbrains.com>`__. **Lets-Plot** is available in Datalore out-of-the-box.

The advantage of `Datalore <https://datalore.jetbrains.com>`__ as a learning tool in comparison to Jupyter is that it is equipped with a very friendly Python editor which comes with auto-completion, intentions and other useful coding assistance features.

Begin with the `quickstart in Datalore <https://view.datalore.io/notebook/Zzg9EVS6i16ELQo3arzWsP>`__ notebook to learn more about Datalore notebooks.

.. raw:: html

    <div class="video-container">
      <iframe width="640" height="360" src="https://www.youtube.com/embed/MjvFQxqNSe0"></iframe>
    </div>

Quickstart
----------

You can use **Lets-Plot** in a Jupyter notebook or another notebook of your choice, like Datalore, Kaggle or Colab.

To evaluate the plotting capabilities of **Lets-Plot**, add the following code to a Jupyter notebook:

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

.. panels::
    :container: + platforms-for-lets-plot
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg
        :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/quickstart.ipynb

    ---
    .. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
        :target: https://view.datalore.io/notebook/Zzg9EVS6i16ELQo3arzWsP

    ---
    .. image:: _static/images/logo/icon-pycharm.svg

    ---
    .. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
        :target: https://www.kaggle.com/alshan/lets-plot-quickstart

    ---
    .. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_colab.svg
        :target: https://colab.research.google.com/drive/1uYYZcG0g0kP4lJdPkpWB8aBS96ioDii2?usp=sharing

    ---
    .. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_deepnote.svg
        :target: https://deepnote.com/project/673ea421-638e-469d-8d04-5cc4c6e0258f#%2Fnotebook.ipynb

More Examples
-------------

.. panels::
    :container: + previews preview-gallery
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |beijing-kaggle|

    ---
    |correlation_plot-nbviewer|

    ---
    |geocoding_examples-nbviewer|

    ---
    |ggbunch-nbviewer|

    ---
    |geopandas_naturalearth-nbviewer|

    ---
    |image_matrix-nbviewer|

    ---
    |airbnb_boston-datalore|

    ---
    |tooltip-nbviewer|

    ---
    |sampling_groups-nbviewer|

    ---
    |sampling_pick-nbviewer|

    ---
    |sampling_stratified-nbviewer|

    ---
    |sampling_vertex-nbviewer|

.. raw:: html

    <div id="preview-gallery-more">
      <a href="#" class="reference internal">Show More</a>
    </div>