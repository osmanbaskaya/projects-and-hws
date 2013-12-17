SHELL := /bin/bash
### PATH
export PATH := .:${PATH}
SEED=1

### Project related files
QUERY_FILE=project-files/desc.51-100.short
STOP_FILE=project-files/stoplist.txt
STEM_FILE=project-files/stem-classes.txt
DOCLIST=project-files/doclist.txt
EVAL_SCP="project-files/trec_eval"
GOLD="project-files/qrels.adhoc.51-100.AP89.txt"

tf-database-%.pkl: ${QUERY_FILE} ${STOP_FILE} ${STEM_FILE}
	-rm -i queries-tf-database-$*.pkl tf-database-$*.pkl ctf-tf-database-$*.pkl
	fetch.py $^ $* 1 $@

qp-query-%: tf-database-%.pkl.qp ctf-tf-database-%.pkl.qp queries-tf-database-%.pkl.qp
	-rm *$*.pkl
	ln -s queries-tf-database-$*.pkl.qp queries-tf-database-$*.pkl
	ln -s tf-database-$*.pkl.qp  tf-database-$*.pkl
	ln -s ctf-tf-database-$*.pkl.qp ctf-tf-database-$*.pkl

r-query-%: tf-database-%.pkl.r ctf-tf-database-%.pkl.r queries-tf-database-%.pkl.r
	-rm *$*.pkl
	ln -s queries-tf-database-$*.pkl.r queries-tf-database-$*.pkl
	ln -s tf-database-$*.pkl.r  tf-database-$*.pkl
	ln -s ctf-tf-database-$*.pkl.r ctf-tf-database-$*.pkl

r-move-original-tf-ctf-query-%:
	mv queries-tf-database-$*.pkl queries-tf-database-$*.pkl.r
	mv tf-database-$*.pkl  tf-database-$*.pkl.r
	mv ctf-tf-database-$*.pkl ctf-tf-database-$*.pkl.r

qp-move-original-tf-ctf-query-%:
	mv queries-tf-database-$*.pkl queries-tf-database-$*.pkl.qp
	mv tf-database-$*.pkl  tf-database-$*.pkl.qp
	mv ctf-tf-database-$*.pkl ctf-tf-database-$*.pkl.qp

robertson-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST}
	tf-based-engine.py $^ robertson_score > $@

okapi-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST}
	tf-based-engine.py $^ okapi_score > $@

vsm-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST}
	tf-based-engine.py $^ vsm > $@

laplace-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST} \
	ctf-tf-database-%.pkl
	lm-based-engine.py $^ laplace_score > $@

jm-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST} \
	ctf-tf-database-%.pkl
	lm-based-engine.py $^ jm_score > $@

bm25-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST} ctf-tf-database-%.pkl
	bm25.py $^ bm25_score > $@

%.score: %.ranking
	${EVAL_SCP} ${GOLD} $< | tee $@

generate.scores:
	for i in 0 1 2 3; do echo vsm-database-$$i.score; done | xargs -n 1 -P 4 make &
	for i in 0 1 2 3; do echo jm-database-$$i.score; done | xargs -n 1 -P 4 make & 
	for i in 0 1 2 3; do echo laplace-database-$$i.score; done | xargs -n 1 -P 4 make &
	for i in 0 1 2 3; do echo okapi-database-$$i.score; done | xargs -n 1 -P 4 make &
	for i in 0 1 2 3; do echo bm25-database-$$i.score; done | xargs -n 1 -P 4 make &
	wait

raw-%.png: r-ans
	cd $<; \
	../plot-score.py $@ "Performance on Dataset$* (No Query Processing)" *-$*.score

qp-%.png: qp-additional-ans
	cd $<; \
	../plot-score.py $@ "Performance on Dataset$* (Query pre-processed)" *-$*.score

# Do not remove intermediate file.
.SECONDARY:
