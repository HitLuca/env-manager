"""
project setup script
"""
from setuptools import setup
import versioneer

readme = open("README.md", "rb").read().decode("utf-8")

setup(
    install_requires=["env-flag==2.1.0"],
    name="env-manager",
    version=versioneer.get_version(),  # type: ignore
    author="Luca Simonetto",
    author_email="luca.simonetto.94@gmail.com",
    description="Environment variables manager",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/HitLuca/env-manager",
    packages=["env_manager"],
    package_data={"env_manager": ["py.typed"]},
    cmdclass=versioneer.get_cmdclass(),  # type: ignore
    python_requires=">3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
)
