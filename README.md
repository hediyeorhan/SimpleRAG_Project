# SimpleRAG

Bu çalışmada Google AI tarafından geliştirilen yapay zekâ Gemini API'ı kullanılarak basit bir RAG (Retrieval-Augmented Generation) projesi geliştirilmiştir. 

Projede __.env__ dosyasında içeriğinde şu veriler bulunmaktadır.

• GEMINI_API_KEY=

• LANGCHAIN_API_KEY=

• LANGCHAIN_TRACING_V2=true

• LANGCHAIN_PROJECT=PROJECT_NAME

Projede, Gemini AI ile birlikte Langchain framework'ü kullanılmıştır. Langchain, büyük dil modelleri ile uygulama geliştirilmesinde kullanılmaktadır. Zincir yapısında LLM'lerin birbirleri ile ve insanlar ile konuşmasını sağlamaktadır. Döküman okuma-yükleme, chat geçmişi tutma, embedding işlemleri ve vektör database işlemleri için langchain framework'ünden faydalanılmıştır. LangChain, LLM'ler ile entegrasyon sağlayarak özelleştirilmiş sorgu yönetimi sunmaktadır.

<h3> RAG </h3>

<br>
Bu çalışmada, bir web sayfasından çekilen veriler, RAG kullanılarak büyük dil modeli (LLM) ile entegre bir yapıda değerlendirilmiştir. Toplanan veriler, RecursiveCharacterTextSplitter mekanizması ile 1000 karakterlik parçalara ayrılmış ve her parça arasında 200 karakterlik bir örtüşme sağlanmıştır. Bu sayede, uzun metinlerin anlamlı parçalara bölünmesi sağlanmış, daha verimli bir bilgi arama ve cevap üretme süreci elde edilmiştir. Sonrasında, bu verilerle özelleştirilmiş bir soru-cevap mekanizması oluşturulmuştur.

Bu çalışmada embedding fonksiyonu olarak __HuggingFaceEmbeddings__ kullanılmıştır.
<br>
Çalışmada vektör veri tabanı olarak Chroma kullanılmıştır. Chroma open source bir vektör veri tabanıdır.
<br>

LangChain Hub üzerinden __rlm/rag-prompt__ adlı özel bir prompt şablonu çekilmiş ve bu şablon, verilerle etkileşime girerek büyük dil modeline yönelik anlamlı soruların oluşturulmasına yardımcı olmuştur. Bu işlem, RAG sürecinin bir parçası olarak, modelin doğru ve bağlama dayalı cevaplar verebilmesi için gerekli olan talimatları içermektedir. LangChain hub üzerinden kullanılacak projeye uygun promptlar seçilebilmektedir. LangChain hub kendi istediğimiz şekilde özelleştirilmiş prompt'lar oluşturmaya olanak sağlamaktadır.


<br>

Çalışmanın örnek çıktıları Şekil 1'de görülmektedir.

<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/e353dbfa-f450-4ca8-af3b-b5d4bfdd49b9" alt="image">
</div>
Şekil 1. Örnek çıktı

