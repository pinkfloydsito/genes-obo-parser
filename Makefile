PYTHON := python
SRC_DIR := src
MODELS_FILE := $(SRC_DIR).models
MAIN_FILE := main.py
DB_NAME := obo_genes_dev
TEST_DB_NAME := obo_genes_test
OBO_FILE_PATH := './files/go-basic.obo' 

all: run

run: create_db
	DEVELOPMENT=1  DEVELOPMENT=1 $(PYTHON) -m src.main $(OBO_FILE_PATH)

create_db:
	- createdb $(DB_NAME)
	- DEVELOPMENT=1 $(PYTHON) -c 'from $(MODELS_FILE) import Base, engine; Base.metadata.create_all(bind=engine)'

create_test_db:
	- createdb $(TEST_DB_NAME)
	- TEST=1 $(PYTHON) -c 'from $(MODELS_FILE) import Base, engine; Base.metadata.create_all(bind=engine)'

clean_db:
	DEVELOPMENT=1 $(PYTHON) -c 'from $(MODELS_FILE) import Base, engine; Base.metadata.drop_all(bind=engine)'

clean_test_db:
	TEST=1 $(PYTHON) -c 'from $(MODELS_FILE) import Base, engine; Base.metadata.drop_all(bind=engine)'

test: clean_test_db create_test_db 
	TEST=1 behave --no-capture

.PHONY: all run create_db clean_db test
