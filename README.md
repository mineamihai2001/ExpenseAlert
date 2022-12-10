# ExpenseAlert

Creati un tool care gestioneaza chetuielile intr-o companie si genereaza alerta cand pentru o
anumita categorie de cheltuieli se depaseste o anumita limita de buget prestabilita.
Tool-ul va monitoriza un director in care apar facturi si va actualiza informatiile intr-o baza de
date.
Utilizatorul poate seta pentru anumite cheltuieli categorii generale ( ex: Chirie ar fi in categoria
Administrative ). Daca pentru o anumite cheltuiala nu este specificata categoria ( in factura
sau in baza de date ) se va considera automat ca face parte din categoria “Diverse”. Toate
cheltuielile din categoria Diverse pot fi catalogate manual. Formatul unui fisier de tip factura
este ceva ce puteti decide voi (ex: un fisier JSON sau fisier XML)

**INPUT** :
Director cu facturi ce va fi monitorizat.
Fisier cu lista de praguri pentru categorii de cheltuieli
( formatele fisierelor vor fi stabilite de dezvoltator )

**OUTPUT** :
Alertele depasire limita pentru anumite categorii - in momentul in care apar
Loguri pentru operatiuni si erorile cand apar