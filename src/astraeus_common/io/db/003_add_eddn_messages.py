from yoyo import step

__depends__ = {"001_initial_db_creation"}

steps = [
    step(
        '''
        CREATE TABLE IF NOT EXISTS "astraeus"."sync_state"
        (
            "id"             uuid PRIMARY KEY,
            "schema"         text,
            "header"         jsonb,
            "message"        jsonb,
            "recv_date"      timestamp default null,
            "sync_date"      timestamp default null
        )
        '''
    )
]
