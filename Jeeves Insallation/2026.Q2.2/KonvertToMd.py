from contextlib import chdir
from pathlib import Path

try:
    import pymupdf
except ModuleNotFoundError as e:
    if e.name != "pymupdf":
        raise
    raise SystemExit(
        "Saknar paketet PyMuPDF. Installera det med: "
        "python -m pip install pymupdf"
    ) from e

# Mappar
INPUT_FOLDER = Path(__file__).resolve().parent
OUTPUT_FOLDER = INPUT_FOLDER / "markdown"
IMAGE_FOLDER = OUTPUT_FOLDER / "images"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
IMAGE_FOLDER.mkdir(parents=True, exist_ok=True)

pdf_files = list(INPUT_FOLDER.glob("*.pdf"))

print(f"Hittade {len(pdf_files)} PDF-filer.")

for pdf_file in pdf_files:
    try:
        print(f"Konverterar: {pdf_file.name}")

        with chdir(OUTPUT_FOLDER):
            with pymupdf.open(str(pdf_file)) as document:
                md_text = document.to_markdown(
                    write_images=True,
                    image_path="images",
                    filename=pdf_file.stem,
                )

        output_file = OUTPUT_FOLDER / f"{pdf_file.stem}.md"

        output_file.write_text(
            md_text,
            encoding="utf-8"
        )

        print(f"OK -> {output_file}")

    except Exception as e:
        print(f"FEL {pdf_file.name}: {e}")

print("Klart!")