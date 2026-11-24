"""The Funniest Out-of-Office — make.fun entry (u-kreutzx-the-funniest-out-of-office-054815cf).

Writes the locked one-line OOO reply verbatim to entry.txt inside
MAKEFUN_OUTPUT_DIR (fallback /output), with no trailing newline.

Entry (111 chars / 113 bytes, one line):
"I'm out until Monday. My inbox is answering for me — it just promoted
itself to manager and denied my time off."
"""

import os

ENTRY = ("I'm out until Monday. My inbox is answering for me \u2014 "
         "it just promoted itself to manager and denied my time off.")

# Assert on the EVALUATED entry value (the em dash is \u2014 in source).
assert len(ENTRY) == 111, len(ENTRY)
assert len(ENTRY.encode("utf-8")) == 113, len(ENTRY.encode("utf-8"))
assert "\n" not in ENTRY


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
