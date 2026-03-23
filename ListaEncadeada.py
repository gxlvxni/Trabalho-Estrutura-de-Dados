class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, dado):
        novo = No(dado)  

        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def listar(self):
        atual = self.inicio

        if atual is None:
            print("⚠️ Lista vazia.")
            return

        while atual:
            print(atual.dado)
            atual = atual.proximo

    def buscar_por_id(self, id):
        atual = self.inicio

        while atual:
            if atual.dado.id == id:
                return atual.dado
            atual = atual.proximo

        return None

    def buscar_por_nome(self, nome):
        atual = self.inicio

        while atual:
            if atual.dado.nome.lower() == nome.lower():
                return atual.dado
            atual = atual.proximo

        return None


    def calcular_total_estoque(self):
        atual = self.inicio
        total = 0

        while atual:
            produto = atual.dado
            total += produto.quantidade * produto.preco
            atual = atual.proximo

        return total
    

    