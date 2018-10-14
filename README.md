# Tutorial Schematics

## Instalação

```console
$ pip install schematics
```
---

## Exemplos

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Exemplo 1: Validação](#exemplo-1-valida%C3%A7%C3%A3o)
- [Exemplo 2: DataError](#exemplo-2-dataerror)
- [Exemplo 3: Usando dicionários](#exemplo-3-usando-dicion%C3%A1rios)
- [Exemplo 4: DataError usando dicionários](#exemplo-4-dataerror-usando-dicion%C3%A1rios)
- [Exemplo 5: Serializando antes](#exemplo-5-serializando-antes)
- [Exemplo 6: Serializando depois](#exemplo-6-serializando-depois)
- [Exemplo 7: Rogue field](#exemplo-7-rogue-field)
- [Exemplo 8: Deserializando](#exemplo-8-deserializando)
- [Exemplo 9: Reserializando antes](#exemplo-9-reserializando-antes)
- [Exemplo 10: Reserializando depois](#exemplo-10-reserializando-depois)
- [Exemplo 11: Definindo tipos](#exemplo-11-definindo-tipos)
- [Exemplo 12: Pessoa tem cachorrinho](#exemplo-12-pessoa-tem-cachorrinho)
- [Exemplo 13: Cachorrinho](#exemplo-13-cachorrinho)
- [Exemplo 14: Validadores - tipo](#exemplo-14-validadores---tipo)
- [Exemplo 15: Validadores - modelo DataError](#exemplo-15-validadores---modelo-dataerror)
- [Exemplo 16: Validadores - modelo](#exemplo-16-validadores---modelo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

Logo após o título de cada exemplo, eu coloquei também a parte inicial do hash do commit que você pode utilizar para "pular" para a versão dos arquivos de forma mais fácil :wink:

### Exemplo 1: Validação

Commit: 1949e50

```python
from models import Pessoa
jess = Pessoa()
jess.nome = "Jess"
jess.idade = "42"
jess.linguagens = ["Python", "R", "Go"]
jess.validate() == None
```

### Exemplo 2: DataError

Commit: 1949e50

```python
from models import Pessoa
jess = Pessoa()
jess.nome = "Jess"
jess.idade = "4p2"
jess.linguagens = ["Python", "R", "Go"]
jess.validate()
```

### Exemplo 3: Usando dicionários

Commit: 1949e50

```python
from models import Pessoa
data = {
    "idade": "42",
    "nome": "Jess",
    "linguagens": [
        "Python",
        "Go",
        "R"
    ]
}
jess = Pessoa(data)
```

### Exemplo 4: DataError usando dicionários

Commit: 1949e50

```python
from models import Pessoa
data = {
    "idade": "4p2",
    "nome": "Jess",
    "linguagens": ["Python", "R", "Go"]
}
jess = Pessoa(data)
```

### Exemplo 5: Serializando antes

Commit: 1949e50

```python
from models import Pessoa
jess = Pessoa()
jess.nome = "Jess"
jess.to_native()
```

### Exemplo 6: Serializando depois

Commit: 1bf5445

```python
from models import Pessoa
jess = Pessoa()
jess.nome = "Jess"
jess.to_native()
```

### Exemplo 7: Rogue field

Commit: 1bf5445

```python
from models import Pessoa
data = {
    "name": "Jess"
}
jess = Pessoa(data)
```

### Exemplo 8: Deserializando

Commit: 9898782

```python
from models import Pessoa
data = {
    "name": "Jess",
    "age": "42",
    "lang": [
        "Python",
        "Go",
        "R"
    ]
}
jess = Pessoa(data)
```

### Exemplo 9: Reserializando antes

Commit: 9898782

```python
from models import Pessoa
data = {
    "name": "Jess",
    "age": "42",
    "lang": [
        "Python",
        "Go",
        "R"
    ]
}
jess = Pessoa(data)
jess.to_native()
```

### Exemplo 10: Reserializando depois

Commit: 2beeea6

```python
from models import Pessoa
data = {
    "name": "Jess",
    "age": "42",
    "lang": [
        "Python",
        "Go",
        "R"
    ]
}
jess = Pessoa(data)
jess.to_native()
```

### Exemplo 11: Definindo tipos

Commit: ecf3a67

```python
from models import Pessoa
jess = Pessoa()
jess.nome = "Jess"
jess.idade = 4242
jess.validate()
```

### Exemplo 12: Pessoa tem cachorrinho

Commit: 923923a

```python
from models import Pessoa
data = {
    "name": "Jess",
    "age": "42",
    "lang": ["Python", "R", "Go"],
    "pets": [
        {"name": "cora", "fur": "preta"},
        {"name": "channel", "fur": "branca"}
    ]
}
jess = Pessoa(data)
```

### Exemplo 13: Cachorrinho

Commit: 923923a

```python
from models import Cachorrinho
data = {
    "name": "cora",
    "fur": "preta"
}
dog = Cachorrinho(data)
```

### Exemplo 14: Validadores - tipo

Commit: 9c3e573

```python
from models import Pessoa
data = {
    "name": "Jess",
    "lang": ["Java"]
}
jess = Pessoa(data)
jess.validate()
```

### Exemplo 15: Validadores - modelo DataError

Commit: b866fd0

```python
from models import Cachorrinho
data = {
    "name": "cora",
    "fur": "preta"
}
dog = Cachorrinho(data)
dog.validate()
```

### Exemplo 16: Validadores - modelo

Commit: b866fd0

```python
from models import Cachorrinho
data = {
    "name": "Cora",
    "fur": "preta"
}
dog = Cachorrinho(data)
dog.validate()
```
