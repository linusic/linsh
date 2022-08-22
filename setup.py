from setuptools import setup


setup(
    name='linsh',
    version="0.0.2",
    author="linusic",
    author_email='cython_lin@cklin.top',
    description="magic operator for sh",
    url="https://github.com/linusic/linsh",   # Github Repositoriy (auto sync stars ...)
    classifiers=[
        'Intended Audience :: Developers',        
        "Environment :: Console",                 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],  
    py_modules=["linsh"], 
    python_requires='>=3.6',
)
