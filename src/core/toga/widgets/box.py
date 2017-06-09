from src.core.toga.platform import get_platform_factory
from .base import Widget


class Box(Widget):
    '''
    This is a Widget that contains other widgets, but has no rendering or
    interaction of its own.

    :param id:          An identifier for this widget.
    :type  id:          ``str``

    :param style:       an optional style object. If no style is provided then a
                        new one will be created for the widget.
    :type style:        :class:`colosseum.CSSNode`

    :param children:    An optional list of child Widgets that will be in this
                        box.
    :type children:     ``list``
    '''
    def __init__(self, id=None, style=None, children=None, factory=None):
        super().__init__(id=id, style=style, children=children)
        self._children = []

        if factory is None:
            self.factory = get_platform_factory()
        else:
            self.factory = factory
        self._impl = self.factory.Box(creator=self)
        self._create()
        # self._configure()

    def _create(self):
        self._impl.create()

    def _configure(self, children):
        if children:
            for child in children:
                self.add(child)
