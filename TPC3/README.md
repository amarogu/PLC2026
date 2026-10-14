# TPC3 — Analisador Léxico

## Autor

<img src="../photo.png" alt="Fotografia de Gustavo Amaro dos Reis" width="200">

- **Nome:** Gustavo Amaro dos Reis
- **Número:** A109310

## Resumo

Analisador léxico escrito em Python com o módulo `re` para uma linguagem de query semelhante a SPARQL. Reconhece os tokens pedidos no enunciado:

- `COMMENT`: de `#` até ao fim da linha (é reconhecido e ignorado)
- `VAR`: `?` seguido de alfanuméricos, como `?nome`
- `LANGUAGE`: `@` seguido de 2 carateres, como `@en`
- `STRING`: qualquer sequência entre aspas, como `"Chuck Berry"`
- `NUMBER`: valor numérico, como `1000`
- `RESERVED`: a palavra reservada `LIMIT`
- `CONCEPT`: as outras sequências de alfanuméricos, incluindo prefixos com `:`, como `dbo:MusicalArtist`, `select` ou `a`
- `L_DELIMITER`, `R_DELIMITER` e `DOT`: os delimitadores `{`, `}` e `.`
- `ERROR`: qualquer outro caráter

Todas as expressões regulares são juntas numa única expressão com grupos nomeados, e o texto é percorrido com `finditer`. Cada correspondência é classificada pelo nome do grupo (`lastgroup`). A ordem dos padrões importa. `NUMBER` vem antes de `CONCEPT` porque `\w` também apanha dígitos. `NUMBER` só é aceite quando não é seguido de outro caráter de conceito, para que `12ab` continue a ser um conceito. `ERROR` vem em último lugar para apanhar o que sobra. Os comentários e os espaços em branco são descartados. A palavra reservada é reconhecida como conceito e depois reclassificada com uma consulta ao conjunto `RESERVED`, para que identificadores como `LIMITx` não sejam partidos.

Utilização:

```bash
python3 analisador_lexico.py text.txt
```

Sem argumentos, o texto é lido do stdin.

## Resultados

- [analisador_lexico.py](analisador_lexico.py): o analisador léxico
- [text.txt](text.txt): a query de exemplo do enunciado

Resultado para `text.txt`:

```
('CONCEPT', 'select')
('VAR', '?nome')
('VAR', '?desc')
('CONCEPT', 'where')
('L_DELIMITER', '{')
('VAR', '?s')
('CONCEPT', 'a')
('CONCEPT', 'dbo:MusicalArtist')
('DOT', '.')
('VAR', '?s')
('CONCEPT', 'foaf:name')
('STRING', '"Chuck Berry"')
('LANGUAGE', '@en')
('DOT', '.')
('VAR', '?w')
('CONCEPT', 'dbo:artist')
('VAR', '?s')
('DOT', '.')
('VAR', '?w')
('CONCEPT', 'foaf:name')
('VAR', '?nome')
('DOT', '.')
('VAR', '?w')
('CONCEPT', 'dbo:abstract')
('VAR', '?desc')
('R_DELIMITER', '}')
('RESERVED', 'LIMIT')
('NUMBER', '1000')
```
