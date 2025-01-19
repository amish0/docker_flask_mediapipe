from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()
  
setup( 
    name='flask_opencv_app', 
    version='0.1', 
    description='A sample Python package', 
    author='Dr. Amish Kumar', 
    author_email='amishkumar562@gmail.com', 
    url='https://github.com/amish0/docker_flask_mediapipe',
    packages=find_packages(), 
    include_package_data=True,
    
    package_data={
        # If any package contains data files, include them here:
        '': ['templates/*', 'static/*'],
    },
    # packages=['fmd'],
    install_requires=requirements,
    python_requires='>=3.6',
)