
from setuptools import setup

required_python_version = (3, 6)
required_python_string=">=" + ".".join(map(str, required_python_version))


setup(
    name="simple_signal_handler",
    version="0.1.0",
    description="A wrapper for handling signals in Python via exceptions.",
    url="https://github.com/timkittel/simple_signal_handler/",
    author="Tim Kittel",
    author_email="Tim.Kittel@pik-potsdam.de",
    license="GNU Lesser General Public License v3.0",
    packages=["simple_signal_handler"],
    python_requires=required_python_string,
    # install_requires=[
    # ],
    zip_safe=False,
)
