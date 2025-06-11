## OS-Specific Tools Projesi Yol Haritası
## Giriş
Bu proje, belirli işletim sistemlerinin (Windows, Linux, macOS) sunduğu benzersiz özelliklerden ve API'lerden faydalanarak, genel sistem yönetimi, otomasyon, performans izleme veya güvenlik araçları gibi çeşitli alanlarda OS'e özgü araçlar geliştirmeyi amaçlamaktadır. Proje, her işletim sistemi için optimize edilmiş çözümler sunmayı ve platformlar arası uyumluluğu mümkün olduğunca göz önünde bulundurarak, her platformun kendine özgü güçlerini kullanmayı hedeflemektedir. Bu yol haritası, projenin kapsamını, hedeflerini ve geliştirme aşamalarını detaylandırmaktadır.

## Ön Koşullar
Bu projeye başlamadan önce aşağıdaki ön koşulların karşılandığından emin olmalısın:

## Bilgi ve Beceriler
Python Programlama: İleri seviye Python bilgisi, özellikle OS ile etkileşim kurma, süreç yönetimi, dosya sistemi işlemleri konularında deneyim.
İşletim Sistemi Bilgisi:
Windows: Windows API (WinAPI), PowerShell, Komut İstemi (CMD) bilgisi.
Linux: Bash betikleme, Linux çekirdek kavramları, dosya sistemi (procfs, sysfs), paket yöneticileri bilgisi.
macOS: Shell betikleme (Bash/Zsh), AppleScript, macOS çerçeveleri bilgisi.
Sürüm Kontrol Sistemi: Git ve GitHub iş akışlarına hakimiyet.
Hata Ayıklama: Gelişmiş hata ayıklama teknikleri.

## Kütüphaneler (Python için)
Genel OS Etkileşimi:
os: Temel işletim sistemi işlemleri (dosya/dizin, çevre değişkenleri).
subprocess: Harici komutları çalıştırma.
shutil: Yüksek seviye dosya işlemleri.
Windows'a Özgü:
pywin32: Windows API'ye Python erişimi sağlar.
wmi: Windows Management Instrumentation (WMI) ile etkileşim için.
Linux'a Özgü:
psutil: Sistem ve süreç bilgilerini almak için (cross-platform olsa da Linux'ta detaylı).
distro: Linux dağıtım bilgilerini almak için.
macOS'a Özgü:
osascript: AppleScript komutlarını çalıştırmak için.
objc (PyObjC): Cocoa çerçevelerine erişim için (daha ileri seviye).
Diğer (Kullanım Alanına Göre):
logging: Detaylı loglama için.
argparse: Komut satırı argümanlarını işlemek için.
colorama: Konsol çıktısını renklendirmek için (cross-platform).

## Gerekli Araçlar
Sürüm Kontrol Sistemi: Git
Kod Düzenleyici / IDE: VS Code, PyCharm veya tercih edilen bir IDE.
İşletim Sistemi Ortamları: Projenin hedeflediği her bir işletim sistemine (Windows, Linux, macOS) erişim. (Sanal makineler veya ayrı cihazlar olabilir.)
Paket Yöneticileri: Hedef işletim sistemlerinin kendi paket yöneticileri (örn. apt, yum, brew, choco).

## Test Ortamı Kurma
Her hedef işletim sistemi için ayrı bir test ortamı kurulmalı ve izole edilmelidir.

1. Geliştirme Ortamı Kurulumu:
Her işletim sisteminde Python'ı (tercihen 3.x) ve pip'i yükle.
Her işletim sisteminde sanal ortam (virtual environment) oluştur ve etkinleştir. Bu, bağımlılık çakışmalarını önleyecektir.

python -m venv venv_<os_adi>
## source venv_<os_adi>/bin/activate   Linux/macOS
## venv_<os_adi>\Scripts\activate      Windows

İlgili OS için gerekli kütüphaneleri pip install komutuyla yükle.
 Windows için:
pip install pywin32 wmi colorama
 Linux için:
pip install psutil distro colorama
 macOS için:
pip install osascript colorama # PyObjC kurulumu daha karmaşık olabilir

2. OS-Specific Test Ortamları:
Windows: Bir Windows sanal makinesi (örn. Hyper-V, VirtualBox, VMware) veya fiziksel bir makine. Testler için yönetici ayrıcalıklarının olduğundan emin ol.
Linux: Çeşitli Linux dağıtımlarını (örn. Ubuntu, Fedora, Debian) içeren sanal makineler.
macOS: Bir macOS sanal makinesi (sınırlı olabilir) veya fiziksel bir Mac cihazı.

3. Temel Komut Testleri: Her ortamda basit OS komutlarını (örn. dir / ls, ipconfig / ifconfig, whoami) Python subprocess modülü ile çalıştırarak temel OS etkileşimlerinin çalıştığından emin ol.

## Temel Bileşenlerin Geliştirilmesi
Bu aşamada, her işletim sistemi için temel, platforma özgü işlevsellikleri geliştireceğiz.

1. Platform Algılama Modülü:
Çalışan işletim sistemini doğru bir şekilde algılayan bir modül (platform modülü kullanarak).
Bu modül, daha sonra hangi OS'e özgü kodun çalıştırılacağını belirleyecektir.

2. Temel Sistem Bilgileri Toplama Modülleri:
CPU Bilgileri: Çekirdek sayısı, kullanım oranı.
Bellek Bilgileri: Toplam, kullanılan, boş bellek.
Disk Bilgileri: Toplam, kullanılan, boş disk alanı.
Ağ Bilgileri: IP adresleri, ağ adaptörleri.
Süreç Bilgileri: Çalışan süreçlerin listesi, PID'leri.

3. Basit Otomasyon Fonksiyonları:
Dosya İşlemleri: Belirli bir dizinde dosya oluşturma/silme, kopyalama/taşıma.
Dizin İşlemleri: Dizin oluşturma/silme.
Uygulama Başlatma/Durdurma: Basit bir uygulamayı başlatma veya bir süreci PID ile sonlandırma.

## Gelişmiş Geliştirmeler
Temel işlevler tamamlandıktan sonra, daha karmaşık ve kullanışlı özelliklere odaklanılacaktır.
1. Gelişmiş Süreç Yönetimi:
Süreç ağacını görüntüleme.
Süreçlerin kaynak tüketimini (CPU, bellek) izleme.
Süreçlere öncelik atama.

2. Sistem Kaynak İzleme Paneli (CLI veya Basit GUI):
Gerçek zamanlı olarak CPU, bellek, disk, ağ kullanımını gösteren bir arayüz.
Trendleri göstermek için geçmiş verileri saklama yeteneği.

3. Otomatik Görev Yönetimi:
Belirli olaylara (örn. düşük disk alanı, yüksek CPU kullanımı) tepki veren otomatik görevler.
Zamanlanmış görevler (örn. Windows Görev Zamanlayıcı, Cron Jobs) için entegrasyon.

4. Güvenlik Odaklı Araçlar (Temel):
Açık portları listeleme.
Güvenlik duvarı kurallarını sorgulama (Windows Defender Firewall, iptables).
Kullanıcı hesap bilgilerini sorgulama.

5. Kullanıcı Arayüzü (GUI - İsteğe Bağlı):
Tkinter veya PyQt gibi kütüphanelerle basit bir GUI oluşturarak daha kullanıcı dostu bir deneyim sunma.
Her OS için native görünümlü GUI bileşenlerini kullanma araştırması.

## Geliştirmelerin Test Edilmesi
Kapsamlı testler, aracın farklı işletim sistemlerinde güvenilir ve doğru çalışmasını sağlamak için hayati önem taşır.
1. Birim Testleri:
Her bir OS'e özgü fonksiyon ve modül için bağımsız testler yaz. (Örn. unittest veya pytest kullanarak).
Mocking kullanarak OS bağımlılıklarını izole et.

2. Entegrasyon Testleri:
Farklı modüllerin (örn. platform algılama ve OS'e özgü işlevler) birlikte düzgün çalıştığından emin olmak için testler yap.
Her hedef OS'de ayrı ayrı çalıştırma testleri.

3. Fonksiyonel Testler:
Aracın beklenen çıktıları doğru bir şekilde ürettiğini doğrula (örn. CPU kullanım yüzdesinin doğru olması).
Gerçek dünya senaryolarını simüle eden testler.

4. Performans Testleri:
Aracın kaynak tüketimini (CPU, bellek) ve yanıt süresini izle.
Farklı yükler altında (örn. çok sayıda süreç izlerken) performansını değerlendir.

5. Güvenlik Testleri (Temel):
Kullanıcı ayrıcalıkları ile ilgili testler (örn. yönetici ayrıcalıkları gerektiren işlemlerin düzgün hata vermesi).
Girdi doğrulama ve enjeksiyon zafiyetlerine karşı kontroller.

## Karşı Önlemler ve En İyi Uygulamalar
Projenin güvenilirliğini, sürdürülebilirliğini ve güvenliğini sağlamak için uygulanacak stratejiler.
1. Güvenlik:
Ayrıcalık Yönetimi: Yönetici/root ayrıcalığı gerektiren işlemler için net gereksinimler ve hata mesajları. Gerekmedikçe bu ayrıcalıkları kullanmaktan kaçınma.
Girdi Doğrulama: Harici kaynaklardan veya kullanıcıdan gelen tüm girdileri dikkatlice doğrula.
Sınırlı Yetki Prensibi: Araçlara yalnızca görevlerini yerine getirmek için gerekli olan minimum ayrıcalıkları ver.
Güvenli Komut Yürütme: subprocess kullanırken shell=True kullanımından kaçın. Güvenlik açıkları için bilinçli ol.

2. Hata Yönetimi ve Loglama:
Kapsamlı hata işleme mekanizmaları (try-except blokları).
Anlaşılır ve bilgilendirici hata mesajları.
logging modülünü kullanarak detaylı günlükler oluştur (hata, uyarı, bilgi seviyeleri).

3. Ölçeklenebilirlik ve Modülerlik:
Kodu küçük, yeniden kullanılabilir fonksiyonlara ve sınıflara böl.
Her işletim sistemi için ayrı modüller oluşturarak (örn. os_tools/windows.py, os_tools/linux.py) kodu düzenli tut.
Gelecekte yeni OS'ler veya özellikler eklemeyi kolaylaştıracak bir mimari tasarla.

4. Dokümantasyon:
README.md dosyasında projenin amacını, kurulumunu ve kullanımını açıkça belirt.
Kod yorumları ve docstring'ler kullanarak fonksiyonların ve sınıfların ne yaptığını açıkla.
Her OS'e özgü özelliklerin ve gereksinimlerin detaylı belgelerini sağla.

5. Test Edilebilirlik:
Kodun test edilebilirliğini artırmak için bağımlılıkları minimize et.
Fonksiyonları saf (pure functions) olacak şekilde tasarla.

6. Kullanıcı Geri Bildirimi:
Kullanıcı geri bildirimlerini topla ve bunlara göre projeyi geliştir.


## Sonuç
Bu yol haritası, OS-Specific Tools projesi için kapsamlı bir çerçeve sunmaktadır. Her aşamanın dikkatli bir şekilde planlanması ve uygulanması, projenin başarılı bir şekilde tamamlanmasını sağlayacaktır. İşletim sistemlerinin derinliklerine inmek, güçlü ve optimize edilmiş araçlar yaratma fırsatı sunar. Bu proje, hem teknik becerilerini geliştirmek hem de farklı işletim sistemlerinin iç işleyişine dair derinlemesine bilgi edinmek için mükemmel bir fırsattır. Unutma, geliştirme süreci iteratif olacaktır; bu nedenle esnek kalmaya ve öğrendikçe yol haritanı uyarlamaya hazır ol.
