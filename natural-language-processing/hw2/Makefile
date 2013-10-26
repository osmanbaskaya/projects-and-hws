SHELL := /bin/bash

### PATH
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := .:${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}
SEED=1


naive_bayes_scores.txt: nb.py
	for i in 1 2 3 4 5; do nb.py $$i; done > $@

nb_calc_scores: naive_bayes_scores.txt
	cat $< | awk '{sum=sum+$$1}END{print sum / 5}'

train.pos.corpus%.txt: train.sample%.txt
	lm-data-prep.py train $* p > $@

train.neg.corpus%.txt: train.sample%.txt
	lm-data-prep.py train $* n > $@

test.corpus%.txt: train.sample%.txt
	lm-data-prep.py test $* n > $@
	lm-data-prep.py test $* p >> $@

LM_VOCAB=2
LM_NGRAM=3
train.vocab-all.gz:
	cat reviews/neg/* reviews/pos/* |\
	ngram-count -write-order 1 -text - -write - | gzip > $@

train.vocab.gz: train.vocab-all.gz
	zcat $< | awk '{if ($$2 >= ${LM_VOCAB}) print $$1}' | gzip > $@
	zcat $@ | wc -l

train.pos.lm%.gz: train.sample%.txt train.vocab.gz
	cat $< | awk '{if ($$2 == "p") print $$1 }' | xargs -n 1 cat | cat |\
	ngram-count -order ${LM_NGRAM} -kndiscount -interpolate -unk -vocab train.vocab.gz -text - -lm $@

train.neg.lm%.gz: train.sample%.txt train.vocab.gz
	cat $< | awk '{if ($$2 == "n") print $$1 }' | xargs -n 1 cat | cat |\
	ngram-count -order ${LM_NGRAM} -kndiscount -interpolate -unk -vocab train.vocab.gz -text - -lm $@

sample%.pos.txt: test.sample%.txt
	for i in `cat test.sample$*.txt | cut -f1`; do cat $$i |\
		ngram -unk -order 3 -lm train.pos.lm$*.gz -ppl - | tail -1 | awk '{print $$4}'; done > $@

sample%.neg.txt: test.sample%.txt
	for i in `cat test.sample$*.txt | cut -f1`; do cat $$i |\
		ngram -unk -order 3 -lm train.neg.lm$*.gz -ppl - | tail -1 | awk '{print $$4}'; done > $@

lm.sample%: 
	lm-based.py <(cat train.sample$*.txt | cut -f2) sample$*.pos.txt \
		sample$*.neg.txt <(cat test.sample$*.txt | cut -f2)

lm.sample.scores:
	for i in 1 2 3 4 5; do make lm.sample$$i; done > $@


