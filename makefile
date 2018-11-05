all: build/main.pdf

build/plot_phase.pdf: plot1.py phasenverschiebung.csv header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot1.py

build/plot_phase_rauschen.pdf: plot2.py phasenverschiebung.csv header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2.py

build/plot_intensity.pdf: plot3.py photo.csv header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot3.py

build/main.pdf: build/plot_phase.pdf build/plot_phase_rauschen.pdf build/plot_intensity.pdf content/tabelle1.tex content/tabelle2.tex lit.bib

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build/*

FORCE:

.PHONY: all clean