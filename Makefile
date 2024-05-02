
init:
	pip3 install -r requirements.txt

build: unstall
	pip3 install .

unstall:
	pip3 uninstall SimpleFTPServer
