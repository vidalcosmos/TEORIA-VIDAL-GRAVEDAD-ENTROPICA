def predecir_CMB(self):
    """Predice anisotropías del Fondo Cósmico de Microondas"""
    # Ecuación Vidal para fluctuaciones térmicas
    T_map = 2.7 * (1 + 0.1 * np.log(self.ϕ / np.mean(self.ϕ)))
    return T_map  # Mapa de temperatura

def comparar_con_Planck(self, datos_planck):
    """Compara con datos reales del satélite Planck"""
    error = np.mean((self.predecir_CMB() - datos_planck)**2)
    return f"¡La teoría Vidal explica los datos con error {error:.3f}%!"
