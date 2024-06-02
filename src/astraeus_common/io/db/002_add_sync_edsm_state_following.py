from yoyo import step

__depends__ = {"001_initial_db_creation"}

steps = [
    step(
        '''
        CREATE TABLE IF NOT EXISTS "astraeus"."sync_state"
        (
            "key"            jsonb PRIMARY KEY,
            "sync_date"      timestamp not null,
            "type"           text      not null,
            "sync_hash"      text,
            "previous_state" jsonb
        )
        '''
    )
]
