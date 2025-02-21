document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const progressBar = document.getElementById("progress-bar");
    const progress = document.querySelector(".progress");
    const successMessage = document.getElementById("success-message");
    const inputField = document.querySelector("input[name='url']");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Previne o recarregamento da página

        const formData = new FormData(form);
        progressBar.style.display = "block"; // Exibe a barra de progresso
        progress.style.width = "10%"; // Inicia com 10% preenchido para indicar ação
        successMessage.style.display = "none";

        let progressInterval = setInterval(() => {
            let currentWidth = parseFloat(progress.style.width);
            if (currentWidth < 90) {
                progress.style.width = (currentWidth + 5) + "%";
            }
        }, 500);

        fetch("/download", {
            method: "POST",
            body: formData,
        })
        .then(response => {
            clearInterval(progressInterval);
            progress.style.width = "100%"; // Define 100% ao finalizar
            return response.json();
        })
        .then(data => {
            if (data.success) {
                successMessage.innerText = data.success;
                successMessage.style.display = "block";
                setTimeout(() => {
                    progress.style.width = "0%";
                    progressBar.style.display = "none";
                    inputField.value = "";
                    successMessage.style.display = "none";
                }, 5000);
            } else if (data.error) {
                alert(data.error);
            }
        })
        .catch(error => console.error("Erro:", error));
    });
});