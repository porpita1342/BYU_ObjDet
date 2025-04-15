# this is used to build the ML project as a package
from setuptools import find_packages, setup



setup(
    name = "BYU_ObjDet",
    version = "0.0.1",
    author = "Jimmy",
    author_email="jimdwq@gmail.com",
    packages=find_packages(),
    install_requires = ['pandas','numpy','seaborn']
)


