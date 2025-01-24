// Bildirim Gösterme Fonksiyonu
function showNotification(message) {
    const notification = document.getElementById('notification');
    notification.textContent = message; // Mesajı ayarla
    notification.classList.add('visible'); // Görünür yap

    // 3 saniye sonra bildirimi gizle
    setTimeout(() => {
        notification.classList.remove('visible');
    }, 3000);
}

// Silme İşlemini Yakalama
const todoList = document.getElementById('todoList');

// Tüm "Sil" bağlantılarına tıklama olayını yakala
todoList.addEventListener('click', (event) => {
    if (event.target.classList.contains('deleteLink')) {
        event.preventDefault(); // Varsayılan sayfa yenilemeyi engelle
        const listItem = event.target.parentElement; // Silinecek öğeyi seç
        const itemText = listItem.querySelector('span').textContent.trim(); // Öğe adını al
        listItem.remove(); // Öğeyi DOM'dan kaldır
        showNotification(`"${itemText}" silindi!`); // Bildirimi göster
    }
});