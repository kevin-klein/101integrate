include Makefile.vars
include ../Makefile.vars

CACHE_FILES = frequenciesMerged.csv frequenciesDistributionMerged.csv frequencies.json frequenciesDistributionDeepMerged.json chapterProfile.numbers.csv

# Please, read the README.md.
nope:
	@echo Please, read the README.md.

# Run mining scripts
mine:
	export LOGGING
	cd mining; $(MAKE) mine

# Run analytics scripts
analyze:
	export LOGGING
	cd analytics; $(MAKE) analyze

# Copies post processed data from cache
from-cache:
	for b in ${NON_LINKED_BOOKS}; do \
		for f in ${CACHE_FILES}; do \
			cp ../data/perbook/"$$b"/cache/"$$f"  ../data/perbook/"$$b"/ ;\
		done \
	done

# Copies post-processed data, required for analytics, to cache
to-cache:
	for b in ${LINKED_BOOKS}; do \
		for f in $(filter-out %.json, $(CACHE_FILES)); do \
			cp ../data/perbook/"$$b"/"$$f"  ../data/perbook/"$$b"/cache/"$$f" ;\
		done \
	done
	for b in ${LINKED_BOOKS}; do \
		for f in $(filter %.json, $(CACHE_FILES)); do \
			$(PYTHON) misc/reduceJson.py ../data/perbook/"$$b"/"$$f"  ../data/perbook/"$$b"/cache/"$$f" ;\
		done \
	done


#runs integration-scripts
integrate:
	export LOGGING
	cd integration; $(MAKE) integrate

# Run backlinking scripts
backlink:
	export LOGGING
	cd mining; $(MAKE) backlink

# Clean it all
clean:
	cd ../; rm -rf logs/
	cd ../data/allbooks; rm -f *.tex *.csv *.json *.png *.html
	cd ..; for b in ${ALL_BOOKS}; do \
			cd data/perbook/"$$b"; rm -rf contents *.tex *.csv *.json *.png *.html ; \
			cd ../../.. ;\
			rm -rf data/perbook/"$$b"/contents; \
	done
