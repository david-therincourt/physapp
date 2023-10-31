# Filtres

## Ordre 1 - Passe bas

Transmittance complexe :

$$
\underline{T} = T_0\times\dfrac{1}{1+{\rm j}\dfrac{f}{f_0}}
$$

Transmittance :

$$
T = T_0\times\dfrac{1}{\sqrt{1+(\dfrac{f}{f_0})^2}}
$$

Gain :

$$
G = G_0- 20\log(\sqrt{1+(\dfrac{f}{f_0})^2}
$$

Phase :

$$
\varphi = -\arctan(\dfrac{f}{f_0})
$$

## Ordre 2 - Passe haut

Transmittance complexe :

$$
\boxed{\underline{T} = T_0\times\dfrac{{\rm j}\dfrac{f}{f_0}}{1+{\rm j}\dfrac{f}{f_0}}}
$$

Transmittance

$$
T = T_0\times\dfrac{\dfrac{f}{f_0}}{\sqrt{1+(\dfrac{f}{f_0})^2}}
$$

Gain :

$$
G = G_0 + 20\log(\dfrac{f}{f_0})- 20\log(\sqrt{1+(\dfrac{f}{f_0})^2})
$$

Phase :

$$
\varphi = 90 -\arctan(\dfrac{f}{f_0})
$$

---

## Ordre 2 - Passe bas

Transmittance complexe :

$$
\underline{T}
= T_0\times\dfrac{1}{1+2m{\rm j}\dfrac{f}{f_0}+({\rm j}\dfrac{f}{f_0})^2}
\quad\implies\quad
\underline{T}
= T_0\times\dfrac{1}{[1-\dfrac{f^2}{f_0^2}]+{\rm j}[2m\dfrac{f}{f_0}]}
$$

Transmittance :

$$
T = T_0\times\dfrac{1}{\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}}
$$

Gain :

$$
G = G_0- 20\log(\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}
$$

Phase :

$$
\varphi = -\arctan(\dfrac{2m\dfrac{f}{f_0}}{1-\dfrac{f^2}{f_0^2}})
$$



## Ordre 2 - Passe haut

Transmittance complexe :

$$
\underline{T}
= T_0\times\dfrac{{\rm j}[\dfrac{f^2}{f_0^2}]}{1+2m{\rm j}\dfrac{f}{f_0}+({\rm j}\dfrac{f}{f_0})^2}
\quad\implies\quad
\underline{T}
= T_0\times\dfrac{-\dfrac{f^2}{f_0^2}}{[1-\dfrac{f^2}{f_0^2}]+{\rm j}[2m\dfrac{f}{f_0}]}
$$

Transmittance :

$$
T = T_0\times\dfrac{\dfrac{f^2}{f_0^2}}{\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}}
$$

Gain :

$$
G = G_0 + 20\log(\dfrac{f^2}{f_0^2})- 20\log(\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}
$$

Phase :

$$
\varphi = 180 -\arctan(\dfrac{2m\dfrac{f}{f_0}}{1-\dfrac{f^2}{f_0^2}})
$$



## Ordre 2 - Passe bande

Transmittance complexe :

$$
\underline{T}
= T_0\times\dfrac{2m{\rm j}\dfrac{f}{f_0}}{1+2m{\rm j}\dfrac{f}{f_0}+({\rm j}\dfrac{f}{f_0})^2}
\quad\implies\quad
\underline{T}
= T_0\times\dfrac{{\rm j}[2m\dfrac{f}{f_0}]}{[1-\dfrac{f^2}{f_0^2}]+{\rm j}[2m\dfrac{f}{f_0}]}
$$

Transmittance :

$$
T = T_0\times\dfrac{2m\dfrac{f}{f_0}}{\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}}
$$

Gain :

$$
G = G_0 + 20\log(2m\dfrac{f}{f_0})- 20\log(\sqrt{(1-\dfrac{f^2}{f_0^2})^2+(2m\dfrac{f}{f_0})^2}
$$

Phase :

$$
\varphi = 90 -\arctan(\dfrac{2m\dfrac{f}{f_0}}{1-\dfrac{f^2}{f_0^2}})
$$
