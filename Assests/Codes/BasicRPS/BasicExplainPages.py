from ..ExplanationPage import Page
from ..consoleColors import bcolors as ccolors


#Page1

Page1 = Page(f"""
{ccolors.IMORANGE}from{ccolors.ENDC} random {ccolors.IMORANGE}import{ccolors.ENDC} choice

choices  {ccolors.OPERATORS}= {ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Taş{ccolors.CODEGREY}", "{ccolors.STRINGG}Kağıt{ccolors.CODEGREY}", "{ccolors.STRINGG}Makas{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
winScore {ccolors.OPERATORS}= {ccolors.OKCYAN}3{ccolors.ENDC}

userScore {ccolors.OPERATORS}= {ccolors.OKCYAN}0{ccolors.ENDC}
computerScore {ccolors.OPERATORS}= {ccolors.OKCYAN}0{ccolors.ENDC}

run {ccolors.OPERATORS}= {ccolors.BOOLS}True{ccolors.ENDC}
{ccolors.OPERATORS}while {ccolors.ENDC}run{ccolors.CODEGREY}:{ccolors.ENDC}
...
...
...

{ccolors.CODEGREY}{'/'*22}AÇIKLAMA{'/'*23}{ccolors.ENDC}
{ccolors.OKBLUE}1-){ccolors.ENDC} İlk satırda "random" kütüphanesinden "choice" modülünü kodumuza ekledik. Bu kod verilen liste arasından rastgele bir seçeneği seçer
{ccolors.OKBLUE}2-){ccolors.ENDC} "choices" değişkenimize ise oyundaki muhtemel seçenekleri yazdık. Birazdan buradaki listeyi bilgisayarın rastgele bir hamle seçmesi için kullanacağız.
{ccolors.OKBLUE}3-){ccolors.ENDC} Oyunun kaçıncı skorda bitip kazanını seçeceğini "winScore" değişkeniyle belirledik. İstediğimiz skorda oyunu bitirtebiliriz.
{ccolors.OKBLUE}4-){ccolors.ENDC} Oyuncunun ve bilgisayarın skorlarını tutacak değişkenler oluşturmamız gerekiyor. Bunları "userScore" ve "computerScore" isimleriyle atadık. Skorlarını ise 0 olarak belirledik çünkü daha maç oynamadılar.
{ccolors.OKBLUE}5-){ccolors.ENDC} Eğer ki bir koşul sonucunda sona erecek bir while döngümüz var ise bunu belirleyecek bir değişkenimiz olmalı. "run" değişkenini {ccolors.BOOLS}True{ccolors.ENDC} olarak atadık. Bu sebepten ötürü "while run:" kısmını Türkçe olarak düşündüğümüzde "run değişkeni {ccolors.BOOLS}True{ccolors.ENDC} olduğu sürece yap:" tarzında bir sonuç çıkıyor.
{ccolors.OKBLUE}6-){ccolors.ENDC} {ccolors.OPERATORS}while{ccolors.ENDC} döngüleri koşulları doğru yani {ccolors.BOOLS}True{ccolors.ENDC} olduğu sürece devam ederler. Bu senaryoda "run" değişkenini {ccolors.BOOLS}False{ccolors.ENDC} olarak atadığımızda döngü sona erecek.

{ccolors.FAIL}Önemli Not!-) {ccolors.OPERATORS}while{ccolors.ENDC}'ın yanına {ccolors.BOOLS}True{ccolors.ENDC} koysaydık {ccolors.BOOLS}True{ccolors.ENDC} koşulunu sona erdirmek için "{ccolors.OPERATORS}break{ccolors.ENDC}" modülünü kullanacaktık. Fakat bu senaryoda olmasa bile başka kodlarda ve projelerde iç içe döngüler olabileceğinden "{ccolors.OPERATORS}break{ccolors.ENDC}" modülü sadece mevcut döngüyü durduracaktı. Bu yüzden kodumuz çalışmaya devam edecekti. Bu yüzden hem bu sorunları çözmek hem de takibini kolaylaştırmak için "run", "appRun", "isRun" tarzında değişkenler kullanmalıyız.

{ccolors.WARNING}Sayfa 1/6{ccolors.ENDC}""")

##Page2

Page2 = Page(f"""
{ccolors.OPERATORS}while{ccolors.ENDC} run{ccolors.CODEGREY}:{ccolors.ENDC}
    computerChoice = {ccolors.MODULES}choice{ccolors.YELLOW}({ccolors.ENDC}choices{ccolors.YELLOW}){ccolors.ENDC}
    userChoice = {ccolors.MODULES}input{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Seçim yapın (Taş, Kağıt, Makas): {ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.CODEGREY}.{ccolors.MODULES}lower{ccolors.YELLOW}(){ccolors.ENDC}
    {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice.{ccolors.ENDC}{ccolors.MODULES}lower{ccolors.ENDC}{ccolors.YELLOW}(){ccolors.ENDC} {ccolors.OPERATORS}=={ccolors.ENDC} userChoice{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: {ccolors.CODEGREY}",{ccolors.ENDC} computerChoice{ccolors.YELLOW}){ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Berabere{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
...
...
...

{ccolors.CODEGREY}{'/'*22}AÇIKLAMA{'/'*23}{ccolors.ENDC}
{ccolors.OKBLUE}1-){ccolors.ENDC} "computerChoice" değişkeni her {ccolors.OPERATORS}while{ccolors.ENDC} döngüsünde yani her tur sonunda rastgele seçilen oyun hamlesini tutuyor. Daha öncesinden dediğim gibi {ccolors.MODULES}choice{ccolors.ENDC} modülü "choices" listesinden bir hamle seçiyor.
{ccolors.OKBLUE}2-){ccolors.ENDC} "userChoice" değişkeni her tur başında oyuncudan istenilen hamleyi tutuyor. {ccolors.MODULES}input{ccolors.ENDC} modülü kodu durdurur ve konsol üzerinden gelen ilk girdiyi alır. {ccolors.MODULES}input{ccolors.YELLOW}(){ccolors.ENDC} parantezin içine yazılan herhangi bir yazı ise girdinin başında gözükür. Boş da bırakabilirsiniz fakat sadece imleç yanıp söner ve ne yapmamız gerektiğini kullanıcıya aktaramayız.
{ccolors.OKBLUE}3-){ccolors.ENDC} input modülünün sonunda {ccolors.MODULES}lower{ccolors.YELLOW}(){ccolors.ENDC} modülünü de kullandık. Bu hamle çoğu konsol uygulamasında kullanılır. Bunun sayesinde konsola "taŞ", "TAŞ", "Taş" da yazılsa bu yazıyı "taş" haline getirecek ve bizde kullanıcının girdisini kontrol ederken ne türde yazdığını önemsemeyeceğiz. Girdinin küçük harflerle "taş" olmasını umacağız.
{ccolors.OKBLUE}3-){ccolors.ENDC} {ccolors.OPERATORS}if{ccolors.ENDC} koşulumuzda ise bilgisayarın seçiminin kullanıcının seçimine eşit olup olmadığını kontrol ediyoruz.
{ccolors.OKBLUE}4-){ccolors.ENDC} Bilgisayar seçimini küçük hale getirmemizin sebebi ("computerChoice{ccolors.CODEGREY}.{ccolors.MODULES}lower{ccolors.YELLOW}(){ccolors.ENDC}") bilgisayarın seçim yaptığı "choices" listesindeki yazıların baş harflerinin büyük yazılması. Eğer bilgisayar seçimini küçültmezsek "Kağıt {ccolors.BOOLS}=={ccolors.ENDC} kağıt" tarzında bir koşul bakacaktır ve istenmeyen sonuçlar doğuracaktır.
{ccolors.OKBLUE}5-){ccolors.ENDC} Peki ya neden doğrudan choices listesini küçük harflerle donatmadık? Sebebi basit. Oyunun ileri aşamalarında bilgisayarın seçimini konsola yazdıracağız. Bu sırada konsolda estetik durması adına baş harfinin büyük durmasını istiyoruz. Detaylar sizi hem farklı çözümler düşünmeye zorlar ve sizi geliştirir hem de uygulamalarınızın kalite standartlarını geçmesine, yetişmesine neden olur.
{ccolors.OKBLUE}6-){ccolors.ENDC} Eğer eşit olma koşulu sağlanırsa oyuncunun karşılaştırması adına bilgisayarın seçimini konsola yazdırıyoruz. Ardından sonucu paylaşmak için konsola "Berabere" yazdırıyoruz. Bundan sonra başka bir tur başlayacak, {ccolors.OPERATORS}while{ccolors.ENDC} döngüsünün başına döneceğiz.

{ccolors.WARNING}Sayfa 2/6{ccolors.ENDC}""")

#Page3

Page3 = Page(f"""
{ccolors.OPERATORS}while{ccolors.ENDC} run{ccolors.CODEGREY}:{ccolors.ENDC}
    computerChoice = {ccolors.MODULES}choice{ccolors.YELLOW}({ccolors.ENDC}choices{ccolors.YELLOW}){ccolors.ENDC}
    userChoice = {ccolors.MODULES}input{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Seçim yapın (Taş, Kağıt, Makas): {ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.CODEGREY}.{ccolors.MODULES}lower{ccolors.YELLOW}(){ccolors.ENDC}

    {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice.{ccolors.ENDC}{ccolors.MODULES}lower{ccolors.ENDC}{ccolors.YELLOW}(){ccolors.ENDC} {ccolors.OPERATORS}=={ccolors.ENDC} userChoice{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: {ccolors.CODEGREY}",{ccolors.ENDC} computerChoice{ccolors.YELLOW}){ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Berabere{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}elif{ccolors.ENDC} userChoice {ccolors.OPERATORS}=={ccolors.ENDC} {ccolors.CODEGREY}"{ccolors.STRINGG}taş{ccolors.CODEGREY}":
        {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}Makas{ccolors.CODEGREY}":{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Makas{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyuncu kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
        {ccolors.OPERATORS}else{ccolors.CODEGREY}:
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Kağıt{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            computerScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
...
...
...

{ccolors.CODEGREY}{'/'*22}AÇIKLAMA{'/'*23}{ccolors.ENDC}
{ccolors.OKBLUE}1-){ccolors.ENDC} {ccolors.OPERATORS}elif{ccolors.ENDC} koşul sağlayıcının açılımı aslında {ccolors.OPERATORS}else if{ccolors.ENDC}'dir. Yani en baştaki {ccolors.OPERATORS}if{ccolors.ENDC} koşulundaki değer dönmüyorsa bir de bu koşula bak demektir.
{ccolors.OKBLUE}2-){ccolors.ENDC} İlk koşulumuzda yani {ccolors.OPERATORS}if{ccolors.ENDC} satırımızda hamlelerin aynı olup olmadıklarına baktık. Eğer hamleler aynı değilse yani {ccolors.OPERATORS}if{ccolors.ENDC} koşulumuz {ccolors.BOOLS}False{ccolors.ENDC} döndürsüyse sonraki koşul sağlayıcısına gider. Bu da aynı girintideki (Python dilinde süslü parentezler yoktur. Bunun yerine girintileri kullanırız. Yani satırın başında kaç boşluk olduğuyla ilgilidir.) diğer koşul sağlayıcısına gitmesi demektir.
{ccolors.OKBLUE}3-){ccolors.ENDC} {ccolors.OPERATORS}if{ccolors.ENDC}'ten sonraki ilk koşul sağlayıcımız {ccolors.OPERATORS}elif{ccolors.ENDC} satırında oyuncu hamlesinin "{ccolors.STRINGG}Taş{ccolors.ENDC}" olması durumunda çalıştırılacak kodu tanımlıyoruz. Eğer kullanıcı hamlesi yani "userChoice" "{ccolors.STRINGG}Taş{ccolors.ENDC}" değilse diğer koşul sağlayacısını arayacak. Unutmayın kullanıcı girdisini küçük harflere dönüştürmüştük bu yüzden doğrudan "{ccolors.STRINGG}taş{ccolors.ENDC}" olup olmamasını kontrol ediyoruz. Eğer girdiyi küçültmeseydik girdi "{ccolors.STRINGG}Taş{ccolors.ENDC}" olsa bile bu satırda koşul {ccolors.BOOLS}True{ccolors.ENDC} olarak sağlanmayacaktı.
{ccolors.OKBLUE}4-){ccolors.ENDC} Eğer ki kullanıcı seçimi taş ise tekrardan bir koşul araması yapacağız. Sorun üzerine düşünelim. Şuanda elimizde iki olasılık var. Ya makas gelir ve kazanırız ya da gelmez veya kaybederiz. Beraber kalabilme durumumuz da var gibi duruyor değil mi? Genel düşünürsek taş seçildiğinde karşı tarafın da taş seçme olasılığı var fakat biz bunun olup olmadığını zaten ilk if koşulunda kontrol ettik. Eğer en başta berabere olma durumunu kontrol etmeseydik her hamlemizde berabere olup olmadığımızı kontrol etmemiz gerekirdi. Bu da koda ve bize fazladan yük demekti. Çoğu {ccolors.OPERATORS}if{ccolors.ENDC}-{ccolors.OPERATORS}else{ccolors.ENDC} koşullarında bu tarz durumlara dikkat etmelisiniz bu sadece bir örnek oldu.
{ccolors.OKBLUE}5-){ccolors.ENDC} Eğer bilgisayarın seçimi makas ise kaybedeceğiz. Unutmayın bu projede bilgisayarın seçim yapacağı listedeki isimler büyük harfle başlıyordu bu yüzden buna göre karşılaştırma yapacağız. 'computerChoice {ccolors.OPERATORS}=={ccolors.ENDC} {ccolors.CODEGREY}"{ccolors.STRINGG}Makas{ccolors.CODEGREY}"{ccolors.ENDC}' bu koşulda eğer bilgisayarın seçimi makas yani kodsal dilde {ccolors.STRINGG}Makas{ccolors.ENDC} stringi ise burası {ccolors.BOLD}True{ccolors.ENDC} dönecek. {ccolors.BOLD}True{ccolors.ENDC} döndüğü için {ccolors.OPERATORS}if{ccolors.ENDC} koşulu sağlanacağından alttaki kod çalışacak.
{ccolors.OKBLUE}6-){ccolors.ENDC} Unutmayın berabere kalma durumunu sorgularken "computerChoice" seçeneğini küçük harflere dönüştürmüştük. Çünkü userChoice girdisi her türlü küçük olacak. Önceki sayfada detaylı açıklaması var.
{ccolors.OKBLUE}7-){ccolors.ENDC} Eğer koşul sağlandıysa yani biz taş bilgisayar da makas seçtiyse kazanacağız. Oyuncunun da bilgisayarın seçimini görebilmesi için bunu konsola yazdırıyoruz. Doğrudan doğruya makas seçtiğini {ccolors.MODULES}print{ccolors.ENDC} modülünün içine elimizle yazabiliriz çünkü zaten bilgisayarın makas seçmesi durumunda çalışacak olan kodu yazıyoruz.
{ccolors.OKBLUE}8-){ccolors.ENDC} Kazandığımız için kendi puanımıza yani oyuncunun puanına 1 puan ekleyeceğiz. Bunu doğrudan doğruya "userScore {ccolors.OPERATORS}={ccolors.ENDC} userScore {ccolors.OPERATORS}+ {ccolors.OKCYAN}1{ccolors.ENDC}" şeklinde de yapabiliriz fakat kısa yol olarak "userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1{ccolors.ENDC}" kullanacağız. Fazladan efora gerek yok. {ccolors.OKCYAN}+{ccolors.ENDC} ve {ccolors.OPERATORS}={ccolors.ENDC}'ın yeri önemli. Önce işlem operatörü ardından eşittir. En sonunda da oyuncunun kazandığını konsoldan bildireceğiz.
{ccolors.OKBLUE}9-){ccolors.ENDC} Eğer hiçbir koşul sağlanmazsa yani bütün {ccolors.OPERATORS}if{ccolors.ENDC} ve {ccolors.OPERATORS}elif{ccolors.ENDC} durumları {ccolors.BOOLS}False{ccolors.ENDC} döndüyse yapılacak olan işi {ccolors.OPERATORS}else{ccolors.ENDC} ile belirtiyoruz. Kısaca "Bu koşul sağlanmadı. Bu koşul da sağlanmadı. O halde şunu yap:" anlamına dönüyor.
{ccolors.OKBLUE}10-){ccolors.ENDC} Aynı hamleyi yapma olasılığını en başta bakmıştık. Halihazırda makas olma koşuluna da baktık o halde son bir koşul yani hamle kalıyor o da bilgisayarın kağıt seçme durumu. Kağıt seçmiş ise biz taş seçtiğimiz için kaybedeceğiz. Aynı şekilde bilgisayarın hamlesini yazıyoruz, bilgisayara puan ekliyoruz ve bilgisayarın kazandığını belirtiyoruz.

{ccolors.FAIL}X-){ccolors.ENDC} Oyuncunun seçebileceği her bir hamle için aynı işlemi yapacağım. Bunları tekrar anlatmayacağım diğer sayfada tüm şekilde görebilirsin. Tabii oraya bakmadan önce kendin tamamlamaya çalış.

{ccolors.WARNING}Sayfa 3/6{ccolors.ENDC}""")

#Page4

Page4 = Page(f"""
{ccolors.OPERATORS}while{ccolors.ENDC} run{ccolors.CODEGREY}:{ccolors.ENDC}
    computerChoice = {ccolors.MODULES}choice{ccolors.YELLOW}({ccolors.ENDC}choices{ccolors.YELLOW}){ccolors.ENDC}
    userChoice = {ccolors.MODULES}input{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Seçim yapın (Taş, Kağıt, Makas): {ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.CODEGREY}.{ccolors.MODULES}lower{ccolors.YELLOW}(){ccolors.ENDC}
    
    {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice.{ccolors.ENDC}{ccolors.MODULES}lower{ccolors.ENDC}{ccolors.YELLOW}(){ccolors.ENDC} {ccolors.OPERATORS}=={ccolors.ENDC} userChoice{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: {ccolors.CODEGREY}",{ccolors.ENDC} computerChoice{ccolors.YELLOW}){ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Berabere{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}elif{ccolors.ENDC} userChoice {ccolors.OPERATORS}=={ccolors.ENDC} {ccolors.CODEGREY}"{ccolors.STRINGG}taş{ccolors.CODEGREY}":
        {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}Makas{ccolors.CODEGREY}":{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Makas{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyuncu kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
        {ccolors.OPERATORS}else{ccolors.CODEGREY}:
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Kağıt{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            computerScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}elif{ccolors.ENDC} userChoice {ccolors.OPERATORS}=={ccolors.ENDC} {ccolors.CODEGREY}"{ccolors.STRINGG}kağıt{ccolors.CODEGREY}":
        {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}Taş{ccolors.CODEGREY}":{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Taş{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyuncu kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW})
        {ccolors.OPERATORS}else{ccolors.CODEGREY}:
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Makas{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            computerScore {ccolors.OPERATORS}+={ccolors.ENDC} {ccolors.OKCYAN}1{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}elif{ccolors.ENDC} userChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}makas{ccolors.CODEGREY}":{ccolors.ENDC}
        {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}Kağıt{ccolors.CODEGREY}":{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Kağıt{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyuncu kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW})
        {ccolors.OPERATORS}else{ccolors.CODEGREY}:
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Taş{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            computerScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
...
...
...

{ccolors.WARNING}Sayfa 4/6""")

#Page5

Page5 = Page(f"""
    ...
    ...
    ...
    {ccolors.OPERATORS}if{ccolors.ENDC} userScore {ccolors.OPERATORS}=={ccolors.ENDC} winScore{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyunu kazandın!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
        run {ccolors.OPERATORS}= {ccolors.BOOLS}False
    {ccolors.OPERATORS}elif{ccolors.ENDC} computerScore {ccolors.OPERATORS}=={ccolors.ENDC} winScore{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyunu kaybettin!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
        run {ccolors.OPERATORS}= {ccolors.BOLD}False

{ccolors.CODEGREY}{'/'*22}AÇIKLAMA{'/'*23}{ccolors.ENDC}
{ccolors.OKBLUE}1-){ccolors.ENDC} Oyunumuzun son koşul sorgulamasına geldik. Buradaki if-else koşulunu önceki if-else koşullarıyla aynı girintide yapıyoruz buraya dikkat. Bunun sebebi: hamlelerin olasılıklarına baktıktan sonra oyunu bir tarafın kazanıp kazanmadığına bakmamız gerektiği
{ccolors.OKBLUE}2-){ccolors.ENDC} Başka bir mantıkla birisi her puan kazandığında da oyunu kazanıp kazanmadığını yani skorunun oyunu kazanma skoruna eşit olup olmadığını kontrol edebilirdik fakat bu bize fazladan boş bir iş yükü olurdu. Yukaridaki her iç if-else yani hamle sorgulamasından sonra bunu yaptığımızı düşünün.
{ccolors.OKBLUE}3-){ccolors.ENDC} Sırası önemli değil burada ilk olarak oyuncunun skorunu taşıyan "userScore" değişkenini sorguladım. Bu değişkenin değeri oyunu kazanma sayısına eşitse oyunu oyuncu kazanmış olacak.
{ccolors.OKBLUE}4-){ccolors.ENDC} Eğer bu koşul True dönmüyorsa sonraki koşul sorgulamaya geçecek. Yani alttaki elif sorgusuna. Burada da bilgisayarın puanının kazanma skoruna eşit olup olmadığına bakıyoruz.
{ccolors.OKBLUE}5-){ccolors.ENDC} İkisinden birisinde koşul True dönerse kimin kazandığına göre değişecek şekilde bunu konsola yazdırıyoruz. Bundan sonra ise while döngümüzü çalıştıran "run" değişkenimizin değerini değiştireceğiz. İlk sayfadan hatırlarsanız run değişkenini True olarak atamıştık. run değişkeni True olduğu süreç boyunca while çalışacaktı. Detaylı anlatım birinci sayfada.
{ccolors.OKBLUE}6-){ccolors.ENDC} run değişkenini False olarak atıyoruz ve while döngüsü en başa dönüyor. Döngüyü tekrar başlatmadan önce kendi koşulunu sorguluyor. Kendi koşulu yani run değişkeni artık False olduğundan dolayı while kendisini tekrar etmiyor ve kod/oyun kapanmış, bitmiş oluyor.
{ccolors.OKBLUE}7-){ccolors.ENDC} True ve False'u aktif ve deaktif veya pozitif ve negatif olarak düşünebiliriz. Yani "while True" esasında "Aktif/Pozitif olduğu süreç boyunca şunu yap:" demek. Koşulu, yani burada run değişkeni oluyor bu, deaktif olduğunda kendini tekrarlamayı bırakıyor.

X-) Kodun tamamı sonraki sayfada.

{ccolors.WARNING}Sayfa 5/6{ccolors.ENDC}""")

#LastPage

LastPage = Page(f"""
{ccolors.IMORANGE}from{ccolors.ENDC} random {ccolors.IMORANGE}import{ccolors.ENDC} choice

choices  {ccolors.OPERATORS}= {ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Taş{ccolors.CODEGREY}", "{ccolors.STRINGG}Kağıt{ccolors.CODEGREY}", "{ccolors.STRINGG}Makas{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
winScore {ccolors.OPERATORS}= {ccolors.OKCYAN}3{ccolors.ENDC}

userScore {ccolors.OPERATORS}= {ccolors.OKCYAN}0{ccolors.ENDC}
computerScore {ccolors.OPERATORS}= {ccolors.OKCYAN}0{ccolors.ENDC}

run {ccolors.OPERATORS}= {ccolors.BOOLS}True{ccolors.ENDC}
{ccolors.OPERATORS}while{ccolors.ENDC} run{ccolors.CODEGREY}:{ccolors.ENDC}
    computerChoice = {ccolors.MODULES}choice{ccolors.YELLOW}({ccolors.ENDC}choices{ccolors.YELLOW}){ccolors.ENDC}
    userChoice = {ccolors.MODULES}input{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Seçim yapın (Taş, Kağıt, Makas): {ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.CODEGREY}.{ccolors.MODULES}lower{ccolors.YELLOW}(){ccolors.ENDC}
    
    {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice.{ccolors.ENDC}{ccolors.MODULES}lower{ccolors.ENDC}{ccolors.YELLOW}(){ccolors.ENDC} {ccolors.OPERATORS}=={ccolors.ENDC} userChoice{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: {ccolors.CODEGREY}",{ccolors.ENDC} computerChoice{ccolors.YELLOW}){ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Berabere{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}elif{ccolors.ENDC} userChoice {ccolors.OPERATORS}=={ccolors.ENDC} {ccolors.CODEGREY}"{ccolors.STRINGG}taş{ccolors.CODEGREY}":
        {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}Makas{ccolors.CODEGREY}":{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Makas{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyuncu kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
        {ccolors.OPERATORS}else{ccolors.CODEGREY}:
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Kağıt{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            computerScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}elif{ccolors.ENDC} userChoice {ccolors.OPERATORS}=={ccolors.ENDC} {ccolors.CODEGREY}"{ccolors.STRINGG}kağıt{ccolors.CODEGREY}":
        {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}Taş{ccolors.CODEGREY}":{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Taş{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyuncu kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW})
        {ccolors.OPERATORS}else{ccolors.CODEGREY}:
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Makas{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            computerScore {ccolors.OPERATORS}+={ccolors.ENDC} {ccolors.OKCYAN}1{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}elif{ccolors.ENDC} userChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}makas{ccolors.CODEGREY}":{ccolors.ENDC}
        {ccolors.OPERATORS}if{ccolors.ENDC} computerChoice {ccolors.OPERATORS}== {ccolors.CODEGREY}"{ccolors.STRINGG}Kağıt{ccolors.CODEGREY}":{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Kağıt{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            userScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1{ccolors.ENDC}
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyuncu kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW})
        {ccolors.OPERATORS}else{ccolors.CODEGREY}:
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar seçimi: Taş{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
            computerScore {ccolors.OPERATORS}+= {ccolors.OKCYAN}1
            {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Bilgisayar kazandı!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
    
    {ccolors.OPERATORS}if{ccolors.ENDC} userScore {ccolors.OPERATORS}=={ccolors.ENDC} winScore{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyunu kazandın!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
        run {ccolors.OPERATORS}= {ccolors.BOOLS}False
    {ccolors.OPERATORS}elif{ccolors.ENDC} computerScore {ccolors.OPERATORS}=={ccolors.ENDC} winScore{ccolors.CODEGREY}:{ccolors.ENDC}
        {ccolors.MODULES}print{ccolors.YELLOW}({ccolors.CODEGREY}"{ccolors.STRINGG}Oyunu kaybettin!{ccolors.CODEGREY}"{ccolors.YELLOW}){ccolors.ENDC}
        run {ccolors.OPERATORS}= {ccolors.BOLD}False

{ccolors.FAIL}Not!-){ccolors.ENDC} Çözüm için nasıl düşündüğümüzü, bilgisayara nasıl bunu anlatabildiğimize odaklan. Kodu birebir kopyalama. Önce sayfalardaki konseptleri tek tek anla ve o sayfanın konusunu kendin kodlamaya çalış. Kodunu da adım adım yani sayfa sayfa yap. O sayfada oyundaki hamleleri nasıl bir yerde tutabileceğini, oyunun kazanma puanını nasıl belirleyebileceğini anlattıysam değişken adlarını kendine göre düzelt ve öyle kodla. Her sayfada adım adım gittim bunu da senin de takip edebilmen için yaptım. Bu oyunu Taş-Kağıt-Makas yapma da Ateş-Su-Toprak şeklinde yap. Hangisi hangisini yener önce onu kombinasyonla. Beraber kalma durumunda rastgele birisine puan ver. Kısaca kendi kodunu kendin yaz. Burada sadece mantığını oturttun. Eğer kendinden bir şeyler katmazsan öğrenemezsin ve bu konu sıkıcı bir hale dönüşür. 

{ccolors.FAIL}Dipnot!-){ccolors.ENDC} Değişkenleri olabildiğince ingilizce yapmaya çalış. Eninde sonunda bu sektör için ingilizce gerekiyor. Hele Python tamamen ingilizceden ibaret. Bu hem senin kodlama karakteristliğini oluşturur hem de aşina olmaya başlarsın.
Saygılar.

{ccolors.WARNING}Sayfa 6/6{ccolors.ENDC}""")

B_Pages = [Page1, Page2, Page3, Page4, Page5, LastPage]