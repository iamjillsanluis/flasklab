from datetime import datetime

from seventh.identities.models import Identity


class IdentityRepository(object):
    def __init__(self):
        seed = [
            Identity(guid="1000-a", name="Homer Simpson", created_at=datetime.now()),
            Identity(guid="1000-b", name="Marge Simpson", created_at=datetime.now()),
            Identity(guid="1000-c", name="Bart Simpson", created_at=datetime.now()),
            Identity(guid="1000-d", name="Lisa Simpson", created_at=datetime.now()),
            Identity(guid="1000-e", name="Maggie Simpson", created_at=datetime.now()),
        ]
        self._cache = {x.guid: x for x in seed}

    def add(self, identity):
        if identity.guid not in self._cache:
            self._cache[identity.guid] = identity
        else:
            raise Exception(f"Record with guid: {identity.guid} already exists.")

    def get(self, identity_guid):
        return self._cache.get(identity_guid)

    def all(self):
        return self._cache.values()
