import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypost",
    version="0.0.1",
    author="Anders Swanson",
    author_email="anders.swanson.93@gmail.com",
    description="Request manager tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anderskswanson/pypost",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)