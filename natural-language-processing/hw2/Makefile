SHELL := /bin/bash

### PATH
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := .:${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}
SEED=1


naive_bayes_scores.txt: nb.py
	for i in 1 2 3 4 5; do nb.py $$i; done > $@

nb_calc_scores: naive_bayes_scores.txt
	cat $< | awk '{sum=sum+$$1}END{print sum / 5}'

