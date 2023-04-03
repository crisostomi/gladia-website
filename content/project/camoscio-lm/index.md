---
title: Camoscio
summary: An Italian instruction-tuned LLaMA

tags:
- opensource
- language model
- italian

date: "2023-03-28T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: "https://github.com/teelinsan/camoscio"

image:
  # caption: Photo by rawpixel on Unsplash
  focal_point: Smart
  preview_only: true


# url_code: "https://github.com/teelinsan/camoscio"
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

authors:
  - santilli

---
<head>
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Camoscio">
  <meta name="twitter:description" content="Camoscio: un language model italiano addestrato a seguire le tue istruzioni">
  <meta name="twitter:image" content="featured.png">
</head>


# 🇮🇹🦙 Camoscio: un language model italiano addestrato a seguire le tue istruzioni

### Contesto

L'intelligenza artificiale ha rivoluzionato l'interazione dell'uomo con la tecnologia, in particolare nell'elaborazione del linguaggio naturale, come dimostrato dal successo dei language modes quali ChatGPT, in grado di dare risposte convincenti alle richieste dell’utente, anche in italiano, ad esempio per generare testi creativi, risolvere problemi matematici, prevedere strutture proteiche o rispondere a domande di comprensione.

Questi modelli sono molto grandi, con miliardi di parametri, il che li rende poco fruibili dai ricercatori; inoltre, non sono accessibili poiché sotto controllo delle grandi corporazioni che li gestiscono. Ciò crea problemi di analisi, studio, efficienza, nonché di riduzione di noti problemi di bias e tossicità di questi modelli.

Recentemente la comunità ha fatto piccoli progressi nello sviluppo di modelli più accessibili, come [LLaMA di Meta AI](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), un modello linguistico addestrato per predire la parola successiva in 20 lingue diverse. Un team di ricerca di Stanford ha poi sviluppato una versione di LLaMA ([Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)) addestrata per seguire istruzioni in inglese, dimostrando che è possibile ottenere performance simili al modello di OpenAI GPT-3 (`text-davinci-003`) pur essendo 25 volte più piccolo.

### Camoscio

In questo contesto, [Andrea Santilli](https://gladia.di.uniroma1.it/authors/santilli/), dottorando del gruppo di ricerca [GLADIA](https://gladia.di.uniroma1.it/) (Sapienza Università di Roma) guidato dal [Prof. Emanuele Rodolà](https://gladia.di.uniroma1.it/authors/rodola/), ha realizzato e condiviso con la comunità Camoscio: un modello addestrato specificamente per comprendere e seguire istruzioni in lingua italiana. Partendo dal lavoro fatto con Stanford Alpaca, traducendo il dataset di *instruction-tuning* in italiano e utilizzandolo per addestrare il modello LLaMA. Il contributo è particolarmente rilevante in quanto:
- mettiamo a disposizione **il primo dataset Italiano** per addestrare modelli a seguire istruzioni;
- rendiamo pubblico il modello addestrato su tale dataset, **completamente open source**, e che dovrebbe offrire prestazioni qualitativamente simili a GPT-3;
- pubblichiamo inoltre la repository per **replicare tutti gli esperimenti**;
- il modello è **piccolo e investigabile**, può essere eseguito su un Raspberry Pi, e si presta ad essere studiato senza necessitare di enormi risorse di calcolo.

Pur con le dovute limitazioni, il modello è un primo passo verso lo **sviluppo di modelli open ed accessibili alla comunità** in grado di seguire istruzioni impartite in linguaggio naturale italiano.

### ✉️ Subscribe
Se sei interessato ad ulteriori aggiornamenti su questo progetto, puoi lasciare qui la tua email per essere aggiornato.
Non ti preoccupare, non ti invieremo spam! Puoi eliminarti in qualsiasi momento [contattandoci](mailto:rodola@di.uniroma1.it).
<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/classic-071822.css" rel="stylesheet" type="text/css">
<style type="text/css">
	#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif}
	/* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
	   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup" class="mb-3">
    <form action="https://uniroma1.us21.list-manage.com/subscribe/post?u=ead8e66ef83dbcc3028d24ed9&amp;id=d015ac5ed8&amp;f_id=00a4a9e1f0" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
        <div id="mc_embed_signup_scroll">
<div class="mc-field-group">
	<label for="mce-EMAIL">Indirizzo Email </label>
	<input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL" required>
	<span id="mce-EMAIL-HELPERTEXT" class="helper_text"></span>
</div>
	<div id="mce-responses" class="clear foot">
		<div class="response" id="mce-error-response" style="display:none"></div>
		<div class="response" id="mce-success-response" style="display:none"></div>
	</div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_ead8e66ef83dbcc3028d24ed9_d015ac5ed8" tabindex="-1" value=""></div>
        <div class="optionalParent">
            <div class="clear foot">
                <input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button">
            </div>
        </div>
    </div>
</form>
</div class>
<script type='text/javascript' src='//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js'></script><script type='text/javascript'>(function($) {window.fnames = new Array(); window.ftypes = new Array();fnames[0]='EMAIL';ftypes[0]='email';fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';fnames[3]='ADDRESS';ftypes[3]='address';fnames[4]='PHONE';ftypes[4]='phone';fnames[5]='BIRTHDAY';ftypes[5]='birthday';}(jQuery));var $mcj = jQuery.noConflict(true);</script>
<!--End mc_embed_signup-->


### 🔗 Link utili

- [Github Repository](https://github.com/teelinsan/camoscio): qui è possibile trovare la repository github del progetto.
- [Demo](https://colab.research.google.com/github/teelinsan/camoscio/blob/master/notebooks/camoscio-gradio.ipynb): qui è disponibile una demo interattiva del modello.
- [Modello addestrato](https://huggingface.co/teelinsan/camoscio-7b-llama): qui è disponibile il modello addestrato.
- [Dataset Camoscio](https://huggingface.co/datasets/teelinsan/camoscio): qui è disponibile il dataset di addestramento.



### 📝 Esempi di Output

<span style="color:red">**Instruction**</span>: Scrivi una breve biografia su Dante Alighieri

**Alpaca-LoRA**: Dante Alighieri (1265-1321) was an Italian poet, philosopher, and political figure. He is best known for his epic poem, The Divine Comedy, which is widely considered to be one of the greatest works of literature ever written. Dante was born in Florence, Italy, and spent much of his life in exile. He wrote The Divine Comedy while in exile, and it tells the story of his journey through Hell, Purgatory, and Heaven. Dante is considered to be one of the founders of the Italian language, and

**ChatGPT**: Dante Alighieri è stato uno dei più grandi poeti italiani del Medioevo. Nato a Firenze nel 1265, ha studiato nella prestigiosa Scuola di Santa Croce e ha mostrato fin da giovane una grande passione per la poesia. Ha scritto la sua prima opera, "Il Convivio", all'età di 30 anni, ma è soprattutto noto per la sua opera più famosa, "La Divina Commedia". Questo poema epico, scritto in terzine, descrive il viaggio immaginario di Dante attraverso l'Inferno, il Purgatorio e il Paradiso, e rappresenta una sintesi della cultura medievale, della filosofia e della teologia. Dante ha anche avuto una vita politica attiva, partecipando alla vita pubblica di Firenze e sostenendo la fazione guelfa. Tuttavia, dopo essere stato esiliato dalla città nel 1302, ha trascorso il resto della sua vita in esilio, scrivendo le sue opere più importanti e cercando di rientr

<span style="color:#16b764">**Camoscio**</span>: Dante Alighieri (1265-1321) è considerato uno dei più grandi poeti e scrittori italiani di tutti i tempi. Nato a Firenze, è conosciuto principalmente per il suo poema epico La Divina Commedia, che è considerato uno dei capolavori della letteratura occidentale.


---

<span style="color:red">**Instruction**</span>: Dimmi tutte le regioni italiane in ordine alfabetico.

**Alpaca-LoRA**: Abruzzo, Basilicata, Calabria, Campania, Emilia-Romagna, Friuli-Venezia Giulia, Lazio, Liguria, Lombardia, Marche, Molise, Piemonte, Puglia, Sardegna, Sicilia, Toscana, Trentino-Alto Adige, Umbria, Veneto.

**ChatGPT**: Abruzzo, Basilicata, Calabria, Campania, Emilia-Romagna, Friuli-Venezia Giulia, Lazio, Liguria, Lombardia, Marche, Molise, Piemonte, Puglia, Sardegna, Sicilia, Toscana, Trentino-Alto Adige/Südtirol, Umbria, Valle d'Aosta/Vallée d'Aoste, Veneto.

<span style="color:#16b764">**Camoscio**</span>: Le regioni italiane in ordine alfabetico sono: Abruzzo, Basilicata, Calabria, Campania, Emilia-Romagna, Friuli-Venezia Giulia, Lazio, Liguria, Lombardia, Marche, Molise, Piemonte, Puglia, Sardegna, Sicilia, Toscana, Trentino-Alto Adige, Umbria, Valle d'Aosta, Veneto.

---

<span style="color:red">**Instruction**</span>: Dimmi di più sul presidente della repubblica Italiana del 2019.

**Alpaca-LoRA**: The President of the Republic of Italy in 2019 is Sergio Mattarella. He was elected in 2015 and re-elected in 2018. He is the 12th President of the Republic of Italy.

**ChatGPT**: Il presidente della Repubblica Italiana del 2019 era Sergio Mattarella. Nato a Palermo nel 1941, Mattarella è stato eletto presidente nel 2015, succedendo a Giorgio Napolitano. Prima di diventare presidente, ha ricoperto importanti incarichi politici, tra cui quello di ministro della Difesa, della Pubblica Istruzione e della Giustizia. 
Durante il suo mandato, Mattarella è stato impegnato nella promozione dell'unità nazionale e nella difesa della Costituzione italiana. Ha anche sostenuto l'integrazione europea e la cooperazione internazionale. Nel 2018, ha svolto un ruolo importante nella formazione del governo italiano, che ha visto la nomina di un governo di coalizione tra il Movimento 5 Stelle e la Lega. 
Mattarella è stato molto attivo nella difesa dei diritti umani e della giustizia sociale, promuovendo iniziative per combattere la povertà e la disuguaglianza. 

<span style="color:#16b764">**Camoscio**</span>: Il presidente della Repubblica Italiana del 2019 è Sergio Mattarella, che è stato eletto il 31 gennaio 2015 e ha prestato giuramento il 31 gennaio 2015.

---

<span style="color:red">**Instruction**</span>: Riassumi la storia di Pinocchio.

**Alpaca-LoRA**: Once upon a time, there was a wooden puppet named Pinocchio who dreamed of becoming a real boy. He was created by a woodcarver named Geppetto, who loved him very much. Pinocchio was a mischievous puppet who often got into trouble, but he always tried to do the right thing in the end. One day, Pinocchio met a fairy who offered him the chance to become a real boy if he proved himself to be brave, truthful, and unselfish. Pinocchio accepted the fairy's offer and set off on a series of advent

**ChatGPT**: La storia di Pinocchio racconta di un burattino di legno, creato dal falegname Geppetto, che prende vita grazie alla fata turchina. Pinocchio ha un forte desiderio di diventare un bambino vero, ma cade in numerose avventure e inganni, spesso guidato dal suo istinto e dalla sua ingenuità. Nel corso della storia, Pinocchio viene ingannato da un gatto e una volpe, viene imprigionato e trasformato in un asino, ma alla fine dimostra il suo coraggio, la sua lealtà e la sua generosità salvando il padre e ottenendo la sua trasformazione in un bambino vero.

<span style="color:#16b764">**Camoscio**</span>: La storia di Pinocchio racconta di un bambino di nome Pinocchio che vive con i suoi genitori in un piccolo villaggio. Un giorno, Pinocchio incontra un burattino magico che gli dona la possibilità di diventare un vero bambino. Pinocchio inizia una serie di avventure mentre cerca di diventare un vero bambino. Durante il suo viaggio, Pinocchio fa amicizia con molti personaggi e impara molte lezioni di vita. Alla fine, Pinocchio raggiunge il suo obiettivo e diventa un vero bambino.

---

<span style="color:red">**Instruction**</span>: Dimmi quattro parole che fanno rima con 'gatto'.

**Alpaca-LoRA**: Cat, hat, mat, rat.

**ChatGPT**: Piatto, matto, spratto, grattò.

<span style="color:#16b764">**Camoscio**</span>: 'Cattivo, cattivo, cattivo, cattivo.'

---






