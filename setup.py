from setuptools import setup

setup(
    name="SimpleFTPServer",
    version="0.1",
    description="A simple FTP server",
    platforms=["Unix", "Windows"],
    scripts=["ftpserver.py"],
    install_requires=["python-ftp-server"]
)