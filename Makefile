build: run-tests
	@pyinstaller FSC/app.py --clean --name FSC -F --windowed

build-debug:
	@pyinstaller FSC/app.py --clean --name FSC_Debug -d -F --console

run-tests:
	@green -vvv --run-coverage