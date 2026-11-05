# Cash Counter

Comptage de caisse pour smartphone (PWA installable, fonctionne hors ligne).
Les comptages restent dans le téléphone (localStorage), rien n'est envoyé.

- Site : https://nicolasmbronner.github.io/cash-counter/
- Fichiers : `index.html` (app complète), `manifest.webmanifest`, `sw.js` (cache hors ligne), icônes PNG. Aucune dépendance.
- Mise à jour : après toute modification, incrémenter `VERSION` dans `sw.js`, sinon le téléphone garde l'ancienne version en cache.
- Icônes : `python icons.py` (Pillow) les régénère.
- Test local : `python -m http.server` puis http://localhost:8000/ (le service worker exige http://localhost ou https).

## Choix v7

- Écran principal strictement fixe : `html,body` en `position:fixed; inset:0; overflow:hidden` et `.app` en `position:fixed; inset:0` (plus de `100vh/100dvh`, dont la valeur peut dépasser la zone visible d'une PWA Android et créer un défilement). Seuls défilent la bande des coupures (horizontal) et Réglages (vertical).
- Vibrations (interrupteur Vibration conservé, pas de réglage de durée) :
  - courte 20 ms : chiffres, ⌫, +1, −1, Préc., saut par appui sur une puce ;
  - normale 40 ms : Suivant, + Ajouter, + rouleau ;
  - double `[40,60,40]` : Effacer confirmé, Nouveau comptage confirmé, dépassement du plafond 9999.
