import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="milkycow", # Replace with your own username
    version="0.0.1",
    author="Madhava-mng",
    author_email="alformint@gmail.com",
    description="Simple encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Madhava-mng/Milkycow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ["codelib"]
)
