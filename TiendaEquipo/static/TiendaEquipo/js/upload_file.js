document.getElementById("id_foto").onchange = function () {
    document.getElementById("uploadFile").value = this.files[0].name;
};