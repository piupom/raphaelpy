Raphaëlpy documentation
=======================

.. automodule:: raphaelpy

.. toctree::
   :maxdepth: 2

Raphael
-------
.. autodata:: Raphael
.. autodata:: null

.. autoclass:: _Raphael
   :members: __call__, el, fn

Paper
-----
.. autoclass:: Paper
   :members: bottom, circle, clear, ellipse, getById, image, path, rect, set, setFinish, setStart, text, top, save, __len__, pattern, marker, clipPath

Element
-------
.. autoclass:: RaphaelElement
   :members: attr, clone, getBBox, hide, id, insertAfter, insertBefore, next, paper, prev, remove, rotate, scale, show, toBack, toFront, transform, translate, junk_string_to_include_transltate_to_html
   :inherited-members:

Set
---
.. autoclass:: Set
   :members: clear, exclude, pop, push, splice, __len__
