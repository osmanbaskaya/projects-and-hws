SHELL := /bin/bash
### PATH
#SRILM_PATH=/opt/srilm/bin/i686-m64
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
	fetch.py $^ $* 1 $@

p-query-qp-%: tf-database-%.pkl.qp ctf-tf-database-%.pkl.qp queries-tf-database-%.pkl.qp
	rm *$*.pkl
	ln -s queries-tf-database-$*.pkl.qp queries-tf-database-$*.pkl
	ln -s tf-database-$*.pkl.qp  tf-database-$*.pkl
	ln -s ctf-tf-database-$*.pkl.qp ctf-tf-database-$*.pkl

r-query-qp-%: tf-database-%.pkl.r ctf-tf-database-%.pkl.r queries-tf-database-%.pkl.r
	rm *$*.pkl
	ln -s queries-tf-database-$*.pkl.r queries-tf-database-$*.pkl
	ln -s tf-database-$*.pkl.r  tf-database-$*.pkl
	ln -s ctf-tf-database-$*.pkl.r ctf-tf-database-$*.pkl

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
	${EVAL_SCP} ${GOLD} $< #> $@

# Do not remove intermediate file.
.SECONDARY:
