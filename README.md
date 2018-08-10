# eoslive-airdrop

EOS LIVE 空投工具，Based on [bihu-airdrop-tool.py](https://github.com/bihu-id/bihu-tools).

> 环境：Python 2.7.10

EOS LIVE 官方会给每个合格的参与者, 分配一个奖券号，从 1 开始的整数。

EOS LIVE 官方会在空投活动截止时，公布 EOS 未来的某个区块号，比如 10185667。

并使用这个区块的 hash，计算一个 luck number

``` python
luck_num = hash1(hash2(...hash(n)(block.hash)))
```

对每一个奖券号，计算得分 score。

``` python
score ＝ hash(luck_num + 奖券号) ％ base
```

依据得分排序，最高的一等奖，以此等等。

Demo: [https://repl.it/@superoneio/eoslive-airdrop-reward](https://repl.it/@superoneio/eoslive-airdrop-reward)
