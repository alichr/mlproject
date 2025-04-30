from setuptools import setup, find_packages


HYPEN_E_DOT = '-e .'

def get_requirements(file_path):

    requirements = []
    with open(file_path) as file:
        for line in file.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Ali Cheraghian',
    author_email= 'alichr64@gmail.com',
    description='A small ML project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)