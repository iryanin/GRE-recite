# GRE-recite
GRE 要你命3K 背单词小程序

## Usage

```bash
./recite.py [-h] [-a A] [-b B] [-f FILE] [-o WRONG]
```

```
optional arguments:
  -h, --help  show this help message and exit
  -a A        begin
  -b B        end
  -f FILE     word file
  -o WRONG    wrong answer output
```

总共3041个单词，比如某天想背list16的100个单词，并且将不熟悉的单词导出到16.csv中：

```
./recite.py -a 1500 -b 1600 -f all.csv -o 16.csv
```

然后接着复习这些错的单词：

```
./recite.py -f 16.csv
```
