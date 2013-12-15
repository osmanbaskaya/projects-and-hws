SHELL := /bin/bash

### PATH
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := ${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}
SEED=1

VALID_POS= "WRB PRP$$ VBG FW CC PDT RBS PRP CD WP$$ VBP VBN EX JJ IN WP VBZ DT MD NNPS RP NN POS RBR VBD JJS JJR SYM VB TO UH LS RB WDT NNS NNP"

%.parsed.gz: wsj/%
	treebank_parser.py $< | gzip > $@

%.tok.gz %.pos.gz: %.parsed.gz
	zcat $< | ./extract.py $*

%.pos-filtered.gz %.tok-filtered.gz: %.tok.gz %.pos.gz
	pos-filter.py $^ ${VALID_POS}

%.vocab.gz: %.tok-filtered.gz
	zcat $< | tr ' ' '\n' | sort | uniq | gzip > $@
	zcat $@ | wc -l

THRESHOLD=2
%.vocab-2.gz: %.tok-filtered.gz
	zcat $< | tr ' ' '\n' | sort | uniq -c  | awk \
	'{if ($$1 >= ${THRESHOLD}) print $$2}' | gzip > $@

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

%.hmm.score: %.hmm.ans %.pos-filtered.gz
	eval-pos-accuracy.py $^

unk.%.hmm.score: unk.%.hmm.ans %-unk.pos-filtered.gz
	eval-pos-accuracy.py $^

mft-baseline.score: mft-baseline.ans test.pos-filtered.gz
	eval-pos-accuracy.py $^

%.word-pos.counts.gz: %.tok-filtered.gz %.pos-filtered.gz
	word-pos-count.py $^ | gzip > $@

%.hmm.ans: train.ngram.gz train.word-pos.counts.gz %.tok-filtered.gz
	hmm.py $^ ${VALID_POS} | gzip > $@

unk.%.hmm.ans: train-unk.ngram.gz train-unk.word-pos.counts.gz %-unk.tok-filtered.gz
	hmm.py $^ ${VALID_POS} | gzip > $@

%-unk.tok-filtered.gz: train.vocab-2.gz %.tok-filtered.gz
	zcat $*.tok-filtered.gz | word-replace.py $< | gzip > $@

%-unk.pos-filtered.gz: %.pos-filtered.gz
	cp $< $@

.SECONDARY:
