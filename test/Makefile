

define TESTTEXT
10
1 2 3 4 5 6 7 8 9 10
10
1 1 1 1 1 1 1 1 1 1
10
5 19 5 81 50 28 29 1 83 23
endef

define SHOULDTEXT
10
0 1 2 3 4 5 6 7 8 9
1
7
5
0 1 5 6 8
endef

define INTEXT
10
1 2 3 4 5 6 7 8 9 10
10
1 1 1 1 1 1 1 1 1 1
10
5 19 5 81 50 28 29 1 83 23
endef

export INTEXT
export TESTTEXT
export SHOULDTEXT

tt:
	@echo "---intext:--"
	@echo "$$INTEXT"
	@echo "----end-of-in----"
	@echo "$$TESTTEXT" | ./longincsubseq.py
	@echo "----should-----"
	@echo "$$SHOULDTEXT"
	@echo "-----end-----"

test3:
	@printf "10\n5 19 5 81 50 28 29 1 83 23\n" | ./longincsubseq.py
	@printf "\n"
	@printf "Solution:\n5\n0 1 5 6 8\n"


test2:
	@printf "10\n1 2 3 4 5 6 7 8 9 10\n10\n1 1 1 1 1 1 1 1 1 1\n10\n5 19 5 81 50 28 29 1 83 23\n" | ./longincsubseq.py
	@printf "\n"
	@printf "Solution:\n10\n0 1 2 3 4 5 6 7 8 9\n1\n7\n5\n0 1 5 6 8\n" 

test:
	@printf "7\n0 1 2 3 4 5 6\n" | python3 longincsubseq.py

test1:
	@printf "3\n4 8 12\n" | python3 longincsubseq.py
	@printf "4\n1 2 2 8 3 4\n" | python3 longincsubseq.py
