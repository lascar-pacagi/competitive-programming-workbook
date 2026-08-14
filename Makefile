.PHONY: pdf check reference audit public-check

SECTIONS := $(shell find sections -maxdepth 1 -type d -name '[0-9][0-9]_*' | sort)
APPENDICES := $(shell find appendices -mindepth 1 -maxdepth 1 -type d | sort)

pdf:
	quarto render HOW_TO_FIND_IT.qmd --to pdf
	@for section in $(SECTIONS); do \
		if [ -f "$$section/lesson.qmd" ]; then quarto render "$$section/lesson.qmd" --to pdf; fi; \
		if [ -f "$$section/editorial.qmd" ]; then quarto render "$$section/editorial.qmd" --to pdf; fi; \
		if [ -f "$$section/problem_sheet.qmd" ]; then quarto render "$$section/problem_sheet.qmd" --to pdf; fi; \
	done
	@for appendix in $(APPENDICES); do \
		if [ -f "$$appendix/lesson.qmd" ]; then quarto render "$$appendix/lesson.qmd" --to pdf; fi; \
		if [ -f "$$appendix/editorial.qmd" ]; then quarto render "$$appendix/editorial.qmd" --to pdf; fi; \
	done

check:
	python3 tools/check_all.py

reference:
	CP_TARGET=solution python3 tools/check_all.py

audit:
	python3 tools/audit_course.py

public-check:
	python3 tools/check_student_stubs.py
	python3 tools/audit_course.py
	python3 -m compileall -q tools
