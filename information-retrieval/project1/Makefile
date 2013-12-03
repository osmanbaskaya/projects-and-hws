SHELL := /bin/bash
### PATH
#SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := .:${PATH}
SEED=1

### Project related files
QUERY_FILE=project-files/desc.51-100.short
STOP_FILE=project-files/stoplist.txt
STEM_FILE=project-files/stem-classes.txt

tf-database-%.pkl: ${QUERY_FILE} ${STOP_FILE}
	fetch.py $^ $* 1
