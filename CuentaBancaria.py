# creamos la clase cuentabancaria con un saldo inicial
class CuentaBancaria():
    v_NumeroDeCuenta= 123456
    v_Sadlo = 5000

# definimos el metodo depositar sin condiciones
def depositar(var_valor1):
    cuenta=CuentaBancaria()
    cuenta.v_Sadlo+=var_valor1
    print("saldo: ",cuenta.v_Sadlo)

# se define el metodo retirar con la condicino de que si esta en cero
# no habra retiro, pero si no esta en cero restara del saldo  
def retirar(var_valor2):
    cuenta=CuentaBancaria()
    if cuenta.v_Sadlo== 0:
        print("FONDOS INSUFICIENTES")
    elif cuenta.v_Sadlo != 0:
        cuenta.v_Sadlo-=var_valor2
        print("saldo al retirar: ",cuenta.v_Sadlo)

# Instanciamiento de metodos con valores a retirar y depositar
retirar(3000)
depositar(10000)