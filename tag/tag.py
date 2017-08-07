from typing import Set

import anytree

from menu import TagItem


class Tag(anytree.NodeMixin):
    separator = " > "
    fields = ('name', )

    def __init__(self, name, parent=None):
        super().__init__()
        self.name = name
        self._entries = set()  # type: Set[SimpleEntry]
        self.parent = parent
        self._manager = None

    @property
    def manager(self):
        return self.root._manager

    @property
    def entries(self) -> Set['SimpleEntry']:
        return self._entries

    def add_entry(self, entry: "SimpleEntry"):
        if entry not in self._entries:
            self._entries.add(entry)
            entry.add_tag(self)

    def remove_entry(self, entry: "SimpleEntry"):
        self._entries.remove(entry)

    @property
    def item(self):
        return TagItem(self, self.manager)