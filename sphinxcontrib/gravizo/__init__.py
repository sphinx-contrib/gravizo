"""
    sphinxcontrib.gravizo
    ~~~~~~~~~~~~~~~~~~~~~

    Embed PlantUML, DOT, etc. diagrams in your documentation using Gravizo.

    :copyright: Copyright 2020 by MikeSmithEU <copyright@mikesmith.eu>
    :license: BSD, see LICENSE for details.
"""

import pbr.version

if False:
    # For type annotations
    from typing import Any, Dict  # noqa

    from sphinx.application import Sphinx  # noqa

__version__ = pbr.version.VersionInfo('gravizo').version_string()


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]

    from .gravizo import GravizoDirective
    app.add_directive("gravizo", GravizoDirective)

    return {'version': __version__, 'parallel_read_safe': True}
