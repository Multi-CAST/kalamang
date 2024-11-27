from setuptools import setup


setup(
    name='cldfbench_mckalamang',
    py_modules=['cldfbench_mckalamang'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'mckalamang=cldfbench_mckalamang:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
