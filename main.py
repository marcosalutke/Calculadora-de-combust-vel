import tkinter as tk
from tkinter import messagebox, ttk

class CalculadoraCombustivel:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Combustível")
        self.root.geometry("400x500")
        
        # Componente de Abas 
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.aba_viagem = ttk.Frame(self.notebook)
        self.aba_flex = ttk.Frame(self.notebook)
        
        self.notebook.add(self.aba_viagem, text="Viagem")
        self.notebook.add(self.aba_flex, text="Etanol x Gasolina")
        
        self.renderizar_aba_viagem()
        self.renderizar_aba_flex()

    def renderizar_aba_viagem(self):
        frame = ttk.Frame(self.aba_viagem, padding="15")
        frame.pack(fill="both", expand=True)
        
        # Entradas de dados (Inputs)
        ttk.Label(frame, text="Distância (km):").pack(anchor="w", pady=2)
        self.campo_distancia = ttk.Entry(frame, width=20)
        self.campo_distancia.pack(anchor="w", pady=2)
        
        self.var_ida_e_volta = tk.BooleanVar()
        ttk.Checkbutton(frame, text="Calcular Ida e Volta", variable=self.var_ida_e_volta).pack(anchor="w", pady=5)
        
        ttk.Label(frame, text="Consumo Médio (km/l ou l/100km):").pack(anchor="w", pady=2)
        self.campo_consumo = ttk.Entry(frame, width=20)
        self.campo_consumo.pack(anchor="w", pady=2)
        
        self.var_unidade_medida = tk.StringVar(value="km/l")
        ttk.Radiobutton(frame, text="km/l", variable=self.var_unidade_medida, value="km/l").pack(anchor="w")
        ttk.Radiobutton(frame, text="l / 100 km", variable=self.var_unidade_medida, value="l / 100 km").pack(anchor="w")
        
        ttk.Label(frame, text="Preço por Litro (R$):").pack(anchor="w", pady=2)
        self.campo_preco_litro = ttk.Entry(frame, width=20)
        self.campo_preco_litro.pack(anchor="w", pady=2)
        
        ttk.Button(frame, text="Calcular", command=self.calcular_viagem).pack(fill="x", pady=15)
        
        # Área de exibição dos resultados (Output)
        self.label_resultado_viagem = ttk.Label(frame, text="", font=("Arial", 10, "bold"))
        self.label_resultado_viagem.pack(anchor="w", pady=5)

    def calcular_viagem(self):
        try:
            # Coleta e tratamento inicial dos dados
            distancia = float(self.campo_distancia.get().replace(",", "."))
            consumo = float(self.campo_consumo.get().replace(",", "."))
            preco = float(self.campo_preco_litro.get().replace(",", "."))
            
            # Aplicação das regras de negócio
            if self.var_ida_e_volta.get(): 
                distancia *= 2
                
            if self.var_unidade_medida.get() == "l / 100 km": 
                consumo = 100 / consumo
            
            # Cálculos matemáticos da rota
            custo_por_km = preco / consumo
            litros_totais = distancia / consumo
            custo_total = distancia * custo_por_km
            
            # Atualização da interface de texto
            self.label_resultado_viagem.config(
                text=f"Distância Total: {distancia:.1f} km\n"
                     f"Custo por km: R$ {custo_por_km:.2f}\n"
                     f"Total de Litros: {litros_totais:.1f} l\n"
                     f"Total a Gastar: R$ {custo_total:.2f}"
            )
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos com números válidos.")

    def renderizar_aba_flex(self):
        frame = ttk.Frame(self.aba_flex, padding="15")
        frame.pack(fill="both", expand=True)
        
        ttk.Label(frame, text="Preço Etanol (R$):").pack(anchor="w", pady=2)
        self.campo_preco_etanol = ttk.Entry(frame, width=20)
        self.campo_preco_etanol.pack(anchor="w", pady=2)
        
        ttk.Label(frame, text="Preço Gasolina (R$):").pack(anchor="w", pady=2)
        self.campo_preco_gasolina = ttk.Entry(frame, width=20)
        self.campo_preco_gasolina.pack(anchor="w", pady=2)
        
        ttk.Button(frame, text="Verificar Vantagem", command=self.calcular_vantagem_flex).pack(fill="x", pady=15)
        
        self.label_resultado_flex = ttk.Label(frame, text="", font=("Arial", 10, "bold"))
        self.label_resultado_flex.pack(anchor="w", pady=5)

    def calcular_vantagem_flex(self):
        try:
            preco_etanol = float(self.campo_preco_etanol.get().replace(",", "."))
            preco_gasolina = float(self.campo_preco_gasolina.get().replace(",", "."))
            
            proporcao_preco = preco_etanol / preco_gasolina
            melhor_combustivel = "ETANOL" if proporcao_preco <= 0.70 else "GASOLINA"
            
            self.label_resultado_flex.config(
                text=f"Proporção: {proporcao_preco*100:.1f}%\n"
                     f"Melhor escolha: Abasteça com {melhor_combustivel}!"
            )
        except ValueError:
            messagebox.showerror("Erro", "Preencha os preços corretamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCombustivel(root)
    root.mainloop()