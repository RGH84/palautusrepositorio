class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license_info, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license_info
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license}\n\n"
            "Authors:\n" +
            "\n".join(f"- {author}" for author in self.authors) +
            "\n\nDependencies:\n" +
            "\n".join(f"- {dep}" for dep in self.dependencies) +
            "\n\nDevelopment dependencies:\n" +
            "\n".join(f"- {dev_dep}" for dev_dep in self.dev_dependencies)
        )
