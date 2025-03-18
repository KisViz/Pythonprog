import subprocess
import json
import os
from dataclasses import dataclass
from typing import List


@dataclass
class ClocResult:
    path: str
    language: str
    code: int
    comment: int
    blank: int

    def loc(self):
        return self.code + self.comment + self.blank


def run_cloc(utvonal: str):
    try:
        be = subprocess.run(["cloc", utvonal],capture_output=True, text=True, timeout=5)
        kimenet = json.loads(be.stdout)

        languages = []
        for lang in kimenet.keys():
            if lang not in ["header", "SUM"]:
                languages.append(lang)

        lang = languages[0]
        stat = kimenet[lang]
        return ClocResult(utvonal, lang, stat.get("code", 0), stat.get("comment", 0), stat.get("blank", 0))
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



results = run_cloc_dir("./sajat_mappa", recursive=True)
for res in results:
    print(f"{res.path}: {res.language}, {res.loc()} sor")
