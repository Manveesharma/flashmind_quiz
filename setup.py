from setuptools import setup

setup(
    name="flashmind",
    version="1.0",
    py_modules=["flashmind_cli"],
    install_requires=["requests", "pyttsx3"],
    entry_points={
        "console_scripts": [
            "flashmind=flashmind_cli:main",
        ],
    },
)
