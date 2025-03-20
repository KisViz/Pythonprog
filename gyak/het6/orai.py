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

        return Tarol(utvonal, darabolt[16], int(darabolt[20]), int(darabolt[19]), int(darabolt[18]))
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


def max_loc(mappa: str, recursive: bool):
    results = run_cloc_dir(mappa, recursive)

    if not results:
        return ""

    def get_loc(result):
        return result.loc()

    return max(results, key=get_loc).path

tmp = run_cloc("utils")
print(tmp)
print(tmp.loc())
vege = run_cloc_dir("utils", recursive=True)
for elem in vege:
    print(f"{elem.path}: {elem.language}, {elem.loc()} sor")
    # print(f", {elem.loc()} sor")
print(max_loc("utils", True))