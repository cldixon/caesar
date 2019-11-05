# Caesar Cypher

### Fun tool for learning about the Caesar Cypher.

![Julius Caesar](https://github.com/cldixon/caesar_cypher/blob/master/src/julius_image.svg)

## Python Module
```python
from cypher import Caesar 

caesar = Caesar()
shift = 5
message = 'veni, vidi, vici'

output = caesar.cypher(message, shift)
print(output)
```

## Command-line Usage
```
# cypher message
python caesar.py -cypher -shift 5 -message "veni, vidi, vici"
```

```
# decypher message
python caesar.py -decypher -shift 5 -message "alkjdfk kaj ieur"
```