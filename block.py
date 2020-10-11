import json
import os


def generate_block(name, amount, to, last_hash=''):
    """Block Generation."""
    blockchain_dir = os.curdir + '/blocks/'

    files = map(int, os.listdir(blockchain_dir))

    data = {'name': name,
            'amount': amount,
            'to': to,
            'hash': last_hash
            }
    with open(blockchain_dir + 'test', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    generate_block()


if __name__ == '__main__':
    main()
