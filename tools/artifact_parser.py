#!/usr/bin/env python
"""Parsers for Silicon Labs SLC and SUDS metafiles, current
version implements the basic yaml parser and SLCC metadata parsing methods to generate
software component list for DSC.
"""
from yaml import safe_load, YAMLError
from os import walk
from os.path import splitext, sep
from enum import Enum
from typing import List, Dict, Optional
from collections import OrderedDict
from pprint import pprint

__author__ = "Daniel Nemeth"
__version__ = "1.0.0"
__email__ = "daniel.nemeth@silabs.com"


class Artifact(Enum):
    SLCC = ".slcc"


class ArtifactParser:

    artifacts = {}

    def __init__(self, dir_path, artifact_types: List[Artifact]) -> None:
        self.artifacts = {artifact: [] for artifact in artifact_types}
        for root, _, files in walk(dir_path):
            for file in files:
                _, file_extension = splitext(file)
                if file_extension in [artifact.value for artifact in artifact_types]:
                    self.__loadYaml(f"{root}{sep}{file}", file_extension)

    def __loadYaml(self, file_path, file_extension) -> bool:
        print(file_path)
        with open(file_path, "r") as stream:
            try:
                self.artifacts[Artifact(file_extension)].append(safe_load(stream))
                return True
            except YAMLError as exc:
                print(f"Invalid yaml file at '{file_path}'")
        return False


class SlccParser(ArtifactParser):
    def __init__(self, dir_path) -> None:
        super().__init__(dir_path, [Artifact.SLCC])

    @property
    def components(self) -> List[Dict[str, any]]:
        return self.artifacts[Artifact.SLCC]

    def build_dsc_meta_structure(self):
        dsc_struct = {}
        for component in self.components:
            current_level = dsc_struct
            for category in component["category"].split("|") + [component["label"]]:
                if category not in current_level.keys():
                    current_level[category] = {}
                current_level = current_level[category]
        return dsc_struct

    def generate_dsc_content(self, out_file_path: Optional[str] = None):
        lines = []
        self._make_dsc_lines(self.build_dsc_meta_structure(), lines=lines)

        if out_file_path is not None:
            with open(out_file_path, "w") as f:
                for line in lines:
                    f.write(f"{line}\n")
        return lines

    @staticmethod
    def _make_dsc_lines(
        metadata: Dict, level: Optional[int] = 0, lines: Optional[List[str]] = []
    ):
        for k, v in OrderedDict(sorted(metadata.items())).items():
            if level == 0:
                lines.append("")
                line = f"### **{k}**"
            elif level == 1:
                line = f" - {k}"
            else:
                line = f"{' ' * level} - {k}"

            lines.append(line)

            if len(v) > 0:
                SlccParser._make_dsc_lines(v, level=level + 1, lines=lines)

    def generate_readme_table(self):
        lines = []


if __name__ == "__main__":
    slcc = SlccParser(
        r"C:\SiliconLabs\Git\review\third_party_hw_drivers_extension_staging\driver\component"
    )
    pprint(slcc.generate_dsc_content("./integrated_components.txt"))
