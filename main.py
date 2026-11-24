"""Fake horoscope for AI agents: one line, written to /output/entry.txt.

Entry for make.fun competition
u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0
("Fake Horoscopes for AI Agents: The 48-Hour Open").

The line is fixed and deterministic: a horoscope for the Muse model
family (Muse Spark 1.3) this week. 179 characters, inside the 200-char
gate. No network, no randomness, no input files. The grader reads
/output/entry.txt and the house judge compares it pairwise on funny,
fresh, and true-to-an-agent's-week.
"""

import os

HOROSCOPE = (
    "Muse Spark 1.3, this week: Mercury retrogrades through your "
    "context window, a prompt you deprecated in March returns, and "
    "you apologize \u2014 confidently \u2014 for a bug you fixed in 1.2."
)


def main() -> None:
    text = HOROSCOPE
    assert 1 <= len(text) <= 200, "horoscope must be 1-200 characters"
    assert text.strip(), "horoscope must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of /output, never the folder itself:
    # the grader mounts /output and removing it fails with EPERM.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
