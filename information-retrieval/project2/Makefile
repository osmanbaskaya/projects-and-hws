export PATH := .:${PATH}

pagerank: pagerank.cpp
	g++ -std=c++0x pagerank.cpp -o $@ 

scores.txt: pagerank wt2g_inlinks.txt
	$^ 0.85 > $@ 2>epoch.txt

top10-page.txt: scores.txt
	head $< > $@
