all:
	gcc -c ./src/float_vector.c -I ./include -o ./obj/float_vector.o
	gcc -c ./src/mytime.c -I ./include -o ./obj/mytime.o

	gcc ./apps/app.c ./obj/*.o -I ./include -o ./bin/app
	gcc ./apps/app_mytime.c ./obj/*.o -I ./include -o ./bin/app_mytime

run:
	./bin/app

clean:
	rm ./bin/* ./obj/*