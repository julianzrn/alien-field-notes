"""Entry for make.fun competition: u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "Four stars for the dogs, one for their owners. "
MIDDLE = "The planet's best species greets every stranger at full volume and has negotiated permanent indoor rights. "
LANDING = "Humans hold the leash and the debt."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
