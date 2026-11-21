"""Run from a Lean 4.33.1 / Mathlib v4.33.1 lake environment."""

from hashlib import sha256
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("statements", type=Path, help="Alpöge's pinned src/Statements.lean")
    args = parser.parse_args()
    source = args.statements.read_bytes()
    if sha256(source).hexdigest() != "79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf":
        raise SystemExit("The upstream Statements.lean checksum differs.")
    version = subprocess.check_output(["lean", "--version"], text=True)
    if "4.33.1" not in version or "819816b2" not in version:
        raise SystemExit("Expected the pinned Lean 4.33.1 compiler.")
    expected = {"product_zero", "box_collision", "simultaneous_return", "polynomial_envelope",
                "recurrence_exponent", "discriminant_envelope"}
    paths = [str(Path(p).resolve()) for p in os.environ["LEAN_PATH"].split(os.pathsep) if p]
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Statements.lean").write_bytes(source)
        shutil.copy(Path(__file__).with_name("FirstCrossing.lean"), root)
        env = dict(os.environ, LEAN_PATH=os.pathsep.join([tmp, *paths]))
        for module in ("Statements", "FirstCrossing"):
            run = subprocess.run(["lean", "-j2", "-R", ".", "-o", module + ".olean", module + ".lean"],
                                 cwd=root, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if run.returncode or "warning:" in run.stdout:
                raise SystemExit(run.stdout or "Lean failed")
        for line in run.stdout.splitlines():
            if "depends on axioms:" not in line:
                raise SystemExit("Unexpected Lean output: " + line)
            name, axioms = line.split(" depends on axioms: ")
            expected.remove(name.strip("'").removeprefix("FirstCrossing."))
            if set(axioms.strip("[]").split(", ")) - {"propext", "Classical.choice", "Quot.sound"}:
                raise SystemExit(line)
            print(line)
        if expected:
            raise SystemExit("Missing axiom reports: " + str(sorted(expected)))


if __name__ == "__main__":
    main()
