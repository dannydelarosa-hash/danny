"""
NeonVelocity Racing Simulation
A turn-based racing game where players manage their car's performance across 10 laps.
"""

import random


def display_status(vuelta_actual, vueltas_totales, posicion, salud_neumaticos, salud_motor, combustible):
    """Display current race status"""
    print(f"\n--- VUELTA {vuelta_actual}/{vueltas_totales} ---")
    print(f"Posición: {posicion}  Neumáticos: {salud_neumaticos}%")
    print(f"Motor: {salud_motor}%  Combustible: {combustible}%")


def get_player_action():
    """Get player's action choice"""
    print("\nElige acción: 1.Push, 2.Mantener, 3.Ahorrar, 4.Box")
    while True:
        try:
            decision = int(input("Tu decisión: "))
            if 1 <= decision <= 4:
                return decision
            print("Por favor, elige una opción entre 1 y 4.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entre 1 y 4.")


def apply_action(decision_usuario, posicion, salud_neumaticos, salud_motor, combustible):
    """Apply consequences based on player's decision"""
    if decision_usuario == 1:  # Acelerar a fondo (Push)
        posicion -= 2  # Adelanta
        salud_neumaticos -= 15
        salud_motor -= 10
        combustible -= 12
        print("🏁 ¡PUSH! Aceleraste a fondo.")
    
    elif decision_usuario == 2:  # Mantener ritmo
        salud_neumaticos -= 5
        salud_motor -= 5
        combustible -= 8
        print("⚙️  Mantienes el ritmo...")
    
    elif decision_usuario == 3:  # Ahorrar
        posicion += 1  # Pierde un puesto
        salud_motor += 2  # Se enfría
        combustible -= 4
        print("💨 Ahorras energía pero pierdes un puesto.")
    
    elif decision_usuario == 4:  # Boxes
        posicion = 19  # Cae al fondo
        salud_neumaticos = 100
        salud_motor = 100
        print("🔧 Parada técnica completada.")
    
    return posicion, salud_neumaticos, salud_motor, combustible


def check_random_events(vueltas_totales):
    """Check for random weather events"""
    if random.randint(1, 10) > 8:
        print("⛈️  ¡Alerta! Empieza a llover en Mónaco.")
        return "Lluvia"
    return "Despejado"


def neon_velocity():
    """Main race simulation"""
    # 1. Configuración inicial (Variables)
    vuelta_actual = 1
    vueltas_totales = 10
    posicion = 8
    salud_neumaticos = 100
    salud_motor = 100
    combustible = 100
    clima = "Despejado"
    
    print("=" * 50)
    print("🏎️  BIENVENIDO A NEONVELOCITY")
    print("=" * 50)
    print(f"Salida en posición {posicion}. ¡Que comience la carrera!")
    
    # 2. Main race loop
    while vuelta_actual <= vueltas_totales and salud_motor > 0:
        display_status(vuelta_actual, vueltas_totales, posicion, salud_neumaticos, salud_motor, combustible)
        
        # 3. Entrada de decisión
        decision_usuario = get_player_action()
        
        # 4. Lógica de Consecuencias
        posicion, salud_neumaticos, salud_motor, combustible = apply_action(
            decision_usuario, posicion, salud_neumaticos, salud_motor, combustible
        )
        
        # 5. Eventos Aleatorios
        clima = check_random_events(vueltas_totales)
        
        # 6. Verificar Condición de Derrota
        if salud_neumaticos <= 0 or salud_motor <= 0:
            print("\n❌ ¡DNF! El coche se ha averiado.")
            print(f"Recorriste {vuelta_actual - 1} vueltas antes del desastre.")
            return
        
        vuelta_actual += 1
    
    # 7. Race finished
    print("\n" + "=" * 50)
    print(f"🏁 ¡Bandera a cuadros! Posición final: {posicion}")
    print("=" * 50)
    
    # Final status
    if posicion <= 3:
        print("🥇 ¡Excelente carrera! ¡Estás en el podio!")
    elif posicion <= 10:
        print("✅ ¡Buena carrera! Terminaste en puntos.")
    else:
        print("💪 Vuelve a intentarlo.")


if __name__ == "__main__":
    neon_velocity()
