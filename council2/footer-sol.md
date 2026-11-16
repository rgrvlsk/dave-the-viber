Proposo tecles de llautó amb tinta fosca, damunt del taulell. CSS provat al navegador amb el tema publicat. Cap fitxer del projecte ni tema modificat.

El peu actual fa 70 px. A 1440×900 i barra de 255 px, el taulell ocupa y=846–862; els botons, y=860–892. Se superposen 2 px. El frontal marró ocupa 38 px. El botó d'actualització conserva el cercle gris perquè queda fora del selector existent.

La proposta posa els botons a y=840–872, el taulell a y=876–892 i el frontal a y=892–900. Deixa 4 px entre les tecles i la fusta. El peu creix 12 px. Manté els botons de 32×32 i els espais de 4 px. El koi conserva la seva franja superior. El selector cobreix també el botó d'actualització simulat.

CSS per afegir després de la secció del peu a `src2/extras.css`. Conserva les regles existents del koi, del compositor i de moviment reduït. A la injecció he substituït únicament `--sk-wood` pel nom compilat `--km1`.

```css
[data-slot="sidebar-footer"] {
  padding-top:22px!important;
  padding-bottom:28px!important;
  background-position:left bottom 8px,0 0!important;
  background-image:var(--sk-wood),linear-gradient(transparent calc(100% - 8px),#8f5a2b 0)!important;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] [data-slot="sidebar-menu-item"]>button {
  border:1px solid #3a2414!important;
  border-radius:0!important;
  background:#d8a15f!important;
  color:#3a2414!important;
  clip-path:none!important;
  box-shadow:inset 1px 1px #ffe0a2,inset -1px -2px #a8703a!important;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] [data-slot="sidebar-menu-item"]>button:hover {
  background:#edba78!important;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] [data-slot="sidebar-menu-item"]>button:active {
  box-shadow:inset 1px 2px #a8703a!important;
}
[data-slot="sidebar-footer"] [data-slot="sidebar-menu-item"]>button:focus-visible {
  outline:2px solid #fff3dc!important;
  outline-offset:2px;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] button svg.lucide {
  color:#3a2414!important;
  filter:none!important;
}
```

Evidència, a aquesta mateixa carpeta:

- `before-dark.png`, `before-light.png`: abans, 255 px.
- `after-dark.png`, `after-light.png`: després, 255 px.
- `after-dark-fixed.png`, `after-light-fixed.png`: koi congelat; diferència PIL de 0 píxels.
- `hover-focus.png`: hover real i focus visible confirmat amb `matches(':focus-visible')`.
- `wide.png`: amplada mesurada de 339 px, sense solapament.

Contrast calculat sRGB de tinta #3a2414: 6,37:1 sobre #d8a15f; 8,25:1 sobre hover #edba78. Fins i tot el bisell més fosc dona 3,50:1. CSS de 1.077 caràcters amb espais minificats, sense nous sprites ni animacions. Sis regles parsejades.

Límits: no he provat una pulsació mantinguda. El CSS de pressed inverteix el bisell sense moure el botó. Actualització simulada amb CircleArrowUp; Download, progrés, badges i avisos opcionals no verificats. No he executat build ni validator perquè el brífing exclou edicions del projecte. Pestanya tancada.
