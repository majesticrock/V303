all: protokoll.pdf

build/plot_phase.pdf: plot1.py phasenverschiebung.csv header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot1.py

build/plot_phase_rauschen.pdf: plot2.py phasenverschiebung.csvheader-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot2.py

build/plot_intensity: plot3.py photo.csvheader-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot3.py

build/main.pdf: build/plot_phase.pdf build/plot_phase_rauschen build/plot_intensity

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

.PHONY: all clean