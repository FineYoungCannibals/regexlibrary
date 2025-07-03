# REgexlib

Common regex and text classification utilities for our Airflow pipelines.

## Usage

```python
import myregexlib

if myregexlib.matches_phone("555-123-4567"):
    print("Looks like a phone number")