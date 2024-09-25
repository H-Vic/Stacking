import numpy as np
from scipy.special import gamma


def Levy(dim, beta=1.5):
    sigma = (gamma(1 + beta) * np.sin(np.pi * beta / 2) /
             (gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
    u = np.random.randn(dim) * sigma
    v = np.random.randn(dim)
    step = u / np.abs(v) ** (1 / beta)
    return step


def SpaceBound(position, lb, ub):
    position = np.maximum(position, lb)
    position = np.minimum(position, ub)
    return position


def APO(N, T, lb, ub, dim, fobj):
    lb = np.array(lb)
    ub = np.array(ub)

    PopPos = np.random.rand(N, dim) * (ub - lb) + lb
    PopFit = np.array([fobj(PopPos[i, :]) for i in range(N)])

    BestF = np.inf
    BestX = None

    for i in range(N):
        if PopFit[i] <= BestF:
            BestF = PopFit[i]
            BestX = PopPos[i, :]

    curve = np.zeros(T)

    for It in range(T):
        for i in range(N):
            theta1 = 1 - It / T
            B = 2 * np.log(1 / np.random.rand()) * theta1

            if B > 0.5:
                while True:
                    K = np.delete(np.arange(N), i)
                    RandInd = np.random.choice(K)
                    step1 = PopPos[i, :] - PopPos[RandInd, :]
                    if np.linalg.norm(step1) != 0 and not np.array_equal(PopPos[i, :], PopPos[RandInd, :]):
                        break

                Y = PopPos[i, :] + Levy(dim) * step1 + np.round(0.5 * (0.05 + np.random.rand())) * np.random.randn(dim)

                R = np.random.rand(dim)
                step2 = (R - 0.5) * np.pi
                S = np.tan(step2)
                Z = Y * S

                Y = SpaceBound(Y, lb, ub)
                Z = SpaceBound(Z, lb, ub)
                NewPop = np.array([Y, Z])
                NewPopfit = np.array([fobj(Y), fobj(Z)])
                sorted_indexes = np.argsort(NewPopfit)
                newPopPos = NewPop[sorted_indexes[0], :]

            else:
                F = 0.5
                K = np.delete(np.arange(N), i)
                RandInd = np.random.choice(K, 3, replace=False)
                f = (0.1 * (np.random.rand() - 1) * (T - It)) / T
                while True:
                    RandInd = np.random.choice(K, 3, replace=False)
                    step1 = PopPos[RandInd[1], :] - PopPos[RandInd[2], :]
                    if np.linalg.norm(step1) != 0 and RandInd[1] != RandInd[2]:
                        break

                if np.random.rand() < 0.5:
                    W = PopPos[RandInd[0], :] + F * step1
                else:
                    W = PopPos[RandInd[0], :] + F * Levy(dim) * step1

                Y = (1 + f) * W

                while True:
                    rand_leader_index1 = np.random.randint(0, N)
                    rand_leader_index2 = np.random.randint(0, N)
                    X_rand1 = PopPos[rand_leader_index1, :]
                    X_rand2 = PopPos[rand_leader_index2, :]
                    step2 = X_rand1 - X_rand2
                    if np.linalg.norm(step2) != 0 and not np.array_equal(X_rand1, X_rand2):
                        break

                Epsilon = np.random.uniform(0, 1)
                if np.random.rand() < 0.5:
                    Z = PopPos[i, :] + Epsilon * step2
                else:
                    Z = PopPos[i, :] + F * Levy(dim) * step2

                NewPop = np.array([W, Y, Z])
                NewPopfit = np.array([fobj(W), fobj(Y), fobj(Z)])
                sorted_indexes = np.argsort(NewPopfit)
                newPopPos = NewPop[sorted_indexes[0], :]

            newPopPos = SpaceBound(newPopPos, lb, ub)
            newPopFit = fobj(newPopPos)

            if newPopFit < PopFit[i]:
                PopFit[i] = newPopFit
                PopPos[i, :] = newPopPos

        for i in range(N):
            if PopFit[i] < BestF:
                BestF = PopFit[i]
                BestX = PopPos[i, :]

        curve[It] = BestF

    return BestF, BestX, curve
