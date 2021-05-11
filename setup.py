from setuptools import setup

requirements = [
    "aiogram", "discord.py"
]

kwargs = {
    "python_requires": ">=3.5",
    "install_requires": requirements,
    "author": "Vincy.exe",
    "description": "A bridge between Discord and Telegram based on discord.py and aiogram",
}

setup(name="telecord", **kwargs)
