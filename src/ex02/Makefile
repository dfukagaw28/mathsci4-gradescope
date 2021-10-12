TARGETS := $(wildcard tests/* *)
TARGETS := $(filter-out autograder.zip Makefile, $(TARGETS))

autograder.zip: $(TARGETS)
	echo $(TARGETS)
	zip -r autograder.zip * -x autograder.zip Makefile

.PHONY: all
all: autograder.zip
