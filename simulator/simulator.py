import time
from datetime import datetime

events = [
    "TEST_KEY_EVENT: A",
    "TEST_KEY_EVENT: B",
    "TEST_KEY_EVENT: C",
    "TEST_KEY_EVENT: ENTER",
    "TEST_KEY_EVENT: CTRL+C"
]

with open("../logs/test_key_events.log", "a") as log:
    for event in events:
        timestamp = datetime.now().isoformat()

        entry = f"{timestamp} | {event}\n"
        log.write(entry)
        log.flush()

        print(entry.strip())
        time.sleep(2)

print("Keylogger simulation completed.")