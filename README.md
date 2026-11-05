# Cash Counter

Comptage de caisse pour smartphone (PWA installable, fonctionne hors ligne).
Les comptages restent dans le téléphone (localStorage), rien n'est envoyé.

- Site : https://nicolasmbronner.github.io/cash-counter/
- Fichiers : `index.html` (app complète), `manifest.webmanifest`, `sw.js` (cache hors ligne), icônes PNG. Aucune dépendance.
- Mise à jour : après toute modification, incrémenter `VERSION` dans `sw.js`, sinon le téléphone garde l'ancienne version en cache.
- Icônes : `python icons.py` (Pillow) les régénère.
- Test local : `python -m http.server` puis http://localhost:8000/ (le service worker exige http://localhost ou https).

## Choix v9

- Écran principal strictement fixe (`position:fixed; inset:0; overflow:hidden`, pas de `100vh/100dvh`). Seuls défilent la bande des coupures (horizontal) et Réglages (vertical).
- Règle de ⌫ :
  - mode ajout avec chiffres (`20 + 50_`) : annule tout l'ajout en cours, retour à `20`, sortie du mode ajout ;
  - mode ajout vide (`20 + _`) : sort du mode ajout ;
  - hors mode ajout, s'il y a un historique d'ajouts (rouleaux compris) : retire le dernier terme ajouté, répétable (`20 + 50 + 12` → `20 + 50` → `20`) ;
  - plus aucun ajout (quantité de base seule) : efface un chiffre.
- Vibrations (interrupteur conservé), constantes `V_SHORT`, `V_NORMAL`, `V_DOUBLE` en tête du script :
  - courte 60 ms : chiffres, ⌫, +1, −1, Préc., puce ;
  - normale 100 ms : Suivant, + Ajouter, + rouleau, interrupteur ;
  - double `[100,80,100]` : Effacer confirmé, Nouveau comptage confirmé, plafond 9999.
