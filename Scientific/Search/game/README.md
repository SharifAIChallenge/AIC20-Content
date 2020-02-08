# N-Queen-Genetic-Algorithm
Famous [n-queen problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle)'s [genetic algorithm](https://kushalvyas.github.io/gen_8Q.html) approach to find solution. 

Right now it can solve for N queens in a N x N chessboard. 
You can look into some of the solutions' [screenshots](https://github.com/mehedi-shafi/N-Queen-Genetic-Algorithm/tree/master/screenshots) I've attached. 

The system is made as a module to use in other scripts. If necessary.
So how to run it. 

1. You need to have a __good__ computer. 
   > The better the configuration the faster the program runs with higher number of Queens.
   > For 10 queens it took 19 minutes in my system.
2. Python 3.6 or higher installed.
3. [Pygame](https://www.pygame.org/news) installed.
4. Now download the code.
5. Open a terminal in the directory of the code and run ``python`` to get into python console.
6. Now import the class ``import nq``
7. Instantaite an object of Queen ``e = nq.queen(N , number_of_population_per_generation)``
   > ``N`` for the number of Queens in a N X N board. ``number_of_population_per_generation`` for starting amount of random solution. keep it under for lower ``N`` higher for bigger ``N``
8. Run it ``e.makeitrain()``
9. Wait.
