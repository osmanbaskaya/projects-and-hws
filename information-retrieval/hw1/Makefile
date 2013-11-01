SHELL := /bin/bash

### PATH
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := .:${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}
SEED=1

%.parsed.txt: %.txt
	parse.pl $< > $@

%.freq.txt: %.parsed.txt
	cat $< | sort | uniq -c | sort -nr | grep -Pn "" | sed "s|:||g" > $@

NUM_TOKEN=26693
%.all.txt: %.freq.txt
	cat $< | awk -F' ' '{print $$1"\t"$$2"\t"$$3"\t"$$2/${NUM_TOKEN}"\t"$$2*$$1/${NUM_TOKEN}}'\
	> $@

%-25-most-freq.txt: %.all.txt
	head -25 $< > $@

NUM_UNIQ= `wc -l alice.freq.txt`

%-25-most-freq-starts-with-f.txt: %.all.txt
	tail -n +25 $< | grep -P "\d+\tf\w+" | head -25 > $@

omit-proportion: alice.freq.txt
	cat $< | awk -F' ' '{if ($$2 > 4) print $$0}' | \
	awk -F' ' 'BEGIN{sum=0}{sum=sum+$$2}END{print sum}'

omit-proportion-vocab: alice.freq.txt
	cat $< | awk -F' ' '{if ($$2 > 4) print $$0}' | \
	wc -l

.SECONDARY:
