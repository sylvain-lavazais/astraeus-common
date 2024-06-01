from yoyo import step

steps = [
    step(
        '''
        CREATE SCHEMA IF NOT EXISTS "astraeus"
        '''
    ),
    step(
        '''
        CREATE TABLE IF NOT EXISTS "astraeus"."system"
                (
                "key"            jsonb PRIMARY KEY,
                "name"           text,
                "coordinates"    jsonb,
                "require_permit" boolean,
                "information"    jsonb,
                "update_time"    timestamp,
                "primary_star"   jsonb
                )
        '''
    ),
    step(
        '''
        CREATE TABLE IF NOT EXISTS "astraeus"."body"
        (
            "key"                    jsonb PRIMARY KEY,
            "system_key"             jsonb,
            "name"                   text,
            "type"                   text,
            "sub_type"               text,
            "discovery"              jsonb,
            "update_time"            timestamp,
            "materials"              jsonb,
            "solid_composition"      jsonb,
            "atmosphere_composition" jsonb,
            "parents"                jsonb,
            "belts"                  jsonb,
            "rings"                  jsonb,
            "properties"             jsonb
        )
        '''
    ),
    step(
        '''
        ALTER TABLE "astraeus"."body"
            ADD FOREIGN KEY (system_key) REFERENCES "astraeus"."system" (key)
        '''
    )
]
