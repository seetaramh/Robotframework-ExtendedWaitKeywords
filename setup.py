import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ExtendedWaitKeywords",
    version="0.0.1",
    author="Seetaram Hegde",
    author_email="seetaramhegde@gmail.com",
    description="Extended Wait Keywords for SeleniumLibrary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seetaramh/Robotframework-ExtendedWaitKeywords",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)