from setuptools import setup,find_packages
setup(
    name='auto',
    version='0.1',
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        'Click',
        'urllib3',
        'certifi',
        'idna',
        'esdk-obs-python',
        'Pillow-PIL',
        'xlrd',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'auto = auto_upload.dropdb:dropdb',
        ]}
)