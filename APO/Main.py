import numpy as np
import matplotlib.pyplot as plt

import matplotlib

# 设置 Matplotlib 后端
matplotlib.use('TkAgg')  # 或者 'Agg' 等其他后端
# 定义测试函数的详细信息
def functions_details(F_name):
    if F_name == 'F1':
        # Example: Sphere function
        lb = -100
        ub = 100
        D = 30

        def fobj(x):
            return np.sum(x ** 2)

    # 可以添加其他测试函数

    return lb, ub, D, fobj


# A fictitious APO algorithm implementation
def APO(N, T, lb, ub, D, fobj):
    # Initialization
    Positions = np.random.uniform(lb, ub, (N, D))
    Fitness = np.apply_along_axis(fobj, 1, Positions)

    Best_Fitness = np.min(Fitness)
    Best_Pos = Positions[np.argmin(Fitness)]
    Convergence_curve = np.zeros(T)

    for t in range(T):
        # Update the position of search agents
        for i in range(N):
            # This is a placeholder for the actual APO update rules
            new_position = Positions[i] + np.random.uniform(-1, 1, D)
            new_position = np.clip(new_position, lb, ub)
            new_fitness = fobj(new_position)

            if new_fitness < Fitness[i]:
                Positions[i] = new_position
                Fitness[i] = new_fitness

        Best_Fitness = np.min(Fitness)
        Best_Pos = Positions[np.argmin(Fitness)]
        Convergence_curve[t] = Best_Fitness

    return Best_Fitness, Best_Pos, Convergence_curve


# 主程序
N = 30  # Number of search agents
T = 1000  # Maximum number of iterations
F_name = 'F1'  # Name of the test function

lb, ub, D, fobj = functions_details(F_name)  # Load details of the selected benchmark function

Best_Fitness, Best_Pos, Convergence_curve = APO(N, T, lb, ub, D, fobj)

# Display calculation results
print('The best fitness is:', Best_Fitness)
print('The best position is:', Best_Pos)

# 绘制收敛曲线
plt.plot(Convergence_curve)
plt.xlabel('Iteration')
plt.ylabel('Best Fitness')
plt.title('Convergence curve')
plt.show()

