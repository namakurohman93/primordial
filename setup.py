import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="primordial",
    version="1.0.0",
    description="Travian 5 API Client framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lijok/primordial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)
