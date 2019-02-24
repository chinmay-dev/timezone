import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timezone-task-chinmay-dev",
    version="0.0.1",
    author="Chinmay Deshpande",
    author_email="chinmaydeshpande0@gmail.com",
    description="Check whether task is created in the mentioned time range",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chinmay-dev/timezone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)