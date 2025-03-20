import subprocess
import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class Tarol:
    path: str
    language: str
    code: int
    comment: int
    blank: int

    def loc(self):
        return self.code + self.comment + self.blank


def run_cloc(utvonal: str):
    try:

        cp = subprocess.run(["cloc", "utils"], capture_output=True, text=True)
        darabolt = cp.stdout.split()

        # print(cp.stdout)
        # print(cp.stdout.split()[20])

        return Tarol(utvonal, darabolt[10], int(darabolt[20]), int(darabolt[19]), int(darabolt[18]))
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return None


def run_cloc_dir(mappa: str, recursive: bool):
    vege = []
    for root, _, files in os.walk(mappa):
        for file in files:
            file_path = os.path.join(root, file)
            cloc_result = run_cloc(file_path)
            if cloc_result:
                vege.append(cloc_result)
        if not recursive:
            break
    return vege


tmp = run_cloc("utils")
print(tmp)
print(tmp.loc())
results = run_cloc_dir("utils", recursive=True)
for res in results:
    print(f"{res.path}: {res.language}, {res.loc()} sor")
