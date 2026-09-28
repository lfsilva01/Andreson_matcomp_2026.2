ativos = [
    {"id": "RESP-1", "setor": "UTI", "dias_sem_manutencao": 45, "calibrado": True},
    {"id": "RESP-2", "setor": "UTI", "dias_sem_manutencao": 210, "calibrado": True},
    {"id": "BOMB-1", "setor": "Triagem", "dias_sem_manutencao": 30, "calibrado": False},
    {"id": "MONITOR-1", "setor": "UTI", "dias_sem_manutencao": 100, "calibrado": True},
]

#REQUESITO 1: validação do quantificador universal para conformidade geral de prazos.
conformidade_geral = all(ativo["dias_sem_manutencao"] <= 180 for ativo in ativos)
print("Conformidade geral de prazos:", conformidade_geral)

#REQUESITO 2: : Implementar a verificação de risco de UTI (∃x (UTI(x) ∧ ¬Calibrado(x))).
risco_uti = any(ativo["setor"] == "UTI" and not ativo["calibrado"] for ativo in ativos)
print("Risco de UTI detectado:", risco_uti)

#REQUESITO 3: Extrair declarativamente a lista de IDs de equipamentos pendentes utilizando List Comprehension.
equipamentos_pendentes = [ativo["id"] for ativo in ativos if ativo["dias_sem_manutencao"] > 180]
print("Equipamentos pendentes de manutenção:", equipamentos_pendentes)
