function confirmDelete(bicycleId) {
    const popup = document.getElementById('popup');
    popup.style.display = 'block';

    const confirmButton = document.getElementById('confirmButton');
    confirmButton.onclick = function () {
        const deleteURL = `/bicycle_delete/${bicycleId}`;

        fetch(deleteURL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({}),
        })
        .then(response => {
            if (response.ok) {
                // 削除が成功した場合、リストページにリダイレクト
                window.location.href = "{% url 'App:list' %}";
            } else {
                // 削除が失敗した場合、エラーメッセージを表示するなどの処理を追加
                console.error('削除に失敗しました。');
            }
        })
        .catch(error => {
            console.error('エラーが発生しました:', error);
        });
    };

    const cancelButton = document.getElementById('cancelButton');
    cancelButton.onclick = function () {
        popup.style.display = 'none';
    };
}