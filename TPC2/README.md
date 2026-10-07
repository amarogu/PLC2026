# TPC2 — Conversor de Markdown para HTML

## Autor

<img src="../photo.png" alt="Fotografia de Gustavo Amaro dos Reis" width="200">

- **Nome:** Gustavo Amaro dos Reis
- **Número:** A109310

## Resumo

Conversor de Markdown para HTML escrito em Python com o módulo `re`. Converte os elementos da "Basic Syntax" pedidos no enunciado:

- Cabeçalhos `#`, `##` e `###` → `<h1>`, `<h2>` e `<h3>`
- Negrito `**texto**` → `<b>texto</b>`
- Itálico `*texto*` → `<i>texto</i>`
- Lista numerada `1. item` → `<ol>` com um `<li>` por item
- Link `[texto](url)` → `<a href="url">texto</a>`
- Imagem `![alt](path)` → `<img src="path" alt="alt"/>`

O texto é processado linha a linha. Os cabeçalhos e os itens de lista são reconhecidos com `fullmatch`, e as linhas seguidas de itens são agrupadas num único `<ol>`. Os elementos inline são substituídos com `sub` e grupos nomeados, por esta ordem: imagens, links, negrito e itálico. As imagens vêm antes dos links porque `![alt](path)` contém a sintaxe de um link, e o negrito vem antes do itálico porque `**` contém `*`. O negrito e o itálico só são reconhecidos quando o texto não começa nem acaba com espaço, para que expressões como `2 * 3 * 4` não sejam convertidas.

Utilização:

```bash
python3 md2html.py exemplo.md exemplo.html
```

Sem o segundo argumento, o HTML é escrito no stdout. Sem argumentos, o Markdown é lido do stdin.

## Resultados

- [md2html.py](md2html.py): o conversor
- [exemplo.md](exemplo.md): ficheiro de teste com os exemplos do enunciado
- [exemplo.html](exemplo.html): resultado da conversão de `exemplo.md`
