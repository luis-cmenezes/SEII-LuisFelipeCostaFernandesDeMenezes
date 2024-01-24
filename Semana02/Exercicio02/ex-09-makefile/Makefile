SRC =  ./src
BIN = ./bin
INCLUDE = ./include
APPS = ./apps
OBJ = ./obj

all: libed myapps

libed: float_vector.o mytime.o

%.o: $(SRC)/%.c $(INCLUDE)/%.h
	gcc -c $< -I $(INCLUDE) -o $(OBJ)/$@

myapps: app.c app_mytime.c

%.c: $(APPS)/%.c
	gcc $< $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/$@

run:
	./bin/app

clean:
	rm -rf $(BIN)/* $(OBJ)/*