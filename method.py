# ----------------------------------------Основной класс расчетного блока-----------------------------------------------
class Method_Pack():
    # ------------------------------Функция инициализации поступающих в класс данных------------------------------------
    def __init__(self, num):
        self.num = num
        self.a = self.num[0]
        self.b = self.num[1]
        self.c = self.num[2]
        self.diap = self.num[3]
        self.N = self.num[4]

    # --------------------------------------Функция левых прямоугольников-----------------------------------------------
    def LP(self):
        delta_x = (self.diap[1] - self.diap[0]) / self.N
        integral_sum = 0

        for i in range(self.N):
            x_left = self.diap[0] + i * delta_x
            x_right = x_left + delta_x

            x_mid = (x_left + x_right) / 2
            f_mid = self.a * x_mid ** 2 + self.b * x_mid + self.c

            integral_sum += f_mid

        integral_value_lp = delta_x * integral_sum
        return integral_value_lp

    # ---------------------------------------------Функция Симпсона-----------------------------------------------------
    def SP(self):
        delta_x = (self.diap[1] - self.diap[0]) / self.N

        x_values = [self.diap[0] + i * delta_x for i in range(self.N + 1)]
        f_values = [self.a * x ** 2 + self.b * x + self.c for x in x_values]

        integral_sum = f_values[0] + f_values[self.N]

        for i in range(1, self.N, 2):
            integral_sum += 4 * f_values[i]

        for i in range(2, self.N - 1, 2):
            integral_sum += 2 * f_values[i]

        integral_value_sp = (delta_x / 3) * integral_sum
        return integral_value_sp


proverka = [1, 2, 2, [-5, 5], 10]
print("Метод левых прямоугольников:",Method_Pack(proverka).LP())
print("Метод трапеций:",Method_Pack(proverka).SP())