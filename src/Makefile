OBJDIR := ./zip
TARGETS := $(wildcard */)
TARGETS := $(filter-out zip/, $(TARGETS))
OBJECTS := $(addprefix $(OBJDIR)/, $(TARGETS:/=.zip))

.PHONY: all
all: $(OBJECTS)
	#

.PHONY: $(TARGETS)
$(TARGETS):
	$(MAKE) -C $@

%/autograder.zip: %
	echo $@

$(OBJDIR)/%.zip: %/autograder.zip
	cp -p $< $@
