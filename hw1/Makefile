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

# make brown.ppl.gz TEST_FILE=wsj.gz
%.ppl.gz: %.lm.gz ${TEST_FILE}
	ngram -lm $< -ppl ${TEST_FILE} -debug 2


.SECONDARY:
#small.tok.gz small.pos.gz small.lem.gz small.raw.gz
#tok.mono.gz pos.mono.gz lem.mono.gz raw.mono.gz
