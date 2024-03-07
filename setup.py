from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
  
setup( 
    name='flask_mediapipe_app', 
    version='0.1', 
    description='A sample Python package', 
    author='Dr. Amish Kumar', 
    author_email='amishkumar562@gmail.com', 
    url='https://github.com/amish0/docker_flask_mediapipe',
    packages=['fflask_mediapipe_app'], 
    install_requires=requirements,
    # install_requires=[ 
    #     'numpy', 
    #     'pandas', 
    # ], 
) 