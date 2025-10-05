# bandit_thompson_vs_eps.py
# Requisitos: numpy, pandas, matplotlib
# Ejecuta: python bandit_thompson_vs_eps.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---------- Config ----------
RNG_SEED = 123
K = 5                                              # número de ítems/brazos
TRUE_CTR = np.array([0.03, 0.06, 0.04, 0.055, 0.025])  # CTRs reales (ocultos)
T = 5000                                           # rondas
EPS = 0.1                                          # epsilon de ε-Greedy
OUTDIR = Path("./out_bandit")
OUTDIR.mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(RNG_SEED)
best_arm = int(np.argmax(TRUE_CTR))

# ---------- Algoritmos ----------
def run_thompson(true_ctr, T, rng):
    K = len(true_ctr)
    alpha = np.ones(K)  # Beta(1,1) sin conocimiento previo
    beta = np.ones(K)

    picks = np.empty(T, dtype=int)
    rewards = np.empty(T, dtype=int)
    cum_regret = np.empty(T, dtype=float)
    cum_opt = np.empty(T, dtype=int)

    reg = 0.0
    opt = 0
    for t in range(T):
        sampled = rng.beta(alpha, beta)   # muestreo de posterior
        a = int(np.argmax(sampled))       # acción con mayor muestra
        r = int(rng.random() < true_ctr[a])  # recompensa Bernoulli

        # actualizar posterior
        alpha[a] += r
        beta[a]  += (1 - r)

        reg += (true_ctr.max() - true_ctr[a])
        opt += (a == best_arm)

        picks[t] = a
        rewards[t] = r
        cum_regret[t] = reg
        cum_opt[t] = opt

    return picks, rewards, cum_regret, cum_opt

def run_eps_greedy(true_ctr, T, eps, rng):
    K = len(true_ctr)
    pulls = np.zeros(K, dtype=int)
    success = np.zeros(K, dtype=int)

    picks = np.empty(T, dtype=int)
    rewards = np.empty(T, dtype=int)
    cum_regret = np.empty(T, dtype=float)
    cum_opt = np.empty(T, dtype=int)

    reg = 0.0
    opt = 0
    for t in range(T):
        if rng.random() < eps:
            a = int(rng.integers(0, K))  # explorar
        else:
            est = np.divide(success, np.maximum(pulls, 1))  # explotar
            a = int(np.argmax(est))

        r = int(rng.random() < true_ctr[a])
        pulls[a] += 1
        success[a] += r

        reg += (true_ctr.max() - true_ctr[a])
        opt += (a == best_arm)

        picks[t] = a
        rewards[t] = r
        cum_regret[t] = reg
        cum_opt[t] = opt

    return picks, rewards, cum_regret, cum_opt

# ---------- Correr experimentos ----------
ts_pick, ts_r, ts_regret, ts_opt = run_thompson(TRUE_CTR, T, rng)
eg_pick, eg_r, eg_regret, eg_opt = run_eps_greedy(TRUE_CTR, T, EPS, rng)

# ---------- Tablas ----------
def build_summary(name, picks, rewards):
    K = len(TRUE_CTR)
    times = np.array([(picks == i).sum() for i in range(K)])
    clicks = np.array([rewards[picks == i].sum() for i in range(K)])
    est_ctr = np.divide(clicks, np.maximum(times, 1))
    return pd.DataFrame({
        "Arm": [f"Item {i}" for i in range(K)],
        "True CTR": TRUE_CTR,
        "Times Shown": times,
        "Clicks": clicks,
        "Estimated CTR": est_ctr,
        "Algorithm": name
    })

ts_sum = build_summary("Thompson", ts_pick, ts_r)
eg_sum = build_summary(f"ε-Greedy (ε={EPS})", eg_pick, eg_r)
summary = pd.concat([ts_sum, eg_sum], ignore_index=True)

summary_path = OUTDIR / "bandit_comparison_summary.csv"
summary.to_csv(summary_path, index=False)

agg_path = OUTDIR / "bandit_regret.csv"
pd.DataFrame({
    "round": np.arange(1, T+1),
    "thompson_regret": ts_regret,
    "eps_greedy_regret": eg_regret,
    "thompson_opt_pick_rate": ts_opt / np.arange(1, T+1),
    "eps_greedy_opt_pick_rate": eg_opt / np.arange(1, T+1)
}).to_csv(agg_path, index=False)

print(f"Guardado resumen: {summary_path}")
print(f"Guardado series:  {agg_path}")

# ---------- Plots ----------
# 1) Regret acumulado
plt.figure(figsize=(7, 4))
plt.plot(ts_regret, label="Thompson Sampling")
plt.plot(eg_regret, label=f"ε-Greedy (ε={EPS})")
plt.title("Cumulative Regret")
plt.xlabel("Round")
plt.ylabel("Regret")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig(OUTDIR / "regret.png", dpi=140)
plt.show()

# 2) Tasa de elección del óptimo
plt.figure(figsize=(7, 4))
plt.plot(ts_opt / np.arange(1, T+1), label="Thompson Sampling")
plt.plot(eg_opt / np.arange(1, T+1), label=f"ε-Greedy (ε={EPS})")
plt.title("Fraction of times the optimal item is picked")
plt.xlabel("Round")
plt.ylabel("Optimal-pick rate")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig(OUTDIR / "optimal_pick_rate.png", dpi=140)
plt.show()

# 3) Asignaciones por algoritmo
def bar_counts(picks, title, fname):
    counts = pd.Series(picks).value_counts().sort_index()
    plt.figure(figsize=(6, 4))
    plt.bar([f"Item {i}" for i in range(K)], counts.values)
    plt.title(title)
    plt.xlabel("Item")
    plt.ylabel("Shows")
    plt.tight_layout()
    plt.savefig(OUTDIR / fname, dpi=140)
    plt.show()

bar_counts(ts_pick, "Thompson – Times each item was shown", "alloc_thompson.png")
bar_counts(eg_pick, f"ε-Greedy (ε={EPS}) – Times each item was shown", "alloc_eps_greedy.png")