SHELL := /bin/bash

### PATH
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := ${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}
SEED=1

VALID_POS="NN NNS VBD IN NNP ."

%.parsed.gz: wsj/%
	treebank_parser.py $< | gzip > $@

%.tok.gz %.pos.gz: %.parsed.gz
	zcat $< | ./extract.py $*

%.pos-filtered.gz %.tok-filtered.gz: %.tok.gz %.pos.gz
	pos-filter.py $^ ${VALID_POS}

%.vocab.gz: %.tok-filtered.gz
	zcat $< | tr ' ' '\n' | sort | uniq | gzip > $@
	zcat $@ | wc -l

%.unknown.word: %.vocab.gz train.vocab.gz %.tok-filtered.gz
	tokens-count.py $^

%.lm.gz: %.pos-filtered.gz
	ngram-count -text $< -lm $@

%.ngram.gz: %.pos-filtered.gz
	ngram-count -text $< | gzip > $@

%.mft.gz: %.tok-filtered.gz %.pos-filtered.gz
	find-most-freq-tags.py $^ | gzip > $@

mft-baseline.ans: train.mft.gz test.tok-filtered.gz
	mft-baseline.py $^ | gzip > $@

mft-baseline.score: mft-baseline.ans test.pos-filtered.gz
	eval-pos-accuracy.py $^

.SECONDARY:
