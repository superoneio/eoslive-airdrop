#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
from collections import OrderedDict

airdrop_prefix = 'LIVE'
# block
block = "4799110853e7f7ab19df8684850c63a13b7b2eb0c09369af590f8294ba1286c9"
# block hash
block_hash = bytearray.fromhex(block)
# total lottery num
total_lottery = 100

def lucky_num_from_block_hash(h):
    hash_names = ['md5', 'md4', 'whirlpool', 'RIPEMD160', 'DSA', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    print(str(len(hash_names)) + ": " + str(hash_names))

    repeat = 10000 * 400 * 20
    # repeat = 10000 * 400
    r = h
    for i in range(repeat):
        if i % 100000 == 0:
            print(str(i) + ":...")
        for n in hash_names:
            h = hashlib.new(n)
            h.update(r)
            r = h.digest()

    return r

def score_for_each_lottery(lucky_num, lottery_id):
    # print(result_hash.hex())
    h = hashlib.sha256()
    h.update(lucky_num)
    h.update(bytes(lottery_id))

    base = 10**11
    score = int(h.hexdigest(), 16) % base
    return score

def compute_airdrop_reward():
    r = {}
    lucky_num = lucky_num_from_block_hash(block_hash)

    for lottery_id in range(1, total_lottery + 1):
        s = score_for_each_lottery(lucky_num, lottery_id)
        r[lottery_id] = s
    return r

def lottery_format(n):
    return airdrop_prefix + '-' + str(n).zfill(7)

def dump_rewards_to_file(rewards):
    c = 1
    f = open('rewards.txt', 'w')
    for r in rewards:
        f.write(str(c) + ',' + lottery_format(r) + ',' + str(rewards[r]) + '\n')
        c += 1

    f.close()

def print_rewards(rewards):
    c = 1
    for item in rewards:
        print(str(c) + ',' + lottery_format(item) + ',' + str(rewards[item]))
        c += 1

# Main
if __name__ == '__main__':
    reward_map = compute_airdrop_reward()
    reward_sorted = OrderedDict(sorted(reward_map.items(), key=lambda t: t[1], reverse = True))
    print("=======================Rewards================================")

    dump_rewards_to_file(reward_sorted)
    print_rewards(reward_sorted)