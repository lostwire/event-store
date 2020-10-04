CREATE_TABLE_EVENT = """
    CREATE TABLE IF NOT EXISTS event (
        id TEXT NOT NULL PRIMARY KEY,
        seq INTEGER,
        stream TEXT NOT NULL,
        version INTEGER NOT NULL,
        FOREIGN KEY(stream) REFERENCES stream(id))"""

CREATE_TRIGGER_AUTO_SEQUENCE = """
    CREATE TRIGGER IF NOT EXISTS auto_sequence AFTER INSERT ON event"""

INITIALIZE = [
    CREATE_TABLE_EVENT,
    CREATE_TRIGGER_AUTO_INCREMENT ]
