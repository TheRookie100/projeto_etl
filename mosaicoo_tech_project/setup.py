from setuptools import find_packages, setup

setup(
    name="mosaicoo_tech_project",
    packages=find_packages(exclude=["mosaicoo_tech_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
