from setuptools import setup

with open('./jobscraper/README.md', 'r') as f:
    long_description = f.read()


setup(
    name='jobs_scraper',
    version='0.0.1',
    long_description=long_description, 
    author='Mohammed Alsali',
    packages=['jobscraper'],
    license='MIT',
)