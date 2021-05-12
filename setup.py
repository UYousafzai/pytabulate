import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytabulate-umark",
    version="0.1.0",
    author="Umar Yousafzai",
    author_email="umaryousafzai9@gmail.com",
    description="in progress package for reading tables metadata from groundtruth xml files stored in UNL format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux (tested)",
    ],
    python_requires='>=3.6',
)