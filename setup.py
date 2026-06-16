from setuptools import find_packages, setup
from typing import List





HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:

    '''
    This function will return the list of requirements as string.
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

# Define meta data about my package
setup(
    name='e2emlproject', 
    version='0.0.1', 
    author='HtetAungLynn',
    author_email='htetaunglynn94@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))