from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tunneler",
    version="0.0.1",
    author="Wing-Kit Lee",
    author_email="wklee4993@gmail.com",
    description="A python script to perform ssh tunneling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wingkitlee0/tunneler",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['tunneler=tunneler:main'],
    }
)
