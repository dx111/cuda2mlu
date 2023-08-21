from setuptools import setup

setup(
    name="cuda2mlu",
    version="0.0.1",
    description="rewrites torch CUDA device to use MLU",
    long_description = "A package that rewrites torch device CUDA to use MLU",
    packages=["cuda2mlu"],
    install_requires=["torch", "torch_mlu"],
    setup_requires=[],
    entry_points={
        'console_scripts': [
            'cuda2mlu = cuda2mlu:cmd',
        ]
    },
    python_requires=">=3.6"
)

