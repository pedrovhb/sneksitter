---
file: /home/pedro/Documents/chatgpt_export/Markdown/Equilíbrio de Nash explicado.md
heading_stack: <root> -> 3b82481d-63e5-4d14-a206-7e8f08917ce7 -> System -> bd7032a3-8956-4632-ab9c-a01fcd623200 -> System -> aaa2817f-485e-4029-8bcc-e22795f2b520 -> User -> 0af197a2-2d3e-44db-87ef-f7e1e1bf7689 -> Assistant -> aaa29528-a303-4f0c-919a-a424bd7e415c -> User -> 5374bac8-7a8d-4b7d-a24c-cde59c531c04 -> Assistant
---
# Assistant

Claro, o "Dilema do Prisioneiro" é um exemplo clássico para ilustrar o equilíbrio de Nash. O jogo envolve dois prisioneiros, A e B, que são detidos e interrogados separadamente. Eles têm duas opções: cooperar e não dizer nada (ficar em silêncio) ou trair o outro (confessar).

A matriz de pagamento poderia ser assim (os números representam anos de prisão):

\[
\begin{array}{c|cc}
 & \text{B Silêncio} & \text{B Confessa} \\
\hline
\text{A Silêncio} & -1, -1 & -10, 0 \\
\text{A Confessa} & 0, -10 & -5, -5 \\
\end{array}
\]

No equilíbrio de Nash deste jogo, ambos os jogadores escolhem "Confessar". Isso porque, independentemente da escolha do outro jogador, confessar sempre resulta em uma sentença igual ou menor para o jogador em questão.

- Se B ficar em silêncio, A é melhor confessando (0 anos vs 1 ano).
- Se B confessar, A ainda é melhor confessando (-5 anos vs -10 anos).

E o mesmo vale para o jogador B. Portanto, o perfil de estratégias (Confessa, Confessa) é um equilíbrio de Nash, mesmo que ambos os jogadores estejam pior do que se cooperassem e ficassem em silêncio, o que resultaria em apenas 1 ano de prisão para cada.

---
