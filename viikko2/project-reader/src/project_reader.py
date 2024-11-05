import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
      
        toml_data = tomli.loads(content)

        name = toml_data.get("tool", {}).get("poetry", {}).get("name", "Unknown")
        description = toml_data.get("tool", {}).get("poetry", {}).get("description", "No description")
        license_info = toml_data.get("tool", {}).get("poetry", {}).get("license", "No license")
        authors = toml_data.get("tool", {}).get("poetry", {}).get("authors", [])
        dependencies = list(toml_data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(toml_data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        return Project(name, description, dependencies, dev_dependencies, license_info, authors)
