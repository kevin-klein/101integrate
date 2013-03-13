BOOKS = LYAH RWH Craft PIH

analyze:
	make frequencies
	make popular
	make move

prepare:
	R < dependencies.R --no-save

frequencies:	
	for b in ${BOOKS}; do \
		R < frequencies.R --no-save --args ""$$b""; \
	done

popular:	
	R < buildPopularTermsTable.R --no-save
	R < buildPopularScatteredTermsTable.R --no-save
	R < rank.R --no-save
	#python fixtable.py 

move:
	sed -i '' '3,10d' Craft/Craft.numbers
	sed -i '' '58,65d' Craft/Craft.numbers
	sed -i '' '3,10d' Craft/Craft.visual
	sed -i '' '58,65d' Craft/Craft.visual
	mv Craft/Craft.numbers ../../data/perbook/Craft/chapterProfile.numbers.tex
	mv Craft/Craft.visual ../../data/perbook/Craft/chapterProfile.visual.tex

	sed -i '' '3,10d' LYAH/LYAH.numbers
	sed -i '' '41,48d' LYAH/LYAH.numbers
	sed -i '' '3,10d' LYAH/LYAH.visual
	sed -i '' '41,48d' LYAH/LYAH.visual
	mv LYAH/LYAH.numbers ../../data/perbook/LYAH/chapterProfile.numbers.tex
	mv LYAH/LYAH.visual ../../data/perbook/LYAH/chapterProfile.visual.tex

	sed -i '' '3,10d' PIH/PIH.numbers
	sed -i '' '35,42d' PIH/PIH.numbers
	sed -i '' '3,10d' PIH/PIH.visual
	sed -i '' '35,42d' PIH/PIH.visual
	mv PIH/PIH.numbers ../../data/perbook/PIH/chapterProfile.numbers.tex
	mv PIH/PIH.visual ../../data/perbook/PIH/chapterProfile.visual.tex

	#sh cuttable.sh RWH/RWH.numbers
	#sh cuttable.sh RWH/RWH.visual
	#sed -i '' '3,10d' RWH/RWH.numbers
	#sed -i '' '75,82d' RWH/RWH.numbers
	#sed -i '' '3,10d' RWH/RWH.visual
	#sed -i '' '75,82d' RWH/RWH.visual
	mv RWH/RWH.numbers ../../data/perbook/RWH/chapterProfile.numbers.tex
	mv RWH/RWH.visual ../../data/perbook/RWH/chapterProfile.visual.tex

	sed -i '' '3,6d' Craft/topFrequency.tex 
	sed -i '' '39,44d' Craft/topFrequency.tex 
	mv Craft/topFrequency.tex ../../data/perbook/Craft/topFrequency.tex

	sed -i '' '3,6d' LYAH/topFrequency.tex 
	sed -i '' '39,44d' LYAH/topFrequency.tex 
	mv LYAH/topFrequency.tex ../../data/perbook/LYAH/topFrequency.tex

	sed -i '' '3,6d' RWH/topFrequency.tex 
	sed -i '' '39,44d' RWH/topFrequency.tex 
	mv RWH/topFrequency.tex ../../data/perbook/RWH/topFrequency.tex

	sed -i '' '3,6d' PIH/topFrequency.tex 
	sed -i '' '39,44d' PIH/topFrequency.tex 
	mv PIH/topFrequency.tex ../../data/perbook/PIH/topFrequency.tex

	#sh cuttable.sh RWH/topScattered.tex
	mv RWH/topScattered.tex ../../data/perbook/RWH/topScattered.tex
	#sh cuttable.sh LYAH/topScattered.tex
	mv LYAH/topScattered.tex ../../data/perbook/LYAH/topScattered.tex
	#sh cuttable.sh Craft/topScattered.tex
	mv Craft/topScattered.tex ../../data/perbook/Craft/topScattered.tex
	#sh cuttable.sh PIH/topScattered.tex
	mv PIH/topScattered.tex ../../data/perbook/PIH/topScattered.tex

	mv unionTopFrequencies.tex ../../data/allbooks/
	mv unionTopFrequencies.csv ../../data/allbooks/
	mv unionTopFrequenciesVisual.tex ../../data/allbooks/
	mv unionTopScatterness.tex ../../data/allbooks/
	mv unionTopScatterness.csv ../../data/allbooks/
	mv unionTopScatternessVisual.tex ../../data/allbooks/
	mv ranks.tex ../../data/allbooks/	

clean:
	rm -f *.tex
	rm -f *.html