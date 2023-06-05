from distutils.core import setup
REQUIRES = [
    'records',
    'structlog',
    'allure-pytest'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/surovp/db_client.git',
    license='MIT',
    author='Pavel Surov',
    author_email='-',
    install_requires=REQUIRES,
    description='database client with allure and logger'
)
