from setuptools import setup, find_packages

setup(name = "census-income",
      author= "shreya",
      author_email="shreygold27@gmail.com",
      version="1.0.0",
      packages=find_packages(), # it takes folder having __init__.py as package
    install_requires = ["pandas", "numpy", "flask"],

)