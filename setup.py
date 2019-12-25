import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

install_requires = []
with open("requirements.txt", "r") as f:
    item = f.readline().strip()
    while item:
        if item.startswith("-e "):
            egg = item.split("egg=")[-1]
            install_requires.append(f"{egg}@{item[3:]}")
        else:
            install_requires.append(item)
        item = f.readline().strip()

setuptools.setup(
    name="landbridge_im",
    version="0.1.0",
    author="Chaoqian Xu",
    author_email="chaoranxu@gmail.com",
    description="CMW system of landbridge project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@bitbros.com:/landbridge-im",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
