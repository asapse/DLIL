# Projet de développement logiciel en industrie de la langue

## Objectifs

Acquérir une expérience de mise en oeuvre de technologies pour la résolution d'une tâche de TALP dans un contexte de traitement de données en français et transcrites automatiquement.

## Tâche de TALP : classification de conversations téléphoniques en motifs d'appels

Nous allons travailler sur le corpus issu du projet [DECODA](http://decoda.univ-avignon.fr/). Ce projet concernait le traitement de conversations téléphoniques de la RATP. Chaque conversation a été classée manuellement en fonction du motif d'appel (14 classes).

Lors de ces TPs, nous allons faire en sorte de reproduire cette classification de manière automatique. Nous disposons des transcriptions et segmentations manuelles (référence) pour chacun des fichiers. Nous disposons aussi de la sortie d'un moteur de reconnaissance automatique de la parole pour chacun de ces fichiers.

Le TP s'articulera en deux phases. Lors de la première phase, vous aurez à votre disposition les transcriptions manuelles (fichiers `.trs`) pour travailler. Lors de la deuxième phase, vous devrez vous contenter des trancriptions automatiques pour essayer d'effectuer la même tâche de classification.

## Phase du projet et calendrier indicatif

Cinq étapes importantes : 
1. Prise en main du corpus de transcriptions manuelles, mise en oeuvre d'une approche de base, évaluation sur le corpus de dev
2. Développement d'une approche personnelle, évaluation sur le corpus de dev
3. Prise en main du corpus de transcriptions automatiques, évaluation de l'approche personnelle, analyse quantitive/qualitative
4. Adaptation de l'approche personnelle sur les transcriptions automatique
5. Evaluation sur le corpus de test des deux approches

Dates importantes

    semaine 50 -  vendredi 15 décembre début de matinée - réception des corpus train et dev de transcription manuelle

    semaine 51 - vendredi 22 décembre fin de matinée -  réception des corpus train et dev de transcription automatique 

    semaine 2 - vendredi 12 janvier - réception des données de test sur les transcriptions manuelles et automatiques

    semaine 3 - vendredi 19 janvier au soir : livraison finale du projet


## Protocole
* Approche de base à mettre en oeuvre : sac de mots tokénisés sur les espaces, pas de pré-traitement, apprentissage supervisé avec classifieur NaiveBayes).
* Métriques d'évaluation à utiliser : micro/macro précision/rappel/F-score

See Multi-labelled classification task. http://atour.iro.umontreal.ca/rali/sites/default/files/publis/SokolovaLapalme-JIPM09.pdf

## Livrable

Un rendu par binôme/trinôme avec une approche personnelle. Néanmoins l'échange et la collaboration en amont ne sont pas interdit.

* rapport (approche mise en oeuvre, performance, difficultés rencontrées et solutions apportées, retour d'expériences sur les technologies testées, sur le traitement des différents types de données)
* code source du projet avec README (avec entre autres les consignes d'installation et d'exécution des différentes phases train/dev/test sur les différents types de données)

Modalités de livraison finales spécifiées ultérieurement.

Vous serez évalué sur la qualité générale du rendu, la diversité et l'originalité des traitements mis en oeuvre.

## Mise en oeuvre technique

Il existe un grand nombre d'outils disponibles dont voici une liste non exhaustive : NTLK,  Spacy, Textblob, OpenNLP, Standford core NLP, Gensim, Mallet, Sklearn, … Jeter un coup d'oeil pour voir le champ des pré-traitements qu'ils offrent et des traits que vous pourrez considérer.


## Corpus

Le corpus vous sera donné en plusieurs phases. Vous aurez tout d'abord accès aux transcriptions manuelles aujourd'hui avec les fichers de dev + train. La semaine prochaine on vous aurez accès aux transcriptions automatiques pour le dev + train. Lors de la dernière semaine, le corpus de test sera dévoilé pour évaluer vos classifieurs.

### Partitions

- Train : 1341 fichiers
- Dev : 291 fichiers
- Test : 305 fichiers

La liste de ces fichiers se trouve dans le répertoire `partitions`.

### Étiquettes

Dans le répertoire `labels` vous trouverez des fichiers `.lst` pour le dev, test et train. Chaque fichier `.lst` contient la liste des fichiers suffixés avec leur classe correspondante _CLASSE (ex: 20091112_RATP_SCD_0009_ETFC).

Les 14 classes (motifs d'appel) sont :

- ETFC = état du trafic
- ITNR = itinéraire
- NVGO = Navigo (cartes et passes) 
- TARF = tarifs
- PV = procès-verbaux
- OBJT = objets trouvés/perdus 
- VGC = vente Grand Compte 
- HORR = horaires
- RETT = remboursement
- CPAG = conflit avec agent de la RATP 
- OFTP = offre de transports palliatif 
- JSTF = justificatif de retard
- NULL = conversations Hors Thème
- AAPL = conversations concernant la SNCF (plutôt que la RATP)

### Transcriptions manuelles

Dans le répertoire `trans-manu` vous trouverez deux types de fichiers intéressants : ce sont les .trs et potentiellement les .uem. Les .trs contiennent la transcription manuelle au format Transcriber (cf. Liens utiles pour le parser) et les .uem contiennent les segmentations de parole en Client/Conseiller.

### Transcriptions automatiques

Dans le répertoire `trans-auto` vous trouverez un unique fichier `trans-asr-decoda.ctm` contenant le résultat des transcriptions automatiques. Chaque ligne représente un mot. Si vous avez besoin de reconstituer les « phrases » (on parle de groupes de souffles en reconnaissance automatique de la parole, le concept de phrase n'a pas de sens), vous devrez corréler les informations contenues dans ce fichier .ctm avec celles contenues dans les fichiers .uem.

Voici un exemple de ligne d'un CTM :

20091112_RATP_SCD_0001 1 10.014 0.02 rue 0.98

Chaque champ est séparé par un espace. La signification des différents champs :
1. Nom du fichier
2. Non utilisé
3. Timestamp de début du mot (en secondes)
4. Durée du mot (en secondes)
5. Mot
6. Mesure de confiance, proba.

### Liens utiles

- http://trans.sourceforge.net/en/tools.php : Permet de transoformer les fichiers XML trs en fichiers « plats »

## Misc

Quelques suggestions/conseils
* Si vous envisagez de produire les data dans un format intermédiaire, préférer un format : un fichier par corpus, une ligne par instance, classe tabulation puis la conversation en brute sur une ligne. C'est peut être contraignant mais ca a aussi des avantages pour tester différents outils. N'hésitez pas à aller jeter un oeil à la bibliothèque python Pandas
* Faites bien attention à l'encodage des fichiers. Ils ont été produits à un moment où l'ISO-8859-1 était encore beaucoup utilisé. La commande unix `iconv -f iso-8859-15 -t utf-8 test.txt > test.utf8.txt` permet de transformer un fichier encodé en iso-8859-1 (test.txt) en fichier encodé en utf8 (test.utf8.txt)
