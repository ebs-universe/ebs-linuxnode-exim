

from ebs.linuxnode.core.log import NodeLoggingMixin
from ebs.linuxnode.core.busy import NodeBusyMixin
from ebs.linuxnode.core.config import ElementSpec, ItemSpec

from .local import LocalEximManager


class LocalEximMixin(NodeBusyMixin, NodeLoggingMixin):
    def __init__(self, *args, **kwargs):
        super(LocalEximMixin, self).__init__(*args, **kwargs)
        self._exim = None

    @property
    def exim(self):
        if not self._exim:
            self._exim = LocalEximManager(self)
        return self._exim

    def exim_install(self):
        super(LocalEximMixin, self).exim_install()
        pass

    def install(self):
        super(LocalEximMixin, self).install()
        _elements = {
            'exim_local_enabled': ElementSpec('exim', 'local_enabled', ItemSpec(bool, fallback=True)),
            'exim_local_mountpoint': ElementSpec('exim', 'local_mountpoint', ItemSpec(fallback='/exim')),
        }
        for name, spec in _elements.items():
            self.config.register_element(name, spec)

        self.exim.install()
        self.exim_install()

    def start(self):
        super(LocalEximMixin, self).start()
        self.reactor.callLater(20, self.exim.trigger, 'startup')
