from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='dexo',
    version='3.4',
    author='Kavin Bharathi',
    author_email='r.m.kavinbharathi@gmail.com',
    description='A cli for a quick and easy web dev kit',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/kavinbharathii/dexo',
    packages = find_packages(),
    install_requires=[
        requirements
    ],
    python_requires='>=3.5',
    entry_points = '''
        [console_scripts]
        dexo=dexo.__main__:main
    '''
)

