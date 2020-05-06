
import argparse

from handout import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--framework', choice=['tf', 'pt'], default='pt')
    arg = parser.parse_args()

    if arg.framework == 'pt':
        pt_main(500, 100)
        pt_adv_main(500, 5, 100, 3, "LSTM", 0.01)
    elif arg.framework == 'tf':
        tf_main()
        tf_adv_main()
    else:
        raise RuntimeError
