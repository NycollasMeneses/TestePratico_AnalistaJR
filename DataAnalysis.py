import pandas as pd

df = pd.read_csv("vendas.csv")

# faturamento total por produto
df["faturamento"] = df["quantidade"] * df["preco_unitario"]
faturamento_por_produto = df.groupby("produto")["faturamento"].sum()

# Encontrar maior e menor faturamento
produto_mais_vendido = faturamento_por_produto.idxmax()
produto_menos_vendido = faturamento_por_produto.idxmin()

print("Faturamento total por produto:")
print(faturamento_por_produto)

print(f"\nProduto com maior faturamento: {produto_mais_vendido} - R$ {faturamento_por_produto.max():.2f}")
print(f"Produto com menor faturamento: {produto_menos_vendido} - R$ {faturamento_por_produto.min():.2f}")
