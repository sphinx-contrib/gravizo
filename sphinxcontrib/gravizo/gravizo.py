"""
    sphinxcontrib.gravizo
    ~~~~~~~~~~~~~~~~~~~~~

    Embed PlantUML, DOT, etc. diagrams in your documentation using Gravizo.

    :copyright: Copyright 2020 by MikeSmithEU <copyright@mikesmith.eu>
    :license: BSD, see LICENSE for details.
"""

from urllib.parse import quote

from docutils import nodes
from docutils.parsers.rst import Directive


class GravizoDirective(Directive):
    """
    The graphviz directive.

    Example usages:

    ```rst
    .. gravizo:: png
        @startuml
        Alice -> Bob: Authentication Request
        Bob --> Alice: Authentication Response

        Alice -> Bob: Another authentication Request
        Alice <-- Bob: Another authentication Response
        @enduml
    ```

    ```rst
    .. gravizo:: ./path/to/graph.puml svg
    ```
    """
    optional_arguments = 1
    has_content = True

    known_formats = {
        'svg': 'http://gravizo.com/svg?%s',
        'png': 'http://gravizo.com/g?%s',
    }
    _format = 'svg'

    def run(self):
        args = self.arguments
        env = self.state.document.settings.env
        warning = self.state.document.reporter.warning

        if (len(args) == 0) and (len(self.content) == 0):
            return [
                warning("gravizo needs either contents or a filename argument")
            ]

        if len(self.content) != 0:
            contents = self.content.join('\n')
        else:
            filename = args.pop(0)
            relfn, absfn = env.relfn2path(filename)
            env.note_dependency(relfn)

            try:
                with open(absfn, 'r') as source_file:
                    contents = source_file.read()
            except (IOError, UnicodeDecodeError) as err:
                return [
                    warning('gravizo: file %r read error: %s' % (filename, err),
                            line=self.lineno)
                ]

        try:
            self._format = args.pop(0).lcase()
        except IndexError:
            pass

        if self._format not in self.known_formats:
            format_args = (
                self._format,
                ', '.join(map(repr,
                              self.known_formats.keys()))
                )

            return [
                warning("gravizo: unrecognized format %r, available formats: %s" % (format_args,),
                        line=self.lineno)
            ]

        image = nodes.image(uri=self.image_url(contents))
        return [image]

    @staticmethod
    def escape(src):
        """
        Properly escapes the graph data
        """
        return quote(bytes(src.replace('\n', ';'), 'utf-8'))

    def image_url(self, src):
        """
        Get the image url for graph data
        """
        return self.known_formats[self._format] % (self.escape(src),)
