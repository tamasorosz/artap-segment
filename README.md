# artap-segment

[![build-status-image]][travis]

[build-status-image]: https://travis-ci.com/tamasorosz/artap-segment.svg?branch=main
[travis]: https://travis-ci.com/tamasorosz/artap-segment.svg?branch=main
[![codecov](https://codecov.io/gh/tamasorosz/artap-segment/branch/main/graph/badge.svg?token=zH6pBqqnid)](https://codecov.io/gh/tamasorosz/artap-segment)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/tamasorosz/artap-segment.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tamasorosz/artap-segment/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/tamasorosz/artap-segment.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tamasorosz/artap-segment/context:python)

[![Code Style](https://badgen.net/badge/Code%20Style/black?labelColor=2e3a44&color=000000)](https://github.com/psf/black)

SimplE GeoMetry gENeraTion for fem-based optimization

A FEM-based optimization needs a parametrized geometry for the mesh generation. The goal of this project to provide a 
simple set of objects and entities for geometry generation. The defined geometry can be exported for many FEM codes scripting files or svg, dxf formats. 
Moreover, the code will be supports the importation of hand-made svg patterns. For the geometry generation the user can use his/her favourite graphic designer app (e.g. Inkscape) where the user can define the whole goemetry,
or only its part and play with it to generate a geometry like in a jigsaw puzzle. 

