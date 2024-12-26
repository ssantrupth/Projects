from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> list[str]:
    '''
    this function will return the list of requirements '''
    with open(file_path, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  
    return requirements

setup(
    name='mlproject1',
    version='0.0.1',
    description='My ML Projects',
    author='ssantrupth',
    author_email='santrupthsunkari@gmail.com',
    url='https://github.com/ssantrupth/Projects.git',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=get_requirements('requirements.txt'),
)