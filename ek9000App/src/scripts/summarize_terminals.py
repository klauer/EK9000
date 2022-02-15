#!/usr/bin/env python3
"""
python3 find_terminals.py [--json] regex [regex [regex...]]
Where regex is a regular expression to match terminals.

Tool for getting PDO information out of the TwinCAT XML files.

Usage examples:

```bash
$ python3 find_terminals.py EL5042
$ python3 find_terminals.py EL504[0123]
$ python3 find_terminals.py EL5042 --json
```
"""

from __future__ import annotations

import re
import sys

from typing import List
from find_terminals import load_existing_terminals, find_matching

HELP_DOCS = __doc__.strip()


def main(names_to_match: List[str]):
    regex = re.compile("|".join(names_to_match), flags=re.IGNORECASE)
    existing_terminals = load_existing_terminals()
    for info in find_matching(regex):
        supported = info.name.split("-")[0] in existing_terminals
        print(
            "\t".join(
                (
                    info.name,
                    info.revision,
                    info.description,
                    "Yes" if supported else "No",
                    info.url or "n/a",
                )
            )
        )


if __name__ == "__main__":
    names_to_match = sys.argv[1:]
    if not names_to_match:
        print(HELP_DOCS)
        sys.exit(1)

    main(names_to_match)
