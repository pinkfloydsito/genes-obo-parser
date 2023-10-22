PYTHON := python
SRC_DIR := src
MODELS_FILE := $(SRC_DIR).models
DATABASE_FILE := $(SRC_DIR).database.py
MAIN_FILE := $(SRC_DIR).main.py
DB_NAME := obo_genes

test:
	behave

all: run

run: create_db
	$(PYTHON) $(MAIN_FILE)

create_db:
	- createdb $(DB_NAME)
	- $(PYTHON) -c 'from $(MODELS_FILE) import Base, engine; Base.metadata.create_all(bind=engine)'

clean_db:
	$(PYTHON) -c 'from $(MODELS_FILE) import Base, engine; Base.metadata.drop_all(bind=engine)'

.PHONY: all run create_db clean_db test
