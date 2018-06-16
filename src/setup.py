from setuptools import setup, find_packages


setup(
	name="juxtaposer",
	version="0.1",
	author="Igor Akulov",
	author_email="wmigor@yandex.ru",
	packages=find_packages(),
	entry_points={
		"gui_scripts": ["juxtaposer = juxtaposer.main:main"]
	}
)
