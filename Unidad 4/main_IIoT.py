from controlador import PlantaController

config_industrial = {
    'temp_max': 1300,       
    'prob_falla': 0.05,     
    'prob_atasco': 0.05,    
}

if __name__ == "__main__":
    app = PlantaController(config_industrial)
    app.iniciar_monitoreo()