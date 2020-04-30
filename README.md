# Reseptikirja
Web-sovellus, jossa käyttäjä voi tehdä reseptejä ja laittaa niitä muiden nähtäväksi.
Web-sovellukseni on sovellus, jossa peruskäyttäjät voivat laittaa sivustolle ja tietokantaan
reseptejä, joita kuka vain voi katsoa vaikka ilman käyttäjää. Reseptejä voi myös päivittää tai poistaa.

# Asennusohje
Lataa tai kloonaa sovelluksen repositorio ja asenna tiedostossa: "requirements.txt" olevat
vaatimukset. Tämän jälkeen voit käynnistää palvelimen repositorion juuresta komennolla:
"python3 run.py". Mene selaimella osoitteeseen, joka ilmestyy komentoriville kun ajat
edellisen komennon ja voit sitten käyttää sovellusta.

# Käyttöohje
### Sovellus herokussa:
[Reseptikirja](https://ostoskassi.herokuapp.com/)

Rekisteröityminen pitää tehdä käsin sqlite tulkin kautta Recipes.db tietokantaan.
Rekisteröidyttyäsi voit käyttää kaikkia sovelluksen ominaisuuksia. Voit kirjautua sisään tai ulos sovelluksen oikeasta yläkulmasta.
Kaikille toiminnallisuuksille on selkeät napit. Kuka tahansa voi katsoa muiden reseptejä. Mutta uusia reseptejä voi luoda vain
kirjautuneet käyttäjät.

# Sovelluksen rajoitteet
Sovellukseen voisi lisätä selkeän rekisteröitymistoiminnallisuuden, jossa ei olisi esimerkiksi sql-injektio mahdollisuuksia.
Jostain syystä en saanut reseptien tekijöiden nimiä näkymään vaan sen tilalla on heidän id:nsä.
Sovellukseen voisi lisätä vielä esimerkiksi uuden tietokantataulun reseptien valmistusohjeille eikä vain ainesosille.
Admin-käyttäjät ja heidän toiminnallisuudet voisi myös lisätä sovellukseen. Admin-käyttäjillä voisi olla esimerkiksi
oikeus estää tiettyjä käyttäjiä tekemästä reseptejä, jos siihen olisi aihetta.
Tiettyjä seikkoja voisi parannella ulkonäössä, esimerkiksi jos ei omista reseptiä niin edit nappi ei edes näkyisi sille käyttäjälle. Tällä hetkellä edit nappi näkyy kaikille mutta vain reseptin omistaja voi sitä käyttää.
