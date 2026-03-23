import csv

# ================= CLIENTES =================

def salvar_clientes(clientes):
    with open("clientes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        atual = clientes.inicio

        while atual:
            c = atual.dado
            writer.writerow([c.id, c.nome])
            atual = atual.proximo


def carregar_clientes(clientes):
    try:
        with open("clientes.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for linha in reader:
                id, nome = linha
                clientes.inserir(__import__("cliente").Cliente(int(id), nome))
    except FileNotFoundError:
        pass


# ================= PRODUTOS =================

def salvar_produtos(produtos):
    with open("produtos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        atual = produtos.inicio

        while atual:
            p = atual.dado
            writer.writerow([p.id, p.nome, p.quantidade, p.preco])
            atual = atual.proximo


def carregar_produtos(produtos):
    try:
        with open("produtos.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for linha in reader:
                id, nome, qtd, preco = linha
                produtos.inserir(__import__("produto").Produto(int(id), nome, int(qtd), float(preco)))
    except FileNotFoundError:
        pass


# ================= VENDAS =================

def salvar_vendas(fila):
    with open("vendas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for v in fila.itens:
            writer.writerow([v.id, v.cliente.id, v.produto.id, v.quantidade, v.valor_total])