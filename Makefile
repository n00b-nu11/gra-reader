voicevox/up:
	docker run -it --rm -p 50021:50021 hiroshiba/voicevox_engine:cpu-ubuntu20.04-0.10.4

setup:
	python3 -m venv .venv
	source ./.venv/bin/activate
	python3 -m pip install -r requirements.txt

run:
	python3 main.py
	
