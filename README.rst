=====================
sphinxcontrib-gravizo
=====================

.. image:: https://travis-ci.org/MikeSmithEU/sphinxcontrib-gravizo.svg?branch=master
    :target: https://travis-ci.org/MikeSmithEU/sphinxcontrib-gravizo

Embed PlantUML, DOT, etc. diagrams in your documentation using Gravizo.

Examples
--------

Inline graph, show as png::

    .. gravizo:: png
        @startuml
        Alice -> Bob: Authentication Request
        Bob --> Alice: Authentication Response

        Alice -> Bob: Another authentication Request
        Alice <-- Bob: Another authentication Response
        @enduml

Load from a file, show as svg::

    .. gravizo:: ./path/to/graph.puml svg

Links
-----

- Source: https://github.com/sphinxcontrib/gravizo
- Bugs: https://github.com/sphinxcontrib/gravizo/issues
