import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyANSI",
    version="1.1.0",
    author="Oliver Jane",
    description="Easy ANSI control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/oliverjane/PyANSI",
    project_urls = {
        "Bug Tracker": "https://github.com/oliverjane/PyANSI/issues"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ]
)
