"""
Recursively cross-compiles MicroPython project sources.

Wraps mpy-cross:
* https://pypi.org/project/mpy-cross/
* https://docs.micropython.org/en/v1.23.0/reference/mpyfiles.html
"""

import shutil
import argparse
import logging
from pathlib import Path
import sys
import mpy_cross
import subprocess

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(_handler)


COPY_ONLY = (Path("main.py"), Path("boot.py"))


def _get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="MPY_BUILD",
    )

    parser.add_argument(
        "-s",
        "--src",
        required=True,
        help="Path to directory containing the source *.py package/module tree.",
    )
    parser.add_argument(
        "-d",
        "--dest",
        required=True,
        help="Path to directory for the resulting build artifact tree.",
    )
    parser.add_argument(
        "--arch",
        help="""
            Architecture for native emitter; 
            x86, x64, armv6, armv6m, armv7m, armv7em, armv7emsp, armv7emdp, xtensa, xtensawin.
        """,
    )

    return parser


class BuildError(Exception):
    """Generic build process error"""


def _build_module(
    src: str,
    dest: str,
    src_embed: str,
    arch: str | None,
) -> None:
    """_summary_

    Args:
        src (str): Path to the source Python module.
        dest (str): Path to the output compiled bytecode module.
        src_embed (str): Path to the compilation source, to be embedded in the bytecode.
        arch (str | None): _description_

    Raises:
        BuildError: _description_
    """
    mpy_args = [
        mpy_cross.mpy_cross,
        "-v",
        "-o",  # Output file
        dest,
        "-s",
        src_embed,  # Source filename to embed in the compiled bytecode
    ]

    if arch:
        mpy_args.append(f"-march={arch}")

    mpy_args.append(src)  # Input file

    result = subprocess.run(mpy_args, capture_output=True)

    try:
        result.check_returncode()
    except subprocess.CalledProcessError as err:
        logger.error("STDOUT='%s'", result.stdout.decode())

        raise BuildError("Cross-compilation failed") from err


def _build_recursive(
    src_dir: Path,
    dest_dir: Path,
    arch: str | None,
) -> None:
    """Recursively cross compiles the target directory.

    Reflects the source directory tree structure in the destination.

    Args:
        src_dir (Path): Sources directory
        dest_dir (Path): Destination directory
        arch (str | None): mpy-cross target architecture
    """
    mpy_cross.fix_perms()

    for src in src_dir.rglob("*.py"):
        src_rel = src.relative_to(src_dir)

        dest_parent = dest_dir / src_rel.parent
        dest_parent.mkdir(parents=True, exist_ok=True)

        # The bootloader will not load boot and main if they're pre-compiled (.upy).
        if src_rel in COPY_ONLY:
            dest = dest_parent / src.name

            logger.info(f"Copying as-is <src>/{src_rel} -> <dest>/{dest.relative_to(dest_dir)}")

            shutil.copy(src, dest)
        else:
            dest = dest_parent / f"{src.stem}.mpy"

            logger.info(f"Cross-compiling <src>/{src_rel} -> <dest>/{dest.relative_to(dest_dir)}")

            _build_module(
                src=str(src.resolve()),
                dest=str(dest.resolve()),
                src_embed=str(src_rel),
                arch=arch,
            )


def main():
    args = _get_parser().parse_args()
    logger.debug(f"{args=}")

    _build_recursive(
        src_dir=Path(args.src),
        dest_dir=Path(args.dest),
        arch=args.arch,
    )

    logger.info("Done")


if __name__ == "__main__":
    main()
