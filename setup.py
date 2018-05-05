from setuptools import setup
from collections import defaultdict

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


requirements = []
extras = defaultdict(list)
for r in parse_requirements('requirements.txt', session='hack'):
    if r.markers:
        extras[':' + str(r.markers)].append(str(r.req))
    else:
        requirements.append(str(r.req))

setup(
    name='Pocket',
    version='0.0.1',
    description='A microservice framework written in Flask using the Django ORM',
    author='Zack Kollar',
    author_email='me@seedyrom.io',
    license='MIT',
    packages=['pocket'],
    install_requires=requirements,
    extras_require=extras,
)