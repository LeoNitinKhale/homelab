"""Database router confining the `ops` app to the separate 'ops' Postgres.

The `ops` app holds high-churn / ephemeral operational data (tasks, workflow and
spaced-repetition review state) that we deliberately keep *off* the core
system-of-record DB. This router sends every `ops` model to the 'ops' database
and everything else to 'default' (core). Routing by app_label keeps the code
boundary and the data boundary aligned: the ops app's migrations only ever touch
the ops DB, and no other app's migrations touch it.

Cross-database ForeignKeys are impossible in Django, so `ops` models reference
core records (a trade, a peg, …) by plain id, not FK; relations only ever exist
*within* a single database, which `allow_relation` reflects.
"""

OPS_APP = 'ops'


class OpsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == OPS_APP:
            return 'ops'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == OPS_APP:
            return 'ops'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        ops1 = obj1._meta.app_label == OPS_APP
        ops2 = obj2._meta.app_label == OPS_APP
        return ops1 == ops2

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == OPS_APP:
            return db == 'ops'
        # Every other app (auth, admin, contenttypes, sessions, and the domain
        # apps) lives only on 'default'; the ops DB holds nothing but ops_* tables.
        return db == 'default'
