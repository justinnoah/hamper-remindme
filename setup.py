from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='hamper-remindme',
    version='0.1',
    packages=['hamper-remindme'],
    author='Dean Johnson',
    author_email='deanjohnson222@gmail.com',
    url='https://github.com/dean/hamper-remindme',
    install_requires=requirements,
    package_data={'hamper-remindme': ['requirements.txt', 'README.md', 'LICENSE']}
)
