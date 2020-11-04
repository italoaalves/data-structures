import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="projeto-ed-italoaalves",  # Replace with your own username
    version="0.0.1",
    author="Felipe Galdino, Ítalo Alves",
    author_email="felipegsousa@gmail.com, italo.alves.jp@gmail.com",
    description="Data structures using pokemon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/italoaalves/projeto-ed",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
