import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="exencolorlogs",
    version="0.3",
    description="Package for colorlogs",
    long_description=long_description,
    author="Exenifix",
    url="https://github.com/Exenifix/exencolorlogs",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    python_requires=">=3.7",
)
