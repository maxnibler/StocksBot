EXEC = main.py
PYTHON = python3
TESTPATH = ../test/
DBPATH = ../db/
LOG = logfile.txt

run: 
	${PYTHON} ${EXEC}

test:
	${PYTHON} ${TESTPATH}runtests.py

clearLog:
	rm ${DBPATH}${LOG}

outLog:
	cat ${DBPATH}${LOG}