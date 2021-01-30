import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="GToolKit", # Replace with your own username
    version="0.0.1",
    author="Guy Boxall",
    author_email="guy.boxall1@gmail.com",
    description="A small package of small tools and scrip i need",
    url="https://github.com/GuyBoh93/GToolKit",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
)