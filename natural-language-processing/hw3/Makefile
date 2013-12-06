SHELL := /bin/bash

### PATH
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := ${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}
SEED=1

VALID_POS="NN NNS VBD IN NNP ."

%.parsed.gz: wsj/%
	treebank_parser.py $< | gzip > $@

%.extract: %.parsed.gz
	zcat $< | ./extract.py $*

%.filter: %.tok.gz %.pos.gz
	pos-filter.py $^ ${VALID_POS}

.SECONDARY:
