# Makefile for converting .ui files to Python with PySide6

UIC = pyside6-uic
UI_DIR = src/view/ui
PY_DIR = src/view/ui
UI_FILES := $(wildcard $(UI_DIR)/*.ui)
PY_FILES := $(UI_FILES:.ui=_ui.py)

# default target: build all python files
all: $(PY_FILES)

# rule to convert .ui -> _ui.py
%_ui.py: %.ui
	$(UIC) $< -o $@

clean:
	rm -f $(PY_FILES)

.PHONY: all clean