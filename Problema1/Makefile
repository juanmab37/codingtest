.PHONY : clean

CXXFLAGS= -ggdb -Wall -Wno-unused-function -Wunused-result -Wno-unused-result -O3  
CPPFLAGS=-lm 

all : P1

clean :
	rm -f *.o
	rm -f *.gch

objects = Problem1.o

P1: $(objects) 
	g++ -o P1 $(objects) $(CPPFLAGS)

%.o: %.cpp $(wildcard *.hpp)
	g++ -c $(CXXFLAGS) $< -o $@
