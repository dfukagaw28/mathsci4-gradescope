TARGETS := $(wildcard tests/* *)
TARGETS := $(filter-out autograder.zip Makefile, $(TARGETS))

autograder.zip: $(TARGETS)
	rm -f autograder.zip
	zip -r autograder.zip * -x autograder.zip Makefile

.PHONY: all
all: autograder.zip

.PHONY: clean
clean:
	rm -f autograder.zip
