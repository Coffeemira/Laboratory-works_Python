// Добавляем обработчик для всех кнопок "свернуть"
var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        // Находим родительский элемент (блок статьи)
        var post = e.target.parentElement;

        // Проверяем, есть ли у поста класс "folded"
        if (post.classList.contains("folded")) {
            // Если есть — разворачиваем
            post.classList.remove("folded");
            e.target.innerHTML = "свернуть";
        } else {
            // Если нет — сворачиваем
            post.classList.add("folded");
            e.target.innerHTML = "развернуть";
        }
    });
}