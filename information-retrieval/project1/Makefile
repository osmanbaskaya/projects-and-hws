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

robertson-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST}
	search_engine.py $^ robertson_score > $@

okapi-database-%.ranking: tf-database-%.pkl queries-tf-database-%.pkl ${DOCLIST}
	search_engine.py $^ okapi_score > $@

%.score: %.ranking
	${EVAL_SCP} $< ${GOLD} #> $@

# Do not remove intermediate file.
.SECONDARY:
