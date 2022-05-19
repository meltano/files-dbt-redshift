from setuptools import find_packages, setup

setup(
    name="files-dbt-redshift",
    version="0.1",
    description="Meltano project files for dbt-redshift",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/models/.gitkeep",
            "transform/profiles/redshift/profiles.yml",
            "transform/.gitignore",
            "transform/dbt_project.yml",
        ]
    },
)
