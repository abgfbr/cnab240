# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='cnab240',
    version='0.02.1',
    author='Tracy Web Technologies',
    author_email='contato@tracy.com.br',
    url='https://github.com/TracyWebTech/cnab240',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools-git'],
    provides=[
        'cnab'
    ],
    license='MIT',
    description='Classe para gerar arquivo de remessa e leitura de retorno no '
                                                            'padrão CNAB',
    long_description=open('README.md', 'r').read(),
    download_url='https://github.com/kmee/cnab',
    scripts=[],
    classifiers=[],
    platforms='any',
    test_suite='',
    tests_require=[],
)
