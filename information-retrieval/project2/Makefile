export PATH := .:${PATH}

scores.txt: pagerank wt2g_inlinks.txt
	$^ 0.85 > $@ 2>epoch.txt

pagerank: pagerank.cpp
	g++ -std=c++0x pagerank.cpp -o $@ 

top10-page.txt: scores.txt
	head $< > $@
