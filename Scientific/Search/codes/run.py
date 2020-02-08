from search import search
from driver import *

from IPython.display import display_html
def restartkernel() :
    display_html("<script>Jupyter.notebook.kernel.restart()</script>",raw=True)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('board')
    args = parser.parse_args()

    read(args.board)

    frontier = search(initial_state)
		
    export(frontier)
    restartkernel()


function_map = {
    'bfs': bfs,
    'dfs': dfs,
    'ast': ast,
    'ida': ida
}

if __name__ == '__main__':
    main()
