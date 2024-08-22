import classes
carrinho = classes.CarrinhoDeCompras()
p1 = classes.Produto('Camiseta',50)
p2 = classes.Produto('Copo',10)
p3 = classes.Produto('Bola',35)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produto()
print(carrinho.soma_total())
