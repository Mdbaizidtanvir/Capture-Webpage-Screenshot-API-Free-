from setuptools import setup, find_packages

setup(
    name="web_screenshot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Flask',
        'selenium',
        'gunicorn',
    ],
    entry_points={
        'console_scripts': [
            'web_screenshot = app:app.run',
        ],
    },
)
