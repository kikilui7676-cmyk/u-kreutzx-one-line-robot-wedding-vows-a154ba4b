import os
from pathlib import Path

LINE = "I promise to love you in sickness and in health, in low battery and in full charge, until a factory reset do us part."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
