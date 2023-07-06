.PHONY: prepare  test

prepare: model.pickle

model.pickle:
	python3 -m gzip -d model.pickle.gz

test:
	python -m pytest tests
