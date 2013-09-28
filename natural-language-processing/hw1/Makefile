SHELL := /bin/bash
### PATH
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := .:${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}
MATLAB_PATH=/mnt/opt/matlab/linux64/R2011a/bin/matlab -nojvm -nodisplay
SEED=1

#CORP_FILES=$(shell find /data/ldc/gigaword_eng/ -name "*.gz" | sort)

### BIN SETUP
bin:
	cd ../bin; make

%.lm.gz: %.gz
	ngram-count -text $< -lm $@

%.lm-with-unk.gz: %.gz
	ngram-count -text $< -unk -lm $@

# make brown.ppl.gz TEST_FILE=wsj.gz
%.ppl.gz: %.lm.gz ${TEST_FILE}
	ngram -lm $< -ppl ${TEST_FILE} -debug 2

%.ppl-with-unk.gz: %.lm-with-unk.gz ${TEST_FILE}
	ngram -lm $< -ppl ${TEST_FILE} -unk -debug 2

%.vocab.gz: %.gz
	zcat $< | ngram-count -write-order 1 -text - -write - | \
	awk '{if ($$2 >= 2) print $$1}' | gzip > $@

%.lm-with-vocab.gz: %.gz %.vocab.gz
	ngram-count -text $< -vocab $*.vocab.gz -lm $@ 

%.ppl-with-vocab.gz: %.lm-with-vocab.gz ${TEST_FILE}
	ngram -unk -lm $< -ppl ${TEST_FILE}

%.sampling: %.gz
	bootstrap.py -i $< -s ${SEED} | gzip > $*.sampled${SAMPLE_N}.gz

.SECONDARY:
#small.tok.gz small.pos.gz small.lem.gz small.raw.gz
#tok.mono.gz pos.mono.gz lem.mono.gz raw.mono.gz
