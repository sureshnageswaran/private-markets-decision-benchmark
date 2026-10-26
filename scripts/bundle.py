"""Bundle benchmarks/**/*.json into a single tests.json, ordered by manifest.json."""
import json
import pathlib
import sys

root = pathlib.Path("benchmarks")
manifest = json.loads((root / "manifest.json").read_text())

tests = []
for entry in manifest["tests"]:
    test = json.loads((root / entry["path"]).read_text())
    if test["id"] != entry["id"]:
        sys.exit(f"id mismatch in {entry['path']}: {test['id']} != {entry['id']}")
    tests.append({"id": test["id"], "domain": entry["domain"], **{k: v for k, v in test.items() if k != "id"}})

if manifest["test_count"] != len(tests):
    sys.exit(f"manifest test_count {manifest['test_count']} != {len(tests)} entries")

listed = {entry["path"] for entry in manifest["tests"]}
on_disk = {str(p.relative_to(root)) for p in root.glob("*/*.json")}
if listed != on_disk:
    sys.exit(f"manifest/disk mismatch: {sorted(listed ^ on_disk)}")

pathlib.Path("tests.json").write_text(json.dumps(tests, indent=2) + "\n")
print(f"Wrote tests.json with {len(tests)} tests")
