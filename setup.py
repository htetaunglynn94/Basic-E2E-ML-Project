from setuptools import find_packages, setup




setup(
    name='e2emlproject', 
    version='0.0.1', 
    author='HtetAungLynn',
    author_email='htetaunglynn94@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))