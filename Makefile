.PHONY: pdf check reference

SECTIONS := $(shell find sections -maxdepth 1 -type d -name '[0-9][0-9]_*' | sort)

pdf:
	@for section in $(SECTIONS); do \
		if [ -f "$$section/lesson.qmd" ]; then quarto render "$$section/lesson.qmd" --to pdf; fi; \
		if [ -f "$$section/editorial.qmd" ]; then quarto render "$$section/editorial.qmd" --to pdf; fi; \
	done

check:
	python3 tools/check_all.py

reference:
	CP_TARGET=solution python3 tools/check_all.py

