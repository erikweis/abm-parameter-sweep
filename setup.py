import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abm-parameter-sweep",
    version="0.0.1",
    author="Erik Weis",
    author_email="erik.weis@uvm.com",
    description="For running parameter in the context of an agent-based model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/abm-parameter-sweep",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/abm-parameter-sweep/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)