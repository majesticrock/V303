all: build/plot_phase.pdf build/plot_phase_rauschen.pdf build/plot_intensity

build/plot_phase.pdf: plot1.py phasenverschiebung.csv | build
	python plot1.py

build/plot_phase_rauschen.pdf: plot2.py phasenverschiebung.csv | build
	python plot2.py

build/plot_intensity: plot3.py photo.csv | build
	python plot3.py

build:
	mkdir -p build

clean:
	rm -rf build/*

.PHONY: all clean