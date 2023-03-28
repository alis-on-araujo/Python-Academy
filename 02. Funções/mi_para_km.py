# função para converter milhas para km

def converte_milhas_para_km(distancia_mi):
    distancia_km = 1.60934 * distancia_mi
    return distancia_km

# quanto é 10 milhas em km?
milhas = 10
km = converte_milhas_para_km(milhas)
print(km)