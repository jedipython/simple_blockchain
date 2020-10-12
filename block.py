import json
import os
import hashlib

blockchain_dir = os.curdir + '/blocks/'


def get_hash(file_name: str):
    file = open(blockchain_dir + file_name, 'rb').read()
    return hashlib.md5(file).hexdigest()


def get_blocks():
    """Return sorted block numbers."""
    return sorted([int(_) for _ in os.listdir(blockchain_dir)])


def check_integrity():
    """Checks the integrity of blocks."""
    blocks = get_blocks()
    results = []
    for block in blocks[1:]:
        hash_ = json.load(open(blockchain_dir + str(block)))['hash']
        prev_block = str(block - 1)
        actual_block_hash = get_hash(prev_block)
        if hash_ == actual_block_hash:
            res = 'Ok'
        else:
            res = 'Modified'
        results.append({'block': prev_block, 'result': res})
    return results


def generate_block(name, amount, to, last_hash=''):
    """Block Generation."""
    last_block = get_blocks()[-1]
    block_name = str(last_block + 1)
    last_hash = get_hash(str(last_block))
    data = {'from': name,
            'amount': amount,
            'to': to,
            'hash': last_hash
            }
    with open(blockchain_dir + block_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
