from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="Patrick F R Ribeiro",
    author_email="patrick_ribeiro@ymail.com",
    description="Projeto criado durante o curso da DIO.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PatrickFRR/creating_image_processing_packages_pyhton",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)