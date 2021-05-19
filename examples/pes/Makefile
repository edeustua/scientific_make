# INPUTS holds the names of all input files.
INPUTS := $(wildcard inputs/*.inp)
# The variable OUTPUTS holds the names of all
# single-energy-point files that will be computed
# to generate the PES figure.
OUTPUTS := $(addsuffix .dat,$(subst inputs,outputs,$(INPUTS)))
FIGURE := h2_dissociation.png

.PHONY: clean view

# Plot the PES figure, that is our final goal.
$(FIGURE): $(OUTPUTS) plot_pes.py
	python3 plot_pes.py $(OUTPUTS)

# Order-only prerequisite to ensure the creation of
# the outputs folder
$(OUTPUTS): | outputs

# Pattern rule that converts and input file into
# a PSI4 output file i.e. this rule runs the
# actual calculation.
outputs/%.dat: inputs/%
	psi4 -o $@ $<

# Outputs folder creation
outputs:
	mkdir $@

# This is a phony rule which helps in cleaning up
# the project.
clean:
	rm -fr outputs $(FIGURE)

# This is a helper to open the resulting figure
view:
	xdg-open $(FIGURE)
