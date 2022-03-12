import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ua-framer",
    version="0.0.1",
    author="Nemu627",
    author_email="nemu.otoyume@gmail.com",
    description="Draw the frame of the Ukrainian flag on the image.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nemu627/UA-framer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
