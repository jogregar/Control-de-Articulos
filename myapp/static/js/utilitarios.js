if (document.getElementById("newcategoria")){
    document.getElementById("newcategoria").addEventListener("click",() => {
        location.href="/admincategorias/0";
    });
}

if (document.getElementById("cancelar1")){
    document.getElementById("cancelar1").addEventListener("click",(e) => {
        e.preventDefault();
        location.href="/categorias/";
    });
}

if (document.getElementById("cancelar2")){
    document.getElementById("cancelar2").addEventListener("click",(e) => {
        e.preventDefault();
        location.href="/articulos/";
    });
}

if (document.querySelectorAll('.eliminar-btn')) {
    const botonesEliminar = document.querySelectorAll('.eliminar-btn');

    botonesEliminar.forEach((boton) => {
        boton.addEventListener('click', (e) => {
            e.preventDefault();
            const enlace = boton.parentElement;
            Swal.fire({
                title: "Eliminar Registro",
                text: "Esta acción no se puede deshacer",
                imageUrl: "/static/img/Papelera.png",
                imageWidth: 400,
                imageHeight: 200,
                showCancelButton: true,
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                confirmButtonText: "Eliminar"
            }).then((result) => {
                if (result.isConfirmed) {
                    location.href = enlace.getAttribute('href');
                }
            });
        });
    });
}
