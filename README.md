# <h2> Türkçe Açıklama </h2>
---
## <h4> Proje Amacı </h4>
Bu proje, başıboş sokak hayvanlarının özellikle çocuklara ve savunmasız bireylere zarar verebileceği durumların önüne geçmeyi amaçlamaktadır. Artan sokak hayvanı popülasyonu ve insanlarla beklenmedik temasların yarattığı riskler, hızlı müdahaleyi gerektiriyor. Bu sistem, kamera veya video akışı üzerinden anlık olarak köpek ve insan tespiti yaparak, gerekli durumlarda anında e-posta uyarısı gönderir. Böylece yetkililerin veya sorumluların hızlıca haberdar olması sağlanır.

## <h4> Projenin Amaçladığı Faydalar </h4>

- **Hassas bölgelerde** (okul bahçeleri, parklar, oyun alanları) devreye alınarak, hem hayvanların hem de insanların zarar görmesini önler.
- **Belediye ve barınak ekiplerinin** hızlı müdahalesine olanak tanır. Özellikle geceleri hayvanların saldırgan davranışları artabilir ve erken müdahale hayat kurtarabilir.
- **Çocukların güvenliğini** sağlamak daha kolay hale gelir. Çocuk parklarında ya da kalabalık etkinlik alanlarında tehlike algılandığında, sorumlu kişilere hemen haber verilir.
- **Hayvan dostu bir yaklaşım** sunar. Hayvanlara zarar vermeden çözüm sunarken, ani karşılaşmalarda oluşabilecek kazaların önüne geçer.
- **Akıllı şehir çözümleri** arasında yer alabilir. Belediyeler bu sistemleri entegre ederek, şehir güvenliğini artırabilir ve hayvan-insan uyumunu iyileştirebilir.
  
## <h4> Projenin Çalışma Mantığı </h4>
Sistem, YOLO modelini kullanarak canlı kamera akışı veya video içeriğinden insan ve köpek tespiti yapar. Eğer aynı anda hem insan hem köpek algılanırsa, otomatik olarak bir uyarı e-postası gönderir. E-posta gönderim işlemi, uygulama şifresi ile güvenli hale getirilir ve gereksiz tekrarların önlenmesi için bir bekleme süresi (cooldown) uygulanır.
Bu sayede, kritik durumlarda zamanında haberdar olunarak, olası kazaların önüne geçilir ve doğru kişiler hemen harekete geçebilir. Proje hem reaktif bir çözüm sunar (tehlike anında anında uyarı) hem de proaktif bir güvenlik önlemi olarak kullanılabilir.

## <h4> Kurulum Adımları </h4>

### <h5> 1. Gerekli Kütüphaneleri Yükleyin </h5>
Terminal veya komut satırında şu komutu çalıştırın:
```bash
pip install -r requirements.txt
```

### <h5> 2. Google Uygulama Şifresi Oluşturun </h5> 
- **Google hesabınızda 2 adımlı doğrulama** etkin olmalıdır.  
- [Google Uygulama Şifresi Oluştur](https://myaccount.google.com/apppasswords) bağlantısından yeni bir şifre oluşturun.

### <h5> 3. mail.py Dosyasını Düzenleyin  </h5>
- **`sender_email`**: Gönderici e-posta adresini yazın.  
- **`sender_password`**: Google uygulama şifresini buraya girin.  
- **`receiver_email`**: E-posta uyarısının gönderileceği adresi belirtin.

### <h5> 4. Model Dosyasını Edinin </h5>
- **`dog_best5.pt`** dosyasını projeye ekleyin. Model dosyasının doğru dizinde olduğundan emin olun.

### <h5> 5. Projeyi Çalıştırın </h5>  
Terminalden şu komutu çalıştırarak projeyi başlatın:
```bash
python main.py
```

---

## Kullanıcıların Dikkat Etmesi Gereken Noktalar  

1. **Model dosyası**:  
   - **`dog_best5.pt`** dosyasının doğru dizinde olduğundan emin olun.

2. **E-posta gönderim gecikmesi**:  
   - **`email_cooldown`** ayarını ihtiyaçlarınıza göre ayarlayabilirsiniz.

3. **E-posta ayarları**:  
   - Gönderici e-posta için **uygulama şifresi** kullanılması zorunludur.

---

# <h2> English Explanation </h2>

---

## <h4> Project Objective </h4>
This project aims to prevent situations where stray animals, especially dogs, could harm children or vulnerable individuals. The growing stray animal population and the risks posed by unexpected encounters with people require quick intervention. This system provides real-time detection of dogs and humans via camera or video stream and sends an instant email alert when necessary. This ensures that authorities or responsible parties are promptly notified.

## <h4> Project Benefits </h4>

- **Protects sensitive areas** (schoolyards, parks, playgrounds) by preventing harm to both animals and humans.
- **Enables quick intervention** by municipal and shelter teams. Animals, especially at night, may exhibit aggressive behavior, and early intervention can save lives.
- **Makes it easier to ensure the safety of children.** When a threat is detected in playgrounds or crowded event areas, responsible individuals are immediately alerted.
- **Offers an animal-friendly approach.** It provides a solution without harming animals, preventing accidents that may occur during sudden encounters.
- **Can be part of smart city solutions.** Municipalities can integrate this system to enhance city safety and improve animal-human coexistence.

## <h4> How the System Works </h4>
The system uses the YOLO model to detect humans and dogs from live camera feeds or video content. If both a human and a dog are detected simultaneously, an automatic email alert is sent. The email sending process is secured with an application password, and a cooldown period is applied to prevent unnecessary repetitions.
This ensures timely notifications in critical situations, allowing the right people to act immediately. The project offers both a reactive solution (alerting during danger) and a proactive security measure.

## <h4> Installation Steps </h4>

### <h5> 1. Install the Required Libraries </h5>
Run the following command in the terminal or command line:
```bash
pip install -r requirements.txt
```

### <h5> 2. Create a Google App Password </h5> 
- **Two-step verification** must be enabled for your Google account.
- Create a new password from the [Google App Passwords](https://myaccount.google.com/apppasswords) link.

### <h5> 3. Edit the mail.py File </h5>
- **`sender_email`**: Enter the sender's email address.  
- **`sender_password`**: Enter the Google app password here.  
- **`receiver_email`**: Specify the address where the email alert will be sent.

### <h5> 4. Obtain the Model File </h5>
- Add the **`dog_best5.pt`** file to the project. Ensure that the model file is in the correct directory.

### <h5> 5. Run the Project </h5>  
Run the following command in the terminal to start the project:
```bash
python main.py
```

---

## Important Notes for Users  

1. **Model file**:  
   - Make sure the **`dog_best5.pt`** file is in the correct directory.

2. **Email delay**:  
   - You can adjust the **`email_cooldown`** setting according to your needs.

3. **Email settings**:  
   - Using an **app password** for the sender email is mandatory.
