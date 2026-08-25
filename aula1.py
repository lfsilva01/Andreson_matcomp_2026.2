# Dados simulados do UrbanInventory
equipamentos = [
    {"tombamento": "TOMB-901", "ativo": "Notebook", "secretaria": "Educacao"},
    {"tombamento": "TOMB-902", "ativo": "Projetor", "secretaria": "Saude"}
]
bairros = ["Centro", "Boa Vista"]

print("=== TAREFA 1: PRODUTO CARTESIANO (A x B) ===")
# Produto cartesiano combinando cada equipamento com cada bairro
A_x_B = [(e["ativo"], b) for e in equipamentos for b in bairros]
print("A x B:", A_x_B)


print("\n=== TAREFA 2: FUNÇÃO f(Ativo) -> Secretaria ===")
def f(ativo):
    for e in equipamentos:
        if e["ativo"] == ativo:
            return e["secretaria"]
    return None

# Imagem da função
imagem_f = {f(e["ativo"]) for e in equipamentos}
print("Imagem Im(f):", imagem_f)


print("\n=== TAREFA 3: FUNÇÃO INVERSA f⁻¹(Tombamento) e BIJETIVIDADE ===")
def f_inversa(tombamento):
    for e in equipamentos:
        if e["tombamento"] == tombamento:
            return e["ativo"]
    return "Não encontrado"

print("Inversa de TOMB-901:", f_inversa("TOMB-901"))
print("Bijetividade: Garantida pois há correspondência 1 para 1 entre Ativo e Tombamento.")


print("\n=== TAREFA 4: PIPELINE (g ∘ f) E ROBUSTEZ ===")
def g(secretaria):
    setores = {"Educacao": "Almoxarifado Norte", "Saude": "Almoxarifado Sul"}
    return setores.get(secretaria)

def pipeline(tombamento):
    # 1. Aplica inversa para achar o ativo
    ativo = f_inversa(tombamento)
    if ativo == "Não encontrado":
        return f"Erro: Tombamento {tombamento} inexistente!"
    
    # 2. Aplica f para achar a secretaria
    sec = f(ativo)
    
    # 3. Aplica g para achar o almoxarifado
    return g(sec)

# Testando com TOMB-901 (válido) e TOMB-999 (inexistente para testar robustez)
print("Pipeline para TOMB-901:", pipeline("TOMB-901"))
print("Pipeline para TOMB-999 (Inexistente):", pipeline("TOMB-999"))