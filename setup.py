from setuptools import setup, find_packages

version="2.3.2"

setup(
    name="homework",
    version=version,
    description="Homework exercise",
    author_email="pm-eng@ndvr.com",
    packages=find_packages(),
    entry_points={"console_scripts": [],},
    install_requires=[
        "click==8.1.3",
        "requests==2.28.1",
        "matplotlib==3.5.2",
        "yfinance==0.2.3"
    ],
)
