# this is used to build the ML project as a package
from setuptools import find_packages, setup
from typing import List



HYPHEN_E_DOT =  '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    the `requirements.txt` file, excluding the `-e .` entry if it exists.

    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  
        #replaces the new line sign with blanks
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)



    return requirements




setup(
    name = "BYU_ObjDet",
    version = "0.0.1",
    author = "Jimmy",
    author_email="jimdwq@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)


