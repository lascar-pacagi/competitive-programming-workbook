"""Export the editable SVG figures to vector PDFs for the course lesson.

Requires Inkscape. Run this script from any directory after editing an SVG.
"""
from pathlib import Path
import subprocess


def main():
    folder = Path(__file__).resolve().parent
    for source in sorted(folder.glob('figure-*.svg')):
        target = source.with_suffix('.pdf')
        subprocess.run(
            [
                'inkscape', str(source), '--export-type=pdf',
                f'--export-filename={target}',
            ],
            check=True,
            capture_output=True,
        )
        print(target.name)


if __name__ == '__main__':
    main()
