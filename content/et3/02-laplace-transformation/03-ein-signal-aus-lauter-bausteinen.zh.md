---
title: 第 2 阶段：完全由基本分量构成的信号
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220300
summary: 第 1 阶段的结论适用于单个基本分量。只有当每个信号都能由基本分量 e pt 构成时，它才真正有用。本阶段说明这确实可行、权重叫什么，以及其局限在哪里。
tags: 绝对可积, 傅里叶表示, 频谱
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
第 [1](warum-gerade.html#stufe-1) 阶段的结论适用于单个基本分量。只有当每个信号都能由基本分量 $\mathrm{e}^{pt}$ 构成时，它才真正有用。本阶段说明这确实可行、权重叫什么，以及其局限在哪里。
:::

### 出发点 $\sigma=0$：纯振荡

<span class="anker" id="stufe-2-1"></span>

在虚轴上（$\sigma=0$），基本分量是纯振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$。__绝对可积__的信号（$\int|s(t)|\,\mathrm{d} t<\infty$，即在两侧都衰减得足够快）可以由它们构成。这就是__傅里叶表示__。这里只需要它的公式。函数 $\mathcal{F}\{s\}(f)$ 称为__频谱__，它给出频率为 $f$ 的振荡的权重：

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

对于系统理论中的许多信号，这还不够。阶跃 $\varepsilon(t)$ 不衰减，而 $\mathrm{e}^{2t}\varepsilon(t)$（一个不稳定系统的冲激响应）甚至会增长。无界增长的信号无法由恒定幅度的振荡构成。
